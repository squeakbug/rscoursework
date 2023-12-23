import logging
import uuid

from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

from config import make_config
from src.api.recomendation_service import RecomendationService
from src.nlp.prolog.command_dispatcher import CommandDispatcherProlog
from src.domain.commands import HelloCommandContructor


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

config = make_config()
dispatcher = CommandDispatcherProlog(config)
dispatcher.registrate_cmd("r_hello", HelloCommandContructor())
rec_service = RecomendationService(dispatcher)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.user_shared.user_id
    user_uuid = uuid.UUID(int=user_id)

    # TODO: check if not exists
    rec_service.create_user(user_uuid)

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command."
    )


if __name__ == "__main__":
    TOKEN = config["TOKEN"]
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()
