import logging
import uuid

from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from dataclass_csv import DataclassReader
import csv
from dataclasses import dataclass

from config import make_config
from src.api.recomendation_service import RecomendationService
from src.nlp.prolog.command_dispatcher import CommandDispatcherProlog
from src.nlp.nlprocessor import NLProcessor
from src.domain.picture import Picture
from src.repositories.pirtures_repo import PicturesRepositoryList
from src.rec_system.recomendation_system import RecomendationSystem
from src.repositories.conversation_context_repo import (
    ConversationContextRepositoryList,
)
from src.repositories.user_repo import UserRepositoryList
from src.telegram_interface.commands import *
from src.rec_system.filter import calc_ranger
from src.rec_system.domain import calc_measure_main, calc_measure_money


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def calc_measure_function(items, calc_func):
    min_values = calc_ranger(items)
    measure_matrix_dict = dict(
        [
            (
                item1.name,
                dict([(item2.name, calc_func(item1, item2, min_values)) for item2 in items]),
            )
            for item1 in items
        ]
    )
    return measure_matrix_dict


@dataclass
class DatasetItem:
    name: str
    full_name: str
    width: int
    height: int
    death: int
    sale_price: int
    country: str = ""
    style: str = ""
    subject: str = ""
    genre: str = ""
    medium: str = ""
    exhibition: bool = False
    for_sale: bool = False
    restored: bool = False


def from_dataset_item_to_pic(item: DatasetItem) -> Picture:
    pic = Picture(
        id=uuid.uuid1(),
        name=item.name,
        country=item.country,
        death=item.death,
        exhibition=item.exhibition,
        for_sale=item.for_sale,
        full_name=item.full_name,
        genre=item.genre,
        height=item.height,
        medium=item.medium,
        restored=item.restored,
        sale_price=item.sale_price,
        style=item.style,
        subject=item.subject,
        width=item.width,
    )
    return pic


config = make_config()
picture_repo = PicturesRepositoryList()
data_root = config["DATA_PATH_ROOT"]
with open(f"{data_root}/query-rk1-aicourse-10-14-2023-QueryResult.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    reader = DataclassReader(csv_file, DatasetItem, validate_header=False)

    for item in reader:
        pic = from_dataset_item_to_pic(item)
        picture_repo.create_picture(pic)


user_repo = UserRepositoryList()
conv_ctx_repo = ConversationContextRepositoryList()
dispatcher = CommandDispatcherProlog(config)
dispatcher.registrate_cmd("r_hello", HelloCommandContructor())
dispatcher.registrate_cmd("r_911", SosCommandContructor())
dispatcher.registrate_cmd("r_for_pleasure", ForPleasureCommandContructor())

dispatcher.registrate_cmd("r_change_strategy", ChangeStrategyCommandContructor(user_repo))
dispatcher.registrate_cmd("r_show_strategy", ShowStrategyCommandContructor())
dispatcher.registrate_cmd("r_change_measure", ChangeMeasureCommandContructor(user_repo))
dispatcher.registrate_cmd("r_show_measure", ShowMeasureCommandContructor())
dispatcher.registrate_cmd("r_show_possible_strategies", ShowPossibleStrategiesCommandContructor())
dispatcher.registrate_cmd("r_show_possible_measures", ShowPossibleMeasuresCommandContructor())

dispatcher.registrate_cmd("r_add_filter", AddFilterCommandContructor())
dispatcher.registrate_cmd(
    "r_add_filter_with_value", AddFilterWithValueCommandContructor(user_repo)
)
dispatcher.registrate_cmd("r_reset_filter", ResetFilterCommandContructor())
dispatcher.registrate_cmd("r_show_filters", ShowFiltersCommandContructor())
dispatcher.registrate_cmd(
    "r_filter_value_eq", FilterValueEqCommandContructor(user_repo, conv_ctx_repo)
)

dispatcher.registrate_cmd("r_show_likes", ShowLikesCommandContructor(picture_repo))
dispatcher.registrate_cmd("r_show_dislikes", ShowDislikesCommandContructor(picture_repo))
dispatcher.registrate_cmd("r_like_writer", LikeWriterCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_like_only", LikeOnlyCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_hate_writer", HateWriterCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_hate_only", HateOnlyCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_hate_picturers", HatePicturersCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_not_like_writer", NotLikeWriterCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_not_like_only", NotLikeOnlyCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_not_hate_writer", NotHateWriterCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_not_hate_only", NotHateOnlyCommandContructor(user_repo, picture_repo))
dispatcher.registrate_cmd("r_not_hate_picturers", NotHatePicturersCommandContructor(user_repo, picture_repo))

dispatcher.registrate_cmd(
    "r_suggest_something", SuggestSomethingCommandContructor(user_repo, picture_repo)
)
dispatcher.registrate_cmd(
    "r_show_something_verbose", ShowSomethingVerboseCommandContructor(user_repo, picture_repo)
)

nlprocessor = NLProcessor(dispatcher, conv_ctx_repo)
rec_system = RecomendationSystem(picture_repo)
pictures = picture_repo.select_all()
rec_system.add_measure_dict("General-driven", calc_measure_function(pictures, calc_measure_main))
rec_system.add_measure_dict("Money-driven", calc_measure_function(pictures, calc_measure_money))
rec_service = RecomendationService(nlprocessor, user_repo, conv_ctx_repo, rec_system)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_uuid = uuid.UUID(int=user_id)

    # TODO: check if not exists
    rec_service.create_user(user_uuid)

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Я бот, пожалуйста, поговорите со мной!"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_uuid = uuid.UUID(int=user_id)

    response_text = rec_service.process_text(user_uuid, update.message.text)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Извините, я не понял эту команду."
    )


if __name__ == "__main__":
    TOKEN = config["TOKEN"]
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    msg_handler = MessageHandler(filters.TEXT, message_handler)
    application.add_handler(msg_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()
