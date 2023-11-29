import telebot

bot = telebot.TeleBot('6883159841:AAEPM-J9Tp_76GFeX6KHBUO_KJuvSn-wJL0')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Приветствую Вас', parse_mode='Markdown')


@bot.message_handler(commands=['go'])
def main(message):
    bot.send_message(message.chat.id, '*Куда-то собрались?* \nОстаньтесь', parse_mode='Markdown')


@bot.message_handler(commands=['find'])
def main(message):
    bot.send_message(message.chat.id, '[Поиск](https://ya.ru/)', parse_mode='Markdown')


@bot.message_handler(commands=['image'])
def main(message):
    bot.send_message(message.chat.id, '[Изображение](https://ya.ru/images/search?from=tabbar&text=image)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['music'])
def main(message):
    bot.send_message(message.chat.id, 'Послушать не получится', parse_mode='Markdown')


@bot.message_handler(commands=['bye'])
def main(message):
    bot.send_message(message.chat.id, '*До свидания*', parse_mode='Markdown')


bot.infinity_polling()
