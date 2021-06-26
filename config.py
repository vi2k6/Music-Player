from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH", "")

START_IMG = getenv("START_IMG", "https://telegra.ph/file/c5f676adcdbe5a0bbb232.jpg")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
