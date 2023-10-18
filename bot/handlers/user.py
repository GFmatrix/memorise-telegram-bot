
from telegram import Update,  User
from telegram.ext import CallbackContext, ConversationHandler, CallbackContext
from db.functions.user import get_user_lang, register, user_data_reset
from bot.keyboards.user import *
from bot import states
from telegram import ParseMode


def start(update: Update, context: CallbackContext) -> None:
    user: User = update.effective_user
    register(user.id, user.first_name,
             user.last_name)
    try: update.message.reply_text(
        "You are in main menu",
        reply_markup=main_keyboard_markup
    )
    except: 
        query = update.callback_query
        query.edit_message_text(
            "You are in main menu",
            reply_markup=main_keyboard_markup)

    return ConversationHandler.END


def add_word(update: Update, context: CallbackContext):

    update.message.reply_text(
        "Yangi so'zni kiriting\n\n<b>so'z inglischa</b>\n<i>ruscha</i>\n<i>o'zbekcha</i>\n\nSo'zni rasm orqali yoki rasm kiritimsadan kiritish mumkin.",
        parse_mode=ParseMode.HTML
    )

    return states.NEW

def settings(update: Update, context: CallbackContext):
    query = update.callback_query
    
    query.message.edit_text(
        "You are in settings menu", reply_markup=settings_keyboard_markup
    )
    query.answer()
    return states.SETTINGS

def reset(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.message.edit_text(
        "Are you sure to reset all your data?", reply_markup=confirmation_keyboard_markup
    )
    return states.RESET_CONFIRMATION

def reset_confirm(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer('Your data has been reset')
    
    user_data_reset(update.effective_user.id)
    settings(update, context)
    # query.edit_message_text(
    #     "You are in settings menu", reply_markup=settings_keyboard_markup
    # )
    
    return states.SETTINGS

def reset_denied(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    settings(update, context)
    # query.edit_message_text(
    #     "You are in settings menu", reply_markup=settings_keyboard_markup
    # )
    return states.SETTINGS

def back_to_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    start(update, context)
    # query.edit_message_text(
    #     "You are in main menu",
    #     reply_markup=main_keyboard_markup
    # )

    return ConversationHandler.END

def language(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    learning_lang, translation_lang = get_user_lang(update.effective_user.id)
    query.edit_message_text(
        "You are in settings menu",
        reply_markup=InlineKeyboardMarkup(language_change(learning_lang, translation_lang))
    )