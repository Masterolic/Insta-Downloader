# Insta-Downloader
This is a simple telegram bot using python to download reels/post from Instagram 

[DEMO VERSION  @Spotify_downloa_bot ](https://t.me/Spotify_downloa_bot)
### IS THIS STILL MAINTAINING?
> Yes ,this repository is still maintained and will be adding new feature's
> 
### WHICH  LANGUAGE AND TELEGRAM API  USED IN THIS ?
> This bot is  created using python language and python  mtproto pyrogram telegram library 

### DONATE ME PLEASE ❣️
> Please buy me a piza by using bellow link 👇👇👇
[Buy Me A Piza](https://www.buymeacoffee.com/Masterolic)

### ABOUT
> A Simple Open Source  Insta Downloader Bot For Telegram 

### WHY I MADE THIS OPEN SOURCE  ?
> The answer simple Let Everyone Deploy there own bots

 
### EASY WAY TO  DEPLOY IN  LOCAL/VPS ?
> First add variables in [config.env](https://github.com/Masterolic/Insta-Downloader/blob/main/config.env)


```
apt update && apt upgrade -y 
apt install git ffmpeg python3 python3-pip -y
git clone https://github.com/Masterolic/Insta-Downloader.git 
cd Insta-Downloader/
pip3 install -r requirements.txt 
python3 bot.py
```

### DOCKER
```
  docker build . -t musicbot
  docker run musicbot  
```
### ENVIRONMENT VARIABLES
#### you need to add these variable in [config.env](https://github.com/Masterolic/Insta-Downloader/blob/main/config.env)

`API_ID and API_HASH` get through [Telegram](https://my.telegram.org)

`BOT_TOKEN`get through [@BotFather](https://t.me/BotFather)

### OPTIONAL ENVIRONMENT VARIABLES 

`LOG_GROUP`Telegram chat id of your log group to dump errors

`DUMP_GROUP` Telegram chat id for logging all messages send to bot dm also files sended by bot 

`RESTART_ON` Pass True To Restart Every 6 Hours .If Your Server Is Heroku It Changes Ip Address Which Prevents Ip Block Or Idle Due To Unknown Reason

`FIXIE_SOCKS_HOST` Pass Your Proxy Url If Available It Prevents Ip Block And Access Restricted Content  You Can Buy Proxy From Heroku See  Below Given  Video 

https://github.com/Masterolic/Insta-Downloader/assets/93469093/87cdc4e7-58b6-4dc3-873b-65e86e2bc1f4


### CAN I CONTACT OWNER ?
 >  IF you need any help or need to add any features or tell feedback , don't hesitate to contact me 

[INSTAGRAM](https://instagram.com/masterolic_official)


[TELEGRAM](https://t.me/Masterolic)
