import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("6102078578:AAHHOgYpKduh_OFRtzh5yLBOKa1KrDVqXg0", "")
    # The Telegram API things
    API_ID = int(os.environ.get("5806640", 12345))
    API_HASH = os.environ.get("127f130ad3745dbcd31aa39aa0eabcb8")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("1375408229", ""))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("mongodb+srv://bossboltebro:<password>@cluster0.jrzdzmy.mongodb.net/?retryWrites=true&w=majority", "")
    MAX_RESULTS = "50"
