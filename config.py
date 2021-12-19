import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Zxyune")
ALIVE_NAME = getenv("ALIVE_NAME", "Takichan")
BOT_USERNAME = getenv("BOT_USERNAME", "LalaStrMusic_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AsisstantMusic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Takichanbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Takichanbot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/e27b0520a6df2337dbfa5.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/f0c793973ab175d88f11b.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/0fab1bb3a391079a67ecd.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/636da766bb9ce67ab1c77.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/2e623648de109b8883006.jpg")
