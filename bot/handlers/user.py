
from telegram import Update,  User
from telegram.ext import CallbackContext, ConversationHandler
from db.functions.user import register
from bot.keyboards.user import main_keyboard_markup
from bot import states
from telegram import ParseMode


def start(update: Update, context: CallbackContext) -> None:
    user: User = update.effective_user
    register(user.id, user.first_name,
             user.last_name)

    update.message.reply_text(
        "You are in main menu",
        reply_markup=main_keyboard_markup
    )

    return ConversationHandler.END


def add_word(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        "Yangi so'zni kiriting\n\n<b>so'z</b>\n<i>tarjima</i>\n\nSo'zni rasm orqali yoki rasm kiritimsadan kiritish mumkin.",
        parse_mode=ParseMode.HTML
    )

    return states.NEW
