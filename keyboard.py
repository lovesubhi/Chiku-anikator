from strings import Chiku_LANG_CODE, DEV_URL, GITHUB_URL
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

START_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('--Github--', GITHUB_URL),
            InlineKeyboardButton('--ᴏᴡɴᴇʀ--', DEV_URL)   
        ]
    ]
)

#Shows a bunch of buttons to change the language of the akinator when playing.
Chiku_LANG_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(Chiku_LANG_CODE['en'], callback_data='Chiku_set_lang_en'),
            InlineKeyboardButton(Chiku_LANG_CODE['ar'], callback_data='Chiku_set_lang_ar'),
            InlineKeyboardButton(Chiku_LANG_CODE['cn'], callback_data='Chiku_set_lang_cn'),
            InlineKeyboardButton(Chiku_LANG_CODE['de'], callback_data='Chiku_set_lang_de')
         ],
         [
            InlineKeyboardButton(Chiku_LANG_CODE['es'], callback_data='Chiku_set_lang_es'),
            InlineKeyboardButton(Chiku_LANG_CODE['fr'], callback_data='Chiku_set_lang_fr'),
            InlineKeyboardButton(Chiku_LANG_CODE['il'], callback_data='Chiku_set_lang_il'),
            InlineKeyboardButton(Chiku_LANG_CODE['it'], callback_data='Chiku_set_lang_it')
         ],
         [
            InlineKeyboardButton(Chiku_LANG_CODE['jp'], callback_data='Chiku_set_lang_jp'),
            InlineKeyboardButton(Chiku_LANG_CODE['kr'], callback_data='Chiku_set_lang_kr'),
            InlineKeyboardButton(Chiku_LANG_CODE['nl'], callback_data='Chiku_set_lang_nl'),
            InlineKeyboardButton(Chiku_LANG_CODE['pl'], callback_data='Chiku_set_lang_pl')
         ],
         [
            InlineKeyboardButton(Chiku_LANG_CODE['pt'], callback_data='Chiku_set_lang_p'),
            InlineKeyboardButton(Chiku_LANG_CODE['ru'], callback_data='Chiku_set_lang_ru'),
            InlineKeyboardButton(Chiku_LANG_CODE['tr'], callback_data='Chiku_set_lang_tr'),
            InlineKeyboardButton(Chiku_LANG_CODE['id'], callback_data='Chiku_set_lang_id')
         ],

    ]
)

#Child Mode enable/disable Buttons
CHILDMODE_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Enable", callback_data='c_mode_1'),
            InlineKeyboardButton("Disable", callback_data='c_mode_0')
        ]
    ]
)


Chiku_PLAY_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Yes", callback_data='Chiku_play_0'),
            InlineKeyboardButton("No", callback_data='Chiku_play_1'),
            InlineKeyboardButton("Probably", callback_data='Chiku_play_3')
        ],
        [
            InlineKeyboardButton("I don't know", callback_data='Chiku_play_2'),
            InlineKeyboardButton("Probably Not", callback_data='Chiku_play_4')
        ],
        [   InlineKeyboardButton("Back", callback_data= 'Chiku_play_5')
        ]
    ]
)

Chiku_WIN_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Yes", callback_data='Chiku_win_y'),
            InlineKeyboardButton("No", callback_data='Chiku_win_n'),
        ]
    ]
)


Chiku_LEADERBOARD_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Total Guesses", callback_data='Chiku_lead_tguess'),
            InlineKeyboardButton("Correct Guesses", callback_data='Chiku_lead_cguess'),
        ],
        [
            InlineKeyboardButton("Wrong Guesses", callback_data='Chiku_lead_wguess'),
            InlineKeyboardButton("Total Questions", callback_data='Chiku_lead_tquestions'),
        ]
    ]
)