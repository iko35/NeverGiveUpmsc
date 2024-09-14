import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 25558996))
API_HASH = getenv("API_HASH", "375b1fe4641b07a60fa4029779ec56ce")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7375051921:AAEYwtNmn-CWjz-3KEkf71wY4xV4SwshXAA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mongoguess:guessmongo@cluster0.zcwklzz.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002346354678))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7447793956))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/K4RACA123/ayut",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/telesatisbayisi")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/zumresohbett")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", True)

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAGF_9QAE-voniMwwVUdsYdBHdbHLZdibUc5pTwnBrfy1dBJRJMmt7JmkcdFngPJtoP0QNt1u8omU-9zZCaHFYl2eByy_LsY5I38I6Yeh3O80x9lgO2ujkRtk25P0n6GY-0QfM8RFs-B0Kooos3fFbP0RMFdrXv4W85nVh27wCVvw2T3JadUBKmPz9T9zmpy4CQLjILeyLXRBqRIk0Dkgadb-TlySjhkRfqd2uL0Eeu7kz-8tXcECZPUpUUR-PwnBTHdhuSJfW7re0ESw8Cu5JSJ7nbe0s95a7L772Vd0f_SR954eI_tlE_KVfcDiy4UNCuHMbL52T4Tn6xVc_KrOVR7BORW-QAAAAGy38KnAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/e4014459d88c8e97ca100.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
STATS_IMG_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/b04e25befdccdfbd77e11.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
