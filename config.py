import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 27725649))
API_HASH = getenv("API_HASH", "77c887f556080a27fa405c6c6de741a5")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7843928458:AAHxPmlFSYtqXhITPZ2DLGmQLqhbaEMlM00")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mongoguess:guessmongo@cluster0.zcwklzz.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002563485663))

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
STRING1 = getenv("STRING_SESSION", "AQGpzyUAV1u24_1Xaq4wHYaXggef8389h6nNijjrrVggTb2qsXgvPMBzZfMS9V0DTFrzGb1ni8tu00S2wPcqZ_tD8ah40wTBWkqi4cZkj_39Ihy8DzarpSSzbm7VA_SOQ1IIznCYyVNm-ViY_3H2MmnQF5GMugPMIN3KqghA5DpSkmTNmH8MrjvdkSnQ_y4b1s1dmWuJTVYPtq5UlANW0MjX55u6pUyv-UvAMAu8KikkzXNZ0KNWZ5YYGMCbWn5M-nbXm3Fg3GY5td5Ye5L3fX0lL7HTWMcJli6eU-8qbjvpJQ-mJ-4LHdB5Sk13uM01uA2sIS4P9nQu_9zHObpkH8XokFF6ZwAAAAEtFV2tAA")
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
    "START_IMG_URL", "https://envs.sh/wc1.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/wc1.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/wc1.jpg"
STATS_IMG_URL = "https://envs.sh/wc1.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/wc1.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/wc1.jpg"
STREAM_IMG_URL = "https://envs.sh/wc1.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/wc1.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/wc1.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/wc1.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/wc1.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/wc1.jpg"


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
