from pyrogram import filters, Client 
import bs4, requests

@Mbot.on_message(filters.regex(r'https?://.*instagram[^\s]+'), group=1)
async def link_handler(Mbot, message):
    link = message.matches[0].group(0)
    try:
        m = await message.reply_text("⏳")
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
            if LOG_GROUP:
               await Mbot.send_message(LOG_GROUP,f"Instagram {e} {content_value}")
            ##optinal 
            await message.reply(f"400: Sorry, Unable To Find It  try another or report it  to @masterolic or support chat @spotify_supportbot 🤖  ")

