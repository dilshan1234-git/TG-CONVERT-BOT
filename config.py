import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6898599695:AAE-rukB-OoPJgxOOOcKKuK_8gv55HiC4ww")
    APP_ID = int(os.environ.get("APP_ID", 14631157))
    API_HASH = os.environ.get("API_HASH", "aa7c2b3be68a7488abdb9de6ce78d311")
    USER_NAME = os.environ.get("USER_NAME", "dilfilter")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5380833276").split())
    BANNED_USER = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    BOT_PWD = os.environ.get("BOT_PASSWORD", "")
    LOGGED_USER = []
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://dilfilter123:dilfilter123@cluster0.tq9uv2k.mongodb.net/?retryWrites=true&w=majority")
