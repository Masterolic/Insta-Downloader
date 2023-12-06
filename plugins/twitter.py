from pyrogram import filters,Client as Mbot
from bot import LOG_GROUP,DUMP_GROUP
import os,re,asyncio,bs4
import requests,wget,traceback

@Mbot.on_message(filters.regex(r'https?://.*twitter[^\s]+'),filters.incoming)
async def twitter_handler(Mbot,message):
   try:            
      link=message.matches[0].group(0)
      if "x.com" in link:
         link=link.replace("x.com","fxtwitter.com")
      if "twitter.com" in link:
         link = link.replace("twitter.com","fxtwitter.com")
      await message.reply_text("⏳")
      try:
          dump_file = await message.reply_video(link)
      except Exception as e:
          print(e)
          try:
             snd_message=await message.reply(link)
             await asyncio.sleep(1)
             dump_file = await message.reply_video(link)
             await snd_message.delete()
          except Exception as e:
              print(e)
              get_api=requests.get(link).text
              soup=bs4.BeautifulSoup(get_api,"html.parser")
              meta_tag= soup.find("meta", attrs = {"property": "og:video"})
              if not meta_tag:
                  meta_tag = soup.find("meta", attrs={"property": "og:image"})
              content_value  = meta_tag['content']
              try:
                  dump_file = await message.reply_video(content_value)
              except Exception as e:
                  print(e)
                  try:
                     snd_msg=await message.reply(content_value)
                     await asyncio.sleep(1)
                     await message.reply_video(content_value)
                     await snd_msg.delete()
                  except Exception as e:
                      print(e)
                      await message.reply("Oops Invalid link or Media Is Not Available:)")
   except Exception as e:
        if LOG_GROUP:
           await Mbot.send_message(e)
           await Mbot.send_message(traceback.exec())
   finally:
       if DUMP_GROUP:
          if "dump_file" in locals():
             await dump_file.copy(DUMP_GROUP)
       await m.delete()
                      
                  
            
