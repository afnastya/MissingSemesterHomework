import telebot

TELEGRAM_TOKEN = input()
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(content_types=["text"])
def echo_messages(message):
    if message.from_user.username != "afnastya":
        return
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)