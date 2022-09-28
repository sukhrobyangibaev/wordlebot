from constants import ENG, RUS, GREET, ESP, CHOOSE_LANG, NATIVE_LANG, CHOOSE_GAME_LANG, NUMBER_OF_LETTERS, \
    DEF_NOT_FOUND, WRONG_LENGTH, WRONG_WORD, WON, LOST, READY, YES, PROCESS, ROW_1, ROW_2, ROW_3, HELP, \
    CHOOSE_HELP_LANG, START

LANG = {
    ENG: {
        GREET: 'Hello!',
        CHOOSE_LANG: 'Please select your native language.',
        NATIVE_LANG: 'English',
        ENG: 'English',
        RUS: 'Russian',
        ESP: 'Spanish',
        CHOOSE_GAME_LANG: 'Please select the language of the words.',
        CHOOSE_HELP_LANG: 'Please select the help language.',
        NUMBER_OF_LETTERS: 'Please select the number of letters in the word.',
        DEF_NOT_FOUND: '(definition not found 🤔)',
        WRONG_LENGTH: 'The word must be {} letters long.',
        WRONG_WORD: 'Such a word does not exist in our dictionary. 😔',
        WON: '<pre>{}</pre>\n\nYou won! 🎉\n<b>{}</b> - {}',
        LOST: 'Sorry... 😔\n<b>{}</b> - {}',
        READY: 'Are you ready for next round?',
        YES: 'YES!',
        PROCESS: '<pre>{}</pre>\nfound letters: <b><u>{}</u></b>\nwrong letters: <b><s>{}</s></b>'
                 '\nattempts remaining: <b>{}</b>\n<pre>{}</pre>',
        ROW_1: ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ROW_2: ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ROW_3: ['Z', 'C', 'V', 'B', 'N', 'M'],
        HELP: (
            'Hi! 👋 This is a word game. 🕹\n'
            'You have to guess a word with a certain number of letters. 🔤\n'
            'You are given 6️⃣ tries.\n'
            'First you need to select your native language (this will be the language of the interface). ✅\n'
            'Then you need to choose the language of the words to guess. ✅\n'
            'After that choose the number of letters in the word. ✅\n'
            '⬜ - means that this letter is not present in the word. \n'
            '🟧 - means that this letter is present in the word, but in a different position. \n'
            '🟩 - means that you guessed both the letter and the position in the word. \n'
            'Press /start to start'
        ),
        START: 'Let\'s go! try to write any word.'
    },
    RUS: {
        GREET: 'Привет!',
        CHOOSE_LANG: 'Пожалуйста, выберите свой родной язык.',
        NATIVE_LANG: 'Русский',
        ENG: 'Английский',
        RUS: 'Русский',
        ESP: 'Испанский',
        CHOOSE_GAME_LANG: 'Пожалуйста, выберите язык слов.',
        CHOOSE_HELP_LANG: 'Пожалуйста, выберите язык справки.',
        NUMBER_OF_LETTERS: 'Пожалуйста, выберите количество букв в слове.',
        DEF_NOT_FOUND: '(определение не найдено 🤔)',
        WRONG_LENGTH: 'Слово должно состоять из {} букв.',
        WRONG_WORD: 'Такого слова не существует в нашем словаре. 😔',
        WON: '<pre>{}</pre>\n\nВы победили! 🎉\n<b>{}</b> - {}',
        LOST: 'Жаль... 😔\n<b>{}</b> - {}',
        READY: 'Вы готовы к следующему раунду?',
        YES: 'ДА!',
        PROCESS: '<pre>{}</pre>\nнайденные буквы: <b><u>{}</u></b>\nнеправильные буквы: <b><s>{}</s></b>'
                 '\nосталось попыток: <b>{}</b>\n<pre>{}</pre>',
        ROW_1: ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ'],
        ROW_2: ['Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э'],
        ROW_3: ['Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю'],
        HELP: (
            'Привет! 👋 Это игра слов. 🕹\n'
            'Вам нужно угадать слово с определённым количеством букв. 🔤\n'
            'Вам дается 6️⃣ попыток.\n'
            'Сначала вам нужно выбрать родной язык(это будет язык интрфейса). ✅\n'
            'Затем вам нужно выбрать язык слов для отгадывания. ✅\n'
            'После этого выбрать количество букв в слове. ✅\n'
            '⬜ - означает, что этой буквы нету в слове. \n'
            '🟧 - означает, что эта буква присутствует в слове, но в другой позиции. \n'
            '🟩 - означает, что вы угадали и букву и позицию в слове. \n'
            'Нажмите /start чтобы начать'
        ),
        START: 'Поехали! Попробуй написать любое слово.'
    },
    ESP: {
        GREET: 'Oye!',
        CHOOSE_LANG: 'Por favor elige tu idioma nativo.',
        NATIVE_LANG: 'Español',
        ENG: 'Inglés',
        RUS: 'Ruso',
        ESP: 'Español',
        CHOOSE_GAME_LANG: 'Por favor seleccione el idioma de las palabras.',
        CHOOSE_HELP_LANG: 'Seleccione un idioma de ayuda.',
        NUMBER_OF_LETTERS: 'Por favor seleccione el número de letras en la palabra.',
        DEF_NOT_FOUND: '(definición no encontrada 🤔)',
        WRONG_LENGTH: 'La palabra debe tener {} letras de largo.',
        WRONG_WORD: 'Esta palabra no existe en nuestro diccionario. 😔',
        WON: '<pre>{}</pre>\n\n¡Ganaste! 🎉\n<b>{}</b> - {}',
        LOST: 'Es una pena... 😔\n<b>{}</b> - {}',
        READY: '¿Estás lista para la próxima ronda?',
        YES: '¡SÍ!',
        PROCESS: '<pre>{}</pre>\ncartas encontradas: <b><u>{}</u></b>\nletras equivocadas: <b><s>{}</s></b>'
                 '\nintentos restantes: <b>{}</b>\n<pre>{}</pre>',
        ROW_1: ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ROW_2: ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ROW_3: ['Z', 'C', 'V', 'B', 'N', 'M'],
        HELP: (
            '¡Hola! 👋 Esto es un juego de palabras. 🕹\n'
            'Tienes que adivinar una palabra con un cierto número de letras. 🔤\n'
            'Tienes 6️⃣ intentos.\n'
            'Primero debe seleccionar su idioma nativo (este será el idioma de la interfaz). ✅\n'
            'Entonces debes elegir el idioma de las palabras para adivinar. ✅\n'
            'Después de eso, elija el número de letras en la palabra. ✅\n'
            '⬜ - significa que esta letra no está presente en la palabra. \norte'
            '🟧 - significa que esta letra está presente en la palabra, pero en una posición diferente. \norte'
            '🟩 - significa que adivinaste tanto la letra como la posición en la palabra. \norte'
            'Presione /start para comenzar'
        ),
        START: '¡Empezado! Intenta escribir cualquier palabra.'
    }
}
