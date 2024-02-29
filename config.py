from json import load
import os
from dotenv import load_dotenv

load_dotenv()

Chiku_MONGO_HOST = os.environ.get('Chiku_mongo_host', "")
BOT_TOKEN = os.environ.get('bot_token', "")