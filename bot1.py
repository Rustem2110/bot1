import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot("5367281045:AAF1ey6jhKHXKrvrIgvrAuXuYeyKBPFiEt0")
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Сам " + message.text)

bot.infinity_polling()
