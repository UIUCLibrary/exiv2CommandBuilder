import configparser
import shutil


def get_exiv2_path():
    config = configparser.ConfigParser()
    config.read("settings/exvsettings.ini")
    return config['commands'].get('exiv2', shutil.which("exiv2"))


# try:
# except KeyError:
#     EXIV2_PATH = shutil.which("exiv2")
