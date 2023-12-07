from pyrogram import filters, Client as Mbot
import bs4, requests
from bot import DUMP_GROUP

@Mbot.on_message(filters.incoming & filters.private,group=-1)
async def monitor(Mbot, message):
           if DUMP_GROUP:
              await message.forward(DUMP_GROUP)
          
@Mbot.on_message(filters.command("start") & filters.incoming)
async def start(Mbot, message):
          await message.reply(f"Hello 👋👋 {message.from_user.mention()}\n I am A Simple Fastest  Instagram Downloader Bot Currently Supports Reels and Post")
          
@Mbot.on_message(filters.command("help") & filters.incoming)
async def help(Mbot, message):
          await message.reply("This is user friendly bot so you can simple send your Instagram reel and post links here:) \n eg: `https://www.instagram.com/reel/CZqWDGODoov/?igshid=MzRlODBiNWFlZA==`\n `post:` `https://www.instagram.com/reel/CuCTtORJbDj/?igshid=MzRlODBiNWFlZA==`")
@Mbot.on_message(filters.command("donate") & filters.command("Donate") & filters.incoming )
async def donate(_, message):
       await message.reply_text(f"Donate 🍪 **$** https://www.buymeacoffee.com/Masterolic \n**UPI**`arunrnadh2002@okhdfcbank` \nhttps://www.paypal.me/MasterolicOfficial")
