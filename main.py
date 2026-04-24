import telebot

TOKEN = "8350010692:AAEowYxkV9Pbgi3wqicXQeiXMCGIiBcBG7s"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands= )
def send_welcome(message):
    bot.reply_to(message, "✅ بوت النشر شغال!\nسيبدأ النشر تلقائياً.")

print("✅ البوت شغال بنجاح...")
bot.infinity_polling()
