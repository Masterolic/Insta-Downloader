from pyrogram import filters, Client 
import bs4, requests

@Mbot.on_message(filters.command("start") & filters.incoming)
async def start(Mbot, message):
          await message.reply(f"Hello 👋👋 {message.from_user.mention()}\n I am A Simple Fastest  Instagram Downloader Bot Currently Supports Reels and Post")
@Mbot.on_message(filters.command("help") & filters.incoming)
async def start(Mbot, message):
          await message.reply(f"Help Guide For  {message.from_user.mention()}\n I am A Simple Fastest  Instagram Downloader Bot Currently Supports Reels and Post \n reel: `https://www.instagram.com/reel/CuCTtORJbDj/?igshid=MzRlODBiNWFlZA==`\n post: `https://www.instagram.com/reel/CZqWDGODoov/?igshid=MzRlODBiNWFlZA==`")

