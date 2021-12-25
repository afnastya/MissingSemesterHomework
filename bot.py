import os
import telebot

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# def echo_messages(message):
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=["text"])
def send_meme(message):
    bot.send_photo(message.char.id, "memes/meme1.jpg")

bot.polling(none_stop=True)
