import os


def save_files(message, file_info, downloaded_file):
    save_file_path = "{0}/{1}/{2}".format("photos", message.from_user.id, file_info.file_path.split("/")[-1])
    dir_path = "/".join(save_file_path.split("/")[:-1])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(save_file_path, "wb") as new_file:
        new_file.write(downloaded_file)
    return save_file_path
