# inline keyboard
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

NEW_WORDS_KEY = "new_words"
REVIEW_KEY = "review_words"
SETTINGS_KEY = "settings"
RESET_KEY = "reset"
BACK_KEY = "back"
RESET_CONFIRMATION_KEY = "reset_confirmation"
RESET_DENIED_KEY = "reset_denied"
LANGUAGE_KEY = "language"
TRANSLATE_LANG_CHANGE_KEY = "change_trans_lang"
LEARNING_LANG_CHANGE_KEY = "change_learn_lang"

main_keyboard = [
    [
        InlineKeyboardButton("📚 Learning new words",
                             callback_data=NEW_WORDS_KEY),
    ],
    [InlineKeyboardButton("📖 Review words", callback_data=REVIEW_KEY)],
    [InlineKeyboardButton("⚙️ Settings", callback_data=SETTINGS_KEY)],
]

settings = [
    [InlineKeyboardButton("♻️ Reset", callback_data=RESET_KEY)],
    [InlineKeyboardButton("🌎 Languages", callback_data=LANGUAGE_KEY)],
    [InlineKeyboardButton("🔙 Back", callback_data=BACK_KEY)]
]

confirmation = [
    [InlineKeyboardButton("✅ Yes", callback_data=RESET_CONFIRMATION_KEY)],
    [InlineKeyboardButton("❌ No", callback_data=RESET_DENIED_KEY)]
]

def language_change(learn_lang, translation_lang): return [
    [
        InlineKeyboardButton('Learning language', callback_data=None),
        InlineKeyboardButton(learn_lang, callback_data=LEARNING_LANG_CHANGE_KEY)
    ],
    [
        InlineKeyboardButton('Translation language', callback_data=None),
        InlineKeyboardButton(translation_lang, callback_data=TRANSLATE_LANG_CHANGE_KEY)
    ],
    [InlineKeyboardButton("🔙 Back", callback_data=BACK_KEY)]
]

confirmation_keyboard_markup = InlineKeyboardMarkup(confirmation)
settings_keyboard_markup = InlineKeyboardMarkup(settings)
main_keyboard_markup = InlineKeyboardMarkup(main_keyboard)
