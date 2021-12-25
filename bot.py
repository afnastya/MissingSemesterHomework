import os
import random
import telebot
from telebot import types

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

memes_number = len(os.listdir('memes'))



@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(
        message.chat.id,
        "Hi there! Click the button below!",
        reply_markup=meme_markup())


@bot.message_handler(func=lambda msg: msg.text == "Get Meme", content_types=["text"])
def send_meme(message):
    meme_id = random.randint(1, memes_number)
    with open(f'memes/meme{meme_id}.jpg', 'rb') as meme:
        bot.send_photo(
            message.chat.id,
            meme,
            reply_markup=meme_markup())


def meme_markup():
    return types.ReplyKeyboardMarkup().row(types.KeyboardButton("Get Meme"))


bot.polling(none_stop=True)
