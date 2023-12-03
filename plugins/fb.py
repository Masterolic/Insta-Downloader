from pyrogram import filters, Client as Mbot
import bs4, requests,re,asyncio
import wget,os,traceback
from bot import LOG_GROUP,DUMP_GROUP

@Mbot.on_message(filters.regex(r'https?://.*facebook[^\s]+') & filters.incoming, group=-1)
async def link_handler(Mbot, message):
    link = message.matches[0].group(0)
    try:
       m = await message.reply_text("⏳")
       get_api=requests.get(f"https://yasirapi.eu.org/fbdl?link={link}")
       if get_api['success'] == "false":
          return await message.reply("Invalid TikTok video url. Please try again :)")
       while True:
          if get_api.get('hd'):
             try:
                 dump_file = await message.reply_video(get_api['result']['hd'],caption="Thank you for using - @InstaReelsdownbot")
             except KeyError:
                 pass 
             except Exception:
                 try:
                     sndmsg = await message.reply(get_api['result']['hd'])
                     await asyncio.sleep(1)
                     dump_file = await message.reply_video(get_api['result']['hd'],caption="Thank you for using - @InstaReelsdownbot")
                     await sndmsg.delete()
                 except Exception:
                      pass 
          else: 
             if get_api.get('sd'):
               try:
                   dump_file = await message.reply_video(get_api['result']['sd'],caption="Thank you for using - @InstaReelsdownbot")
               except KeyError:
                   pass
               except Exception:
                   try:
                       sndmsg = await message.reply(get_api['result']['sd'])
                       await asyncio.sleep(1)
                       dump_file = await message.reply_video(get_api['result']['sd'],caption="Thank you for using - @InstaReelsdownbot")
                       await sndmsg.delete()
                   except Exception:
                      pass 
    except Exception as e:
           if LOG_GROUP:
               await Mbot.send_message(LOG_GROUP,f"Facebook {e} {link}")
               await Mbot.send_message(LOG_GROUP, traceback.format_exc())          
    finally:
          if 'dump_file' in locals():
            if DUMP_GROUP:
               await dump_file.copy(DUMP_GROUP)
          await m.delete()      
