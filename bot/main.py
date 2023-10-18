from ast import Call
import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from bot import config
from bot.handlers import user
from bot.handlers import word
from bot.keyboards import user as user_keyboard
from bot import states
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', user.start),
            CommandHandler('add', user.add_word),
            CallbackQueryHandler(
                word.new_words_start, pattern=user_keyboard.NEW_WORDS_KEY),
            CallbackQueryHandler(
                word.new_words_update, pattern='^known-'),
            CallbackQueryHandler(
                word.new_words_update, pattern='^learn-'),
            CallbackQueryHandler(
                word.review_words_start, pattern=user_keyboard.REVIEW_KEY),
            CallbackQueryHandler(
                word.review_words_update, pattern='^review_known-'),
            CallbackQueryHandler(
                word.review_words_update, pattern='^review_learn-'),
            CallbackQueryHandler(
                word.check_word, pattern='^check-'),
            CallbackQueryHandler(
                user.start, pattern='add_cancel'),
            CallbackQueryHandler(
                word.add_new_word, pattern='add_approve'),
            CallbackQueryHandler(
                user.settings, pattern=user_keyboard.SETTINGS_KEY),

            # type: ignore
        ],
        states={
            states.NEW: [
                CallbackQueryHandler(
                    word.cancel_word, pattern='add_cancel'),
                CallbackQueryHandler(
                    word.add_new_word, pattern='add_approve'),
                MessageHandler(Filters.all, word.add_word),],
            states.SETTINGS: [
                CallbackQueryHandler(
                    user.reset, pattern=user_keyboard.RESET_KEY),
                CallbackQueryHandler(
                    user.back_to_menu, pattern=user_keyboard.BACK_KEY),
                CallbackQueryHandler(
                    user.language, pattern=user_keyboard.LANGUAGE_KEY),
            ],
            # states.LANGUAGE:[
            #     CallbackQueryHandler()
            # ],
            states.RESET_CONFIRMATION: [
                CallbackQueryHandler(
                    user.reset_confirm, pattern=user_keyboard.RESET_CONFIRMATION_KEY),
                CallbackQueryHandler(
                    user.reset_denied, pattern=user_keyboard.RESET_DENIED_KEY),
            ]
        },
        fallbacks=[CommandHandler('start', user.start),],
    )

    dispatcher.add_handler(conv_handler)
    # on different commands - answer in Telegram

    # Start the Bot
    updater.start_polling()
    updater.idle()
