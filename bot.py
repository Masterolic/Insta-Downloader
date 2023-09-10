#https://t.me/Masterolic
from pyrogram import filters, Client 
import bs4, requests
from os import environ
from dotenv import load_dotenv
load_dotenv("config.env")
API_ID=int(environ['API_ID'])
API_HASH=environ['API_HASH']
BOT_TOKEN=environ['BOT_TOKEN']
LOG_GROUP=environ.get('LOG_GROUP',"")
DUMP_GROUP=environ.get('DUMP_GROUP',"")
OWNER_ID=environ['OWNER_ID']
if LOG_GROUP:
   int(LOG_GROUP)
if DUMP_GROUP:
   int(DUMP_GROUP)
Mbot=Client(name="instabot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
            sleep_threshold=22)
if __name__ == '__main__':
    print (" Insta-DL Bot started  running...")
    Mbot.run()
