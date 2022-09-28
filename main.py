import html
import json
import traceback

from telegram.constants import ParseMode

from constants import *
from db_init import init_dictionary
from helpers import get_random_word, check_word, get_wiki
from languages import LANG

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info('/start message from user with id {}'.format(update.effective_user.id))
    if FIRST_START not in context.user_data:
        context.user_data[FIRST_START] = True
        user = update.effective_user
        chat = update.effective_chat

        if not users_col.find_one({'id': user.id}):
            users_col.insert_one(user.to_dict())
            logger.info('added new user {}'.format(user))

        if not chats_col.find_one({'id': chat.id}):
            chats_col.insert_one(chat.to_dict())
            logger.info('added new chat {}'.format(chat))

        context.user_data[USER_ID] = user.id
        context.user_data[FIRST_START] = False

        text = '{} 👋 {} 👋 {}'.format(LANG[ENG][GREET], LANG[RUS][GREET], LANG[ESP][GREET])
        await update.message.reply_text(text)

    return await choose_native_lang(update, context)


async def choose_native_lang(update: Update, _) -> int:
    languages = [[LANG[ENG][NATIVE_LANG]],
                 [LANG[RUS][NATIVE_LANG]],
                 [LANG[ESP][NATIVE_LANG]]]
    keyboard = ReplyKeyboardMarkup(languages, one_time_keyboard=True)
    text = '{}\n{}\n{}'.format(LANG[ENG][CHOOSE_LANG], LANG[RUS][CHOOSE_LANG], LANG[ESP][CHOOSE_LANG])
    await update.message.reply_text(text, reply_markup=keyboard)

    return CHOOSE_NATIVE_LANG


async def handle_choose_native_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = update.message.text
    logger.info('user with id {} chose {} native language'.format(update.effective_user.id, lang))
    context.user_data[USER_NATIVE_LANG] = lang_code[lang]

    return await choose_lang(update, context)


async def choose_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    languages = [[LANG[context.user_data[USER_NATIVE_LANG]][ENG]],
                 [LANG[context.user_data[USER_NATIVE_LANG]][RUS]],
                 [LANG[context.user_data[USER_NATIVE_LANG]][ESP]]]
    keyboard = ReplyKeyboardMarkup(languages, one_time_keyboard=True)
    text = LANG[context.user_data[USER_NATIVE_LANG]][CHOOSE_GAME_LANG]
    await update.message.reply_text(text, reply_markup=keyboard)

    return CHOOSE_LANG


async def handle_choose_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = update.message.text
    logger.info('user with id {} chose {} language'.format(update.effective_user.id, lang))
    context.user_data[GAME_LANG] = lang_code[lang]

    return await choose_number_of_letters(update, context)


