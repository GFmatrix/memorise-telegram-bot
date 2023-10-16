
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from db.functions.user import register
from bot.keyboards.user import main_keyboard_markup
from db.functions.word import get_user_word, users_words_create, get_user_review_word, users_words_update
from db.functions.user import get_user_data
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def new_words(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()
    user = get_user_data(query.from_user.id)
    word = get_user_word(user.id)

    if word:

        word_keyboard = [
            [
                InlineKeyboardButton(
                    "✅ Known", callback_data=f"known-{word.id}-{user.id}-1"),
                InlineKeyboardButton(
                    "♻️ Learn", callback_data=f"learn-{word.id}-{user.id}-2"),
            ],

        ]

        word_keyboard_markup = InlineKeyboardMarkup(word_keyboard)

        query.edit_message_text(
            text=f"{word.word}", reply_markup=word_keyboard_markup)
    else:
        query.edit_message_text(text="No words")


def update_words(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data.split('-')
    query.answer()
    if len(data) > 3:
        users_words_create(data[2], data[1], data[3])
    user = get_user_data(query.from_user.id)
    word = get_user_word(user.id)
    print(word)
    if word:
        word_keyboard = [
            [
                InlineKeyboardButton(
                    "✅ Known", callback_data=f"known-{word.id}-{user.id}-1"),
                InlineKeyboardButton(
                    "♻️ Learn", callback_data=f"learn-{word.id}-{user.id}-2"),
            ],

        ]

        word_keyboard_markup = InlineKeyboardMarkup(word_keyboard)
        query.edit_message_text(
            text=f"{word.word}", reply_markup=word_keyboard_markup)
    else:
        query.edit_message_text(text="No words")


def review_words(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()
    user = get_user_data(query.from_user.id)
    word = get_user_review_word(user.id)

    if word:

        word_keyboard = [
            [
                InlineKeyboardButton(
                    "✅ Known", callback_data=f"review_known-{word.id}-{user.id}-1"),
                InlineKeyboardButton(
                    "♻️ Learn", callback_data=f"review_learn-{word.id}-{user.id}-2"),
            ],

        ]

        word_keyboard_markup = InlineKeyboardMarkup(word_keyboard)

        query.edit_message_text(
            text=f"{word.word}", reply_markup=word_keyboard_markup)
    else:
        query.edit_message_text(text="No words")


def review_update_words(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data.split('-')
    query.answer()
    if len(data) > 3:
        users_words_update(data[2], data[1], data[3])
    user = get_user_data(query.from_user.id)
    word = get_user_word(user.id)
    print(word)
    if word:
        word_keyboard = [
            [
                InlineKeyboardButton(
                    "✅ Known", callback_data=f"review_known-{word.id}-{user.id}-1"),
                InlineKeyboardButton(
                    "♻️ Learn", callback_data=f"review_learn-{word.id}-{user.id}-2"),
            ],

        ]

        word_keyboard_markup = InlineKeyboardMarkup(word_keyboard)
        query.edit_message_text(
            text=f"{word.word}", reply_markup=word_keyboard_markup)
    else:
        query.edit_message_text(text="No words")
