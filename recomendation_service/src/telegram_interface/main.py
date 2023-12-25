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


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


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


picture_repo = PicturesRepositoryList()
with open("../data/query-rk1-aicourse-10-14-2023-QueryResult.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    reader = DataclassReader(csv_file, DatasetItem, validate_header=False)

    for item in reader:
        pic = from_dataset_item_to_pic(item)
        picture_repo.create_picture(pic)


config = make_config()
user_repo = UserRepositoryList()
conv_ctx_repo = ConversationContextRepositoryList()
dispatcher = CommandDispatcherProlog(config)
dispatcher.registrate_cmd("r_hello", HelloCommandContructor())
dispatcher.registrate_cmd("r_change_strategy", ChangeStrategyCommandContructor(user_repo))
dispatcher.registrate_cmd("r_show_strategy", ShowStrategyCommandContructor())
dispatcher.registrate_cmd("r_change_measure", ChangeMeasureCommandContructor(user_repo))
dispatcher.registrate_cmd("r_show_measure", ShowMeasureCommandContructor())
nlprocessor = NLProcessor(dispatcher, conv_ctx_repo)
rec_system = RecomendationSystem(picture_repo)
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
