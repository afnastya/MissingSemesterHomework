import os
import telebot
import random

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

memes_number = len(os.listdir('memes/'))

@bot.message_handler(content_types=["text"])
def send_meme(message):
    meme_id = random.randint(1, memes_number)
    bot.send_photo(message.chat.id, open('memes/meme{0}.jpg'.format(meme_id), 'rb'))

bot.polling(none_stop=True)
