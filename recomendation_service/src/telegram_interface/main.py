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
from recomendation_service.src.rec_system.commands.other_cmds.hello_command import (
    HelloCommandContructor,
)
from src.rec_system.recomendation_system import RecomendationSystem
from recomendation_service.src.repositories.conversation_context_repo import (
    ConversationContextRepositoryList,
)
from recomendation_service.src.repositories.user_repo import UserRepositoryList


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
    pic = Picture(id=uuid.uuid1(), name=item.name)
    return pic


picture_repo = PicturesRepositoryList()
with open("../data/query-rk1-aicourse-10-14-2023-QueryResult.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    reader = DataclassReader(csv_file, DatasetItem, validate_header=False)

    for item in reader:
        pic = from_dataset_item_to_pic(item)
        picture_repo.create_picture(pic)


config = make_config()
dispatcher = CommandDispatcherProlog(config)
dispatcher.registrate_cmd("r_hello", HelloCommandContructor())
user_repo = UserRepositoryList()
conv_ctx_repo = ConversationContextRepositoryList()
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
