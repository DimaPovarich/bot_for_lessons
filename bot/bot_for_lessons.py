import telebot

bot = telebot.TeleBot('6841761218:AAGt3gwtJGMsZzWd2NS1g-j_EqEnp4eEfqg')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для отслеживания активности ученика в группе на паре, чтобы узнать что я могу напиши /help')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/start_search - начать отслеживание активности участников группы \n/active - показать активность участников группы с момента последней отправки /start_search\n')


bot.polling(none_stop=True)