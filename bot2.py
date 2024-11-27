import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from text import library_descriptions, full_info_library


bot = telebot.TeleBot("7860026666:AAHNNIkLieuOnbhf5pkfIxmtgb10XNlje2M")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, я телеграм-бот, який допоможе тобі дізнатися про бібліотеки в Python.")
    bot.send_message(message.chat.id, "Список бібліотек про які я можу розповісти:")

    keyboard = InlineKeyboardMarkup(row_width=3)
    button = [InlineKeyboardButton(library.capitalize(), callback_data=library) for library in library_descriptions.keys()]
    keyboard.add(*button)

    bot.send_message(message.chat.id, "Виберіть бібліотеку:", reply_markup=keyboard)


@bot.callback_query_handler()
def library_info(call):
    library_name = call.data.lower()
    description = library_descriptions.get(library_name)
    if description:
        bot.send_message(call.message.chat.id, description)
        link = full_info_library.get(library_name)
        if link:
            bot.send_message(call.message.chat.id,"Перейшовши за цим посиланням, ти можеш детальніше дізнатися про потрібну тобі бібліотеку:")
            bot.send_message(call.message.chat.id, link)
    else:
        bot.send_message(call.message.chat.id, "Вибач, я не маю інформації про цю бібліотеку.")


bot.polling()
