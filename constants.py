import logging
import pymongo

(
    FIRST_START,
    USER_ID,
    CHOOSE_LANG,
    GAME_LANG,
    CHOOSE_NUMBER,
    WORD_LENGTH,
    GUESS_WORD,
    GUESS_WORD_DEF,
    GUESSED_PART,
    FOUND_LETTERS,
    WRONG_LETTERS,
    READY,
    ATTEMPTS,
    CHOOSE_NATIVE_LANG,
    USER_NATIVE_LANG,
    GREET,
    NATIVE_LANG,
    CHOOSE_GAME_LANG,
    NUMBER_OF_LETTERS,
    DEF_NOT_FOUND,
    WRONG_LENGTH,
    WRONG_WORD,
    WON,
    LOST,
    YES,
    PROCESS,
    ROW_1,
    ROW_2,
    ROW_3,
    KEYBOARD,
    TILES,
    ADMIN_MESSAGE,
    HELP,
    CHOOSE_HELP_LANG,
    START
) = range(35)

lang_code = {
    'English': 'en',
    'Английский': 'en',
    'Inglés': 'en',
    'Russian': 'ru',
    'Русский': 'ru',
    'Ruso': 'ru',
    'Spanish': 'es',
    'Испанский': 'es',
    'Español': 'es'
}

ENG = 'en'
RUS = 'ru'
ESP = 'es'
DEFAULT_ATTEMPTS = 6
DEVELOPER_CHAT_ID = '1476403327'

logging.basicConfig(
    filename='dota_data_bot.log',
    format="[%(asctime)s > %(levelname)s > %(name)s] %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

yandex_dict_api_key = 'dict.1.1.20220926T060839Z.f2e6c2a397483a83.7a0d470472ce9344cab2d4b0b2084682798d4cbb'
client = pymongo.MongoClient('mongodb://localhost:27017/')
database = client['wordlebot']
eng_words_col = database['eng_words']
eng_four_letter_words_col = database['eng_four_letter_words']
eng_five_letter_words_col = database['eng_five_letter_words']
eng_six_letter_words_col = database['eng_six_letter_words']
rus_words_col = database['rus_words']
rus_four_letter_words_col = database['rus_four_letter_words']
rus_five_letter_words_col = database['rus_five_letter_words']
rus_six_letter_words_col = database['rus_six_letter_words']
esp_words_col = database['esp_words']
esp_four_letter_words_col = database['esp_four_letter_words']
esp_five_letter_words_col = database['esp_five_letter_words']
esp_six_letter_words_col = database['esp_six_letter_words']
users_col = database['users']
chats_col = database['chats']
