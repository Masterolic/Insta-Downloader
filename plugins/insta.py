from pyrogram import filters, Client as Mbot
import bs4, requests
import wget,os,traceback
from bot import LOG_GROUP,DUMP_GROUP
@Mbot.on_message(filters.regex(r'https?://.*instagram[^\s]+') & filters.incoming, group=1)
async def link_handler(Mbot, message):
    link = message.matches[0].group(0)
    try:
        m = await message.reply_text("⏳")
        url= link.replace("instagram.com","ddinstagram.com")
        url=url.replace("==","%3D%3D")
        if url.endswith("="):
           dump_file=await message.reply_video(url[:-1])
        else:
            dump_file=await message.reply_video(url)
        if 'dump_file' in locals():
           await dump_file.forward(DUMP_GROUP)
        await m.delete()
    except Exception as e:
        try:
            if "/reel/" in url:
               getdata = requests.get(url).text
               soup = bs4.BeautifulSoup(getdata, 'html.parser')
               meta_tag = soup.find('meta', attrs={'property': 'og:video'})
               if not meta_tag:
                  meta_tag = soup.find('meta', attrs={'property': 'og:image'})    
               content_value = meta_tag['content']
               downfile=wget.download(f"https://ddinstagram.com{content_value}")
               dump_file=await message.reply_video(downfile) 
            elif "/p/" in url:
                 getdata = requests.get(url).text
                 soup = bs4.BeautifulSoup(getdata, 'html.parser')
                 meta_tag = soup.find('meta', attrs={'property': 'og:video'})
                 if not meta_tag:
                    meta_tag = soup.find('meta', attrs={'property': 'og:image'})
                    content_value = meta_tag['content']
                    downrm=wget.download(f"https://ddinstagram.com{content_value}")
                    os.rename(downrm,f"{downrm}.png")
                    downfile=f"{downrm}.png"
                    dump_file=await message.reply_photo(downfile)
                 else:
                     content_value = meta_tag['content']
                     downfile=wget.download(f"https://ddinstagram.com{content_value}")
                     dump_file=await message.reply_video(downfile)
        except Exception as e:
            await message.reply_text(f"https://ddinstagram.com{content_value}")
            if LOG_GROUP:
               await Mbot.send_message(LOG_GROUP,f"Instagram {e} {content_value}")
               tracemsg=traceback.extract_tb(e.__traceback__)
               await message.reply(tracemsg)
            ##optinal 
            await message.reply(f"400: Sorry, Unable To Find It  try another or report it  to @masterolic or support chat @spotify_supportbot 🤖  ")

        finally:
            if 'dump_file' in locals():
               if DUMP_GROUP:
                  await dump_file.forward(DUMP_GROUP)
            await m.delete()
            if 'downfile' in locals():
                os.remove(downfile)
                
