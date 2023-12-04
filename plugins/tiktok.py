from pyrogram import filters, Client as Mbot
import bs4, requests,re,asyncio
import wget,os,traceback
from bot import LOG_GROUP,DUMP_GROUP

@Mbot.on_message(filters.regex(r'https?://.*tiktok[^\s]+') & filters.incoming)
async def link_handler(Mbot, message):
    link = message.matches[0].group(0)
    try:
        m = await message.reply_text("⏳")
        get_api= requests.post("https://lovetik.com/api/ajax/search",data={"query":link}).json()
        if get_api['status'] and "Invalid TikTok video url" in get_api['mess']: 
           return await message.reply("Oops Invalid TikTok video url. Please try again :) ")
        if get_api.get('links'):
           try:
              dump_file = await message.reply_video(get_api['links'][0]['a'], caption="Thank you for using - @InstaReelsdownbot")
           except KeyError:
               return await message.reply("Invalid TikTok video url. Please try again.")
           except Exception:
               snd_msg=await message.reply(get_api['links'][0]['a'])
               await asyncio.sleep(1)
               try:
                  dump_file = await message.reply_video(get_api['links'][0]['a'],caption="Thank you for using - @InstaReelsdownbot")
                  await snd_msg.delete()
               except Exception:
                   pass
    except Exception as e:      
        if LOG_GROUP:
               await Mbot.send_message(LOG_GROUP,f"TikTok {e} {link}")
               await Mbot.send_message(LOG_GROUP, traceback.format_exc())          
    finally:
        if 'dump_file' in locals():
            if DUMP_GROUP:
               await dump_file.copy(DUMP_GROUP)
            await m.delete()
