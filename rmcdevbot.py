from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()

BACKUP_COUNT = 5
MAX_LOG_WEIGHT = 52428800

logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
    filename="bot_log.log",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)
handler = RotatingFileHandler(
    "bot_log.log",
    maxBytes=MAX_LOG_WEIGHT, backupCount=BACKUP_COUNT
)
logger.addHandler(handler)


BOT_TOKEN = os.getenv('BOT_TOKEN')


def actual_po(update, context):
    chat = update.effective_chat
    text = 'Последняя версия ПО: 1.1.2'
    context.bot.send_message(chat.id, text)


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    keyboard = ReplyKeyboardMarkup(
        [['/act_po']],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    context.bot.send_message(
        chat_id=chat.id,
        text='Приветствую, {}!'.format(name),
        reply_markup=keyboard
    )


def main():
    updater = Updater(token=BOT_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('act_po', actual_po))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()