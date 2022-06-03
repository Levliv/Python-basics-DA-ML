import telebot
import os
from types import *
from image_pocessing import image_colorize
from file_saver import save_files

secret_key = ""
with open("secrets.txt") as file:
    secret_key = file.readline()
bot = telebot.TeleBot(secret_key)


@bot.message_handler(commands=["start", "help"])
def start_help(message):
    bot.reply_to(
        message,
        "Привет, {0}!\nОтправьте фотографию (.jpg), а я её раскрашу.\nЕсли нужна помощь, отправьте /help.\n"
        "Чтобы получить результат преобразования, отправьте /results".format(message.from_user.first_name),
    )


@bot.message_handler(commands=["results"])
def get_results(message):
    user_id = message.from_user.id
    dir_path = "/".join(["photos", "colored_" + str(user_id)])
    if not len(os.listdir(dir_path)):
        bot.reply_to(message, "Вы уже скачали все фоторгафии \U000026C4.\nЗагружайте еще!")
    else:
        user_colored_photos = os.listdir(dir_path)
        for photo in user_colored_photos:
            photo_path = "/".join([dir_path, photo])
            with open(photo_path, "rb") as photo_file:
                bot.send_photo(user_id, photo_file)
            os.remove(photo_path)
        bot.reply_to(message, "После получения результата ваши фотографии будут удалены и сохранятся только у вас.")


@bot.message_handler(content_types=["photo"])
def handle_text(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_file_path = save_files(message, file_info, downloaded_file)
    bot.reply_to(message, "Фото добавлено.\nВам придет уведомление, когда фотография будет обработана.")
    image_colorize(save_file_path)
    bot.reply_to(message, "Чтобы получить раскрашеную фотографию используйте /results.")
    os.remove(save_file_path)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Я еще не знаю такую команду, отправьте /help чтобы получить справку по использованию")


bot.infinity_polling()
