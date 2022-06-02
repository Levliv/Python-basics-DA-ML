import telebot
import os
from types import *
from image_pocessing import image_colorize


bot = telebot.TeleBot("5532763302:AAH0Ovnsc0rT2F5EPbHZKd6qPS_-6FVePsg")


@bot.message_handler(commands=["start", "help"])
def start_help(message):
    bot.reply_to(
        message,
        "Привет, {0}!\nОтправьте фотографию (.jpg), а я её раскрашу.\nЕсли нужна помощь, отправьте /help.\n"
        "Чтобы получить результат преобразования, отправьте /results".format(
            message.from_user.first_name
        ),
    )


@bot.message_handler(commands=["results"])
def get_results(message):
    user_id = message.from_user.id
    dir_path = '/'.join(['photos', 'colored_' + str(user_id)])
    user_colored_photos = os.listdir(dir_path)
    for photo in user_colored_photos:
        photo_path = '/'.join([dir_path, photo])
        with open(photo_path, 'rb') as file:
            bot.send_photo(user_id, file)
        os.remove(photo_path)
    bot.reply_to(message, 'После получения результата ваши фотографии будут удалены и храниться только у вас.')


@bot.message_handler(content_types=["photo"])
def handle_text(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_file_path = "{0}/{1}/{2}".format("photos", message.from_user.id, file_info.file_path.split("/")[-1])
    dir_path = "/".join(save_file_path.split("/")[:-1])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(save_file_path, "wb") as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "Фото добавлено.\nЧтобы получить раскрашенную фотографию используйте /results")
    image_colorize(save_file_path)
    os.remove(save_file_path)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Я еще не знаю такую команду, отправьте /help чтобы получить справку по использованию")


bot.infinity_polling()
