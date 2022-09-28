import json

from constants import *


def init_dictionary() -> None:
    if 'wordlebot' not in client.list_database_names():
        if 'words' not in database.list_collection_names():
            with open('files/eng.json') as dictionary_file:
                # words_counter = 0
                four_letter_words_counter = 0
                five_letter_words_counter = 0
                six_letter_words_counter = 0
                dictionary = json.load(dictionary_file)
                for key, value in dictionary.items():
                    # words_counter += 1
                    # eng_words_col.insert_one({'rnd': words_counter, 'word': key})
                    if len(key) == 4:
                        four_letter_words_counter += 1
                        eng_four_letter_words_col.insert_one(
                            {'rnd': four_letter_words_counter, 'word': key.upper()})
                    elif len(key) == 5:
                        five_letter_words_counter += 1
                        eng_five_letter_words_col.insert_one(
                            {'rnd': five_letter_words_counter, 'word': key.upper()})
                    elif len(key) == 6:
                        six_letter_words_counter += 1
                        eng_six_letter_words_col.insert_one(
                            {'rnd': six_letter_words_counter, 'word': key.upper()})
                logger.info('added {} en 4 letter words'.format(four_letter_words_counter))
                logger.info('added {} en 5 letter words'.format(five_letter_words_counter))
                logger.info('added {} en 6 letter words'.format(six_letter_words_counter))

            with open('files/rus.json', encoding='utf-8') as dictionary_file:
                # words_counter = 0
                four_letter_words_counter = 0
                five_letter_words_counter = 0
                six_letter_words_counter = 0
                dictionary = json.load(dictionary_file)
                for word in dictionary:
                    # words_counter += 1
                    # rus_words_col.insert_one({'rnd': words_counter, 'word': word.upper()})
                    if len(word) == 4:
                        four_letter_words_counter += 1
                        rus_four_letter_words_col.insert_one(
                            {'rnd': four_letter_words_counter, 'word': word.upper()})
                    elif len(word) == 5:
                        five_letter_words_counter += 1
                        rus_five_letter_words_col.insert_one(
                            {'rnd': five_letter_words_counter, 'word': word.upper()})
                    elif len(word) == 6:
                        six_letter_words_counter += 1
                        rus_six_letter_words_col.insert_one(
                            {'rnd': six_letter_words_counter, 'word': word.upper()})

                # logger.info('added {} words'.format(words_counter))
                logger.info('added {} ru 4 letter words'.format(four_letter_words_counter))
                logger.info('added {} ru 5 letter words'.format(five_letter_words_counter))
                logger.info('added {} ru 6 letter words'.format(six_letter_words_counter))

            with open('files/esp.json', encoding='utf-8') as dictionary_file:
                # words_counter = 0
                four_letter_words_counter = 0
                five_letter_words_counter = 0
                six_letter_words_counter = 0
                dictionary = json.load(dictionary_file)
                for word in dictionary:
                    # words_counter += 1
                    # esp_words_col.insert_one({'rnd': words_counter, 'word': word.upper()})
                    if len(word) == 4:
                        four_letter_words_counter += 1
                        esp_four_letter_words_col.insert_one(
                            {'rnd': four_letter_words_counter, 'word': word.upper()})
                    elif len(word) == 5:
                        five_letter_words_counter += 1
                        esp_five_letter_words_col.insert_one(
                            {'rnd': five_letter_words_counter, 'word': word.upper()})
                    elif len(word) == 6:
                        six_letter_words_counter += 1
                        esp_six_letter_words_col.insert_one(
                            {'rnd': six_letter_words_counter, 'word': word.upper()})

                # logger.info('added {} words'.format(words_counter))
                logger.info('added {} es 4 letter words'.format(four_letter_words_counter))
                logger.info('added {} es 5 letter words'.format(five_letter_words_counter))
                logger.info('added {} es 6 letter words'.format(six_letter_words_counter))
    else:
        logger.info('database already exists')
