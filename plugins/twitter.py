from pyrogram import filters, Client as Mbot
import bs4, requests,re,asyncio
import wget,os,traceback
from bot import LOG_GROUP,DUMP_GROUP
from bs4 import BeautifulSoup
headers = {
            "Host": "ssstwitter.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "HX-Request": "true",
            "Origin": "https://ssstwitter.com",
            "Referer": "https://ssstwitter.com/id",
            "Cache-Control": "no-cache",
}
@Mbot.on_message(filters.regex(r'https?://.*twitter[^\s]+') & filters.incoming)
async def twitter_handler(Mbot, message):
      link = message.matches[0].group(0)
      try:
          data = {
            "id": link,
            "locale": "id",
            "tt": "bc9841580b5d72e855e7d01bf3255278l",
            "ts": "1691416179",
            "source": "form",
          }
          m = await message.reply_text("⏳")
          get_api=post("https://ssstwitter.com/id",data=data,headers=headers)
          try:
              soup = BeautifulSoup(get_api.text, "lxml")
              cekdata = soup.find("a", {"pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark vignette_active"})
          except Exception as e:
              print(e)
              return await message.reply("Oops Invalid TikTok video url. Please try again :)")
          try:
              dump_file = await message.reply_video(cekdata.get('href'))
          except Exception as e:
              print(e)
              snd_msg = await message.reply(cekdata.get('href'))
              await asyncio.sleep(1)
              try:
                  await message.reply_video(cekdata.get('href'))
              except Exception as e:
                  pass
                  print(e)
      except Exception as e:
          print(e)
          if LOG_GROUP:
             await Mbot.send_message(LOG_GROUP,f"TikTok {e} {link}")
             await Mbot.send_message(LOG_GROUP, traceback.format_exc())          
      finally:
         if 'dump_file' in locals():
            if DUMP_GROUP:
               await dump_file.copy(DUMP_GROUP)
            await m.delete()
  
