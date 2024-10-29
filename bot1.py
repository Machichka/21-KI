import telebot
from mY_tok import key
from text import library_descriptions
from text import full_info_library
bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, я телеграм-бот, який допоможе тобі дізнатися про бібліотеки в Python.")
    bot.send_message(message.chat.id, "Напиши назву бібліотеки, яка тебе цікавить, і я розкажу тобі про неї.")

@bot.message_handler()
def library(message):
    library_name = message.text.lower()
    description = library_descriptions.get(library_name)
    if description:
        bot.send_message(message.chat.id, description)
        link = full_info_library.get(library_name)
        if link:
            bot.send_message(message.chat.id,"Перейшовши за цим посиланням, ти можеш детальніше дізнатися про потрібну тобі бібліотеку:")
            bot.send_message(message.chat.id, link)
    else:
        bot.send_message(message.chat.id, "Вибач, я не маю інформації про цю бібліотеку.")

bot.polling()

