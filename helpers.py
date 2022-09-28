import random
import wikipediaapi
from constants import eng_four_letter_words_col, eng_five_letter_words_col, eng_six_letter_words_col, \
    rus_four_letter_words_col, rus_five_letter_words_col, rus_six_letter_words_col, esp_four_letter_words_col, \
    esp_five_letter_words_col, esp_six_letter_words_col, logger, DEF_NOT_FOUND
from languages import LANG


def get_random_word(lang, length):
    random_word = ''
    if lang == 'en':
        if length == 4:
            rand = random.randrange(1, eng_four_letter_words_col.count_documents({}))
            random_word = eng_four_letter_words_col.find_one({'rnd': rand})
        elif length == 5:
            rand = random.randrange(1, eng_five_letter_words_col.count_documents({}))
            random_word = eng_five_letter_words_col.find_one({'rnd': rand})
        elif length == 6:
            rand = random.randrange(1, eng_six_letter_words_col.count_documents({}))
            random_word = eng_six_letter_words_col.find_one({'rnd': rand})
    elif lang == 'ru':
        if length == 4:
            rand = random.randrange(1, rus_four_letter_words_col.count_documents({}))
            random_word = rus_four_letter_words_col.find_one({'rnd': rand})
        elif length == 5:
            rand = random.randrange(1, rus_five_letter_words_col.count_documents({}))
            random_word = rus_five_letter_words_col.find_one({'rnd': rand})
        elif length == 6:
            rand = random.randrange(1, rus_six_letter_words_col.count_documents({}))
            random_word = rus_six_letter_words_col.find_one({'rnd': rand})
    elif lang == 'es':
        if length == 4:
            rand = random.randrange(1, esp_four_letter_words_col.count_documents({}))
            random_word = esp_four_letter_words_col.find_one({'rnd': rand})
        elif length == 5:
            rand = random.randrange(1, esp_five_letter_words_col.count_documents({}))
            random_word = esp_five_letter_words_col.find_one({'rnd': rand})
        elif length == 6:
            rand = random.randrange(1, esp_six_letter_words_col.count_documents({}))
            random_word = esp_six_letter_words_col.find_one({'rnd': rand})

    logger.info('generated random {} letters {} word - {}'.format(length, lang, dict(random_word)['word']))
    return random_word


def check_word(word, lang, length):
    found = False
    if lang == 'en':
        if length == 4:
            found = eng_four_letter_words_col.find_one({'word': word})
        elif length == 5:
            found = eng_five_letter_words_col.find_one({'word': word})
        elif length == 6:
            found = eng_six_letter_words_col.find_one({'word': word})
    elif lang == 'ru':
        if length == 4:
            found = rus_four_letter_words_col.find_one({'word': word})
        elif length == 5:
            found = rus_five_letter_words_col.find_one({'word': word})
        elif length == 6:
            found = rus_six_letter_words_col.find_one({'word': word})
    elif lang == 'es':
        if length == 4:
            found = esp_four_letter_words_col.find_one({'word': word})
        elif length == 5:
            found = esp_five_letter_words_col.find_one({'word': word})
        elif length == 6:
            found = esp_six_letter_words_col.find_one({'word': word})
    return True if found else False


def get_wiki(word, trans_from, trans_to) -> str:
    wiki = wikipediaapi.Wikipedia(trans_from)
    page = wiki.page(word.lower())
    if page.exists():
        url = f'<a href="{page.fullurl}">🔗</a>'
        text = page.summary[0:300] + '...' + url
    else:
        text = LANG[trans_to][DEF_NOT_FOUND]

    return text
