import telebot
bot = telebot.TeleBot("7860026666:AAHNNIkLieuOnbhf5pkfIxmtgb10XNlje2M")


bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
