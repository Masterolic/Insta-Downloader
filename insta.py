#https://t.me/Masterolic
from pyrogram import filters, Client 
import bs4, requests
from sys import environ
from dotenv import load_dotenv
load_dotenv("config.env")
API_ID=int(environ['API_ID'])
API_HASH=environ['API_HASH']
BOT_TOKEN=environ['BOT_TOKEN']
Mbot=Client(api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=16,
            sleep_threshold=22)

@Mbot.on_message(filters.regex(r'https?://.*instagram[^\s]+'), group=1)
async def link_handler(Mbot, message):
    link = message.matches[0].group(0)
    get_s = await db.get_set(message.chat.id)
    if get_s['http'] == "False":
       return
    try:
 #       m = await message.reply_text("⏳")
        url= link.replace("instagram.com","ddinstagram.com")
        await message.reply_video(url)
    except Exception as e:
        try:
            if "/reel/" in url:
               getdata = requests.get(url).text
               soup = bs4.BeautifulSoup(getdata, 'html.parser')
               meta_tag = soup.find('meta', attrs={'property': 'og:video'})
               content_value = meta_tag['content']
               await message.reply_video(f"https://ddinstagram.com{content_value}")
            elif "/p/" in url:
                 getdata = requests.get(url).text
                 soup = bs4.BeautifulSoup(getdata, 'html.parser')
                 meta_tag = soup.find('meta', attrs={'property': 'og:image'})
                 content_value = meta_tag['content']
                 await message.reply_photo(f"https://ddinstagram.com{content_value}")
        except Exception as e:
            await message.reply_text(f"https://ddinstagram.com{content_value}")
            await Mbot.send_message(-1001744816254,f"Instagram {e} {content_value}")
            await message.reply(f"400: Sorry, Unable To Find It  try another or report it  to @masterolic or support chat @spotify_supportbot 🤖  ")
if __name__ == '__main__':
    print (" Insta-DL Bot started  running...")

Mbot.run()