async def choose_number_of_letters(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    numbers = [['4', '5', '6']]
    keyboard = ReplyKeyboardMarkup(numbers, one_time_keyboard=True)
    text = LANG[context.user_data[USER_NATIVE_LANG]][NUMBER_OF_LETTERS]
    await update.message.reply_text(text, reply_markup=keyboard)

    return CHOOSE_NUMBER


async def handle_choose_number_of_letters(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    number_of_letters = update.message.text
    logger.info('user with id {} chose {} letters in word'.format(update.effective_user.id, number_of_letters))
    context.user_data[WORD_LENGTH] = int(number_of_letters)

    return await get_new_word(update, context)


async def get_new_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data[GAME_LANG]
    length = context.user_data[WORD_LENGTH]
    random_word = get_random_word(lang, length)

    context.user_data[GUESS_WORD] = random_word.get('word')
    context.user_data[FOUND_LETTERS] = []
    context.user_data[WRONG_LETTERS] = []
    context.user_data[TILES] = ''
    context.user_data[KEYBOARD] = '{}\n {}\n    {}'.format(' '.join(LANG[context.user_data[GAME_LANG]][ROW_1]),
                                                           ' '.join(LANG[context.user_data[GAME_LANG]][ROW_2]),
                                                           ' '.join(LANG[context.user_data[GAME_LANG]][ROW_3]))
    context.user_data[ATTEMPTS] = DEFAULT_ATTEMPTS
    text = '{}\n\n<pre>{}</pre>'.format(LANG[context.user_data[USER_NATIVE_LANG]][START], ' '.join('⬜' * length))

    context.user_data[GUESS_WORD_DEF] = get_wiki(random_word.get('word'), context.user_data[GAME_LANG],
                                                 context.user_data[USER_NATIVE_LANG])

    await update.message.reply_text(text=text, parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove())
    return GUESS_WORD


async def guess_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    given_answer = update.message.text.upper()
    logger.info('user with id {} send word {}'.format(update.effective_user.id, given_answer))
    guessing_word = str(context.user_data[GUESS_WORD])

    if len(given_answer) != context.user_data[WORD_LENGTH]:
        await update.message.reply_text(
            LANG[context.user_data[USER_NATIVE_LANG]][WRONG_LENGTH].format(context.user_data[WORD_LENGTH]))
        return GUESS_WORD

    if not check_word(given_answer, context.user_data[GAME_LANG], context.user_data[WORD_LENGTH]):
        await update.message.reply_text(LANG[context.user_data[USER_NATIVE_LANG]][WRONG_WORD])
        return GUESS_WORD

    context.user_data[ATTEMPTS] -= 1
    for i, letter in enumerate(given_answer):
        if i != 0:
            context.user_data[TILES] += ' '
        context.user_data[TILES] += letter
        if letter in guessing_word:
            if letter not in context.user_data[FOUND_LETTERS]:
                context.user_data[FOUND_LETTERS].append(letter)
            if i == guessing_word.find(letter):
                context.user_data[TILES] += '🟩'
            elif i == guessing_word.rfind(letter):
                context.user_data[TILES] += '🟩'
            else:
                context.user_data[TILES] += '🟧'
        else:
            context.user_data[TILES] += '⬜'
            context.user_data[KEYBOARD] = context.user_data[KEYBOARD].replace(letter, ' ')
            if letter not in context.user_data[WRONG_LETTERS]:
                context.user_data[WRONG_LETTERS].append(letter)
    context.user_data[TILES] += '\n'

    if given_answer == guessing_word:
        await update.message.reply_text(
            LANG[context.user_data[USER_NATIVE_LANG]][WON].format(context.user_data[TILES], guessing_word,
                                                                  context.user_data[GUESS_WORD_DEF]),
            parse_mode=ParseMode.HTML)
        return await ready(update, context)

    text = LANG[context.user_data[USER_NATIVE_LANG]][PROCESS].format(
        context.user_data[TILES], ' '.join(context.user_data[FOUND_LETTERS]),
        ' '.join(context.user_data[WRONG_LETTERS]), context.user_data[ATTEMPTS], context.user_data[KEYBOARD])

    await update.message.reply_text(text=text, parse_mode=ParseMode.HTML)

    if not context.user_data[ATTEMPTS]:
        await update.message.reply_text(
            LANG[context.user_data[USER_NATIVE_LANG]][LOST].format(guessing_word,
                                                                   context.user_data[GUESS_WORD_DEF]),
            parse_mode=ParseMode.HTML)
        return await ready(update, context)

    return GUESS_WORD


async def ready(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_button = [[LANG[context.user_data[USER_NATIVE_LANG]][YES]]]
    keyboard = ReplyKeyboardMarkup(reply_button, one_time_keyboard=True)

    await update.message.reply_text(LANG[context.user_data[USER_NATIVE_LANG]][READY], reply_markup=keyboard)
    return READY


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f"An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )

    await context.bot.send_message(
        chat_id=DEVELOPER_CHAT_ID, text=message[0:4090], parse_mode=ParseMode.HTML
    )


async def admin_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if str(update.effective_chat.id) == str(DEVELOPER_CHAT_ID):
        await update.message.reply_text('Please write admin message:')
        return ADMIN_MESSAGE
    else:
        await update.message.reply_text('unknown command')
        return await start(update, context)


async def handle_admin_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    msg_to_all = update.message.text
    for chat in chats_col.find():
        await context.bot.send_message(chat_id=chat.get('id'), text=msg_to_all)

    return await start(update, context)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if HELP not in context.user_data:
        languages = [[LANG[ENG][NATIVE_LANG]],
                     [LANG[RUS][NATIVE_LANG]],
                     [LANG[ESP][NATIVE_LANG]]]
        keyboard = ReplyKeyboardMarkup(languages, one_time_keyboard=True)
        text = '{}\n{}\n{}'.format(LANG[ENG][CHOOSE_HELP_LANG], LANG[RUS][CHOOSE_HELP_LANG],
                                   LANG[ESP][CHOOSE_HELP_LANG])
        await update.message.reply_text(text, reply_markup=keyboard)
        return HELP
    else:
        await handle_help_command(update, context)


async def handle_help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if HELP not in context.user_data:
        help_lang = lang_code[update.message.text]
        context.user_data[HELP] = help_lang
    else:
        help_lang = context.user_data[HELP]
    text = LANG[help_lang][HELP]
    await update.message.reply_text(text)
    return HELP


def main() -> None:
    application = Application.builder().token("5725942411:AAHp_Vx7sm6ueTdqprhW6mFu39iEl225AZA").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSE_NATIVE_LANG: [MessageHandler(filters.Regex('^English|Русский|Español$'), handle_choose_native_lang)],
            CHOOSE_LANG: [MessageHandler(
                filters.Regex('^English|Английский|Inglés|Russian|Русский|Ruso|Spanish|Испанский|Español$'),
                handle_choose_lang)],
            CHOOSE_NUMBER: [MessageHandler(filters.Regex('^4|5|6$'), handle_choose_number_of_letters)],
            GUESS_WORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, guess_word)],
            READY: [MessageHandler(filters.Regex('^YES!|ДА!|¡SÍ!'), get_new_word)],
            ADMIN_MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_admin_message)],
            HELP: [MessageHandler(filters.Regex('^English|Русский|Español$'), handle_help_command)],
        },
        fallbacks=[
            CommandHandler('start', start),
            CommandHandler('admin', admin_message),
            CommandHandler('help', help_command)
        ]
    )
    application.add_handler(conv_handler)
    application.add_error_handler(error_handler)

    init_dictionary()
    application.run_polling()


if __name__ == "__main__":
    main()
