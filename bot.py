import os
import random
import telebot

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

memes_number = len(os.listdir('memes/'))

@bot.message_handler(content_types=["text"])
def send_meme(message):
    meme_id = random.randint(1, memes_number)
    with open(f'memes/meme{meme_id}.jpg', 'rb') as meme:
        bot.send_photo(message.chat.id, meme)

bot.polling(none_stop=True)
