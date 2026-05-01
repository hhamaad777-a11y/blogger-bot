import telebot
import os

TOKEN = "8350010692:AAEowYxkV9Pbgi3wqicXQeiXMCGIiBcBG7s"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands= )
def send_welcome(message):
    bot.reply_to(message, "✅ البوت شغال بنجاح!\nأرسل أي رسالة للتجربة.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "تم الاستلام: " + message.text)

print("✅ البوت شغال بنجاح...")
bot.infinity_polling()