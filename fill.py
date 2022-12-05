#AUTO VARS ADDING CODE MADE BY AYUSH
#THIS WORK ONLY FOR VPS 

import os
from dotenv import load_dotenv, find_dotenv, set_key
load_dotenv(find_dotenv())

#-----please do not change the code else it will return errors----#
#-----------pure code for adding vars in .env file----------------#

print("This File Will Fill The Vars In .env File..If You Want To Add Or Edit Vars In The .env, Please Use > nano .env\n\n")
set_key('.env','API_ID', input("API_ID : "))
set_key('.env','API_HASH', input("API_HASH : "))
set_key('.env','STRING_SESSION1', input("STRING_SESSION 1 : "))
set_key('.env','STRING_SESSION2', input("STRING SESSION 2 : "))
set_key('.env','STRING_SESSION3', input("STRING SESSION 3 : "))
set_key('.env','STRING_SESSION4', input("STRING SESSION 4 : "))
set_key('.env','STRING_SESSION5', input("STRING SESSION 5 : "))
set_key('.env','BOT_TOKEN', input("BOT_TOKEN : "))
set_key('.env','MONGO_DB_URI', input("MONGO_DB_URI : "))
set_key('.env','MUSIC_BOT_NAME', input("MUSIC_BOT_NAME : "))
set_key('.env','OWNER_ID_ONE', input("OWNER_ID_ONE : "))
set_key('.env','OWNER_ID_TWO', input("OWNER_ID_TWO : "))
set_key('.env','LOG_GROUP_ID', input("LOG_GROUP_ID : "))
set_key('.env','AUTO_LEAVE_ASSISTANT_TIME', input("AUTO_LEAVE_ASSISTANT_TIME : "))
set_key('.env','AUTO_LEAVING_ASSISTANT', input("AUTO LEAVE ASSISTANT (True/None) : "))
set_key('.env','SPOTIFY_CLIENT_ID', input("SPOTIFY CLIENT ID : "))
set_key('.env','SPOTIFY_CLIENT_SECRET ', input("SPOTIFY CLIENT SECRET  : "))
set_key('.env','GBAN_LOG ', input("GBAN LOG CHANNEL ID  : "))
set_key('.env','DM_LINK', input("MESSAGE OR LINK TO SHARE INCOMING DM/PRIVATE MESSAGES : "))
print("All Basic Vars Has Been Set To Bot. Now You Can Skip Upcoming Vars Or Give URL To Download Thumbnails From Web.")
print("......................")
print("......................")
set_key('.env','PING_IMG_URL', input("PING IMG URL : "))
set_key('.env','PLAYLIST_IMG_URL', input("PLAYLIST IMG URL : "))
set_key('.env','GLOBAL_IMG_URL', input("GLOBAL IMG URL : "))
set_key('.env','STATS_IMG_URL', input("STATS IMG URL : "))
set_key('.env','TELEGRAM_AUDIO_URL', input("TELEGRAM AUDIO URL : "))
set_key('.env','TELEGRAM_VIDEO_URL', input("TELEGRAM VIDEO URL : "))
set_key('.env','STREAM_IMG_URL', input("STREAM IMG URL : "))
set_key('.env','SOUNCLOUD_IMG_URL', input("SOUNCLOUD IMG URL : "))
set_key('.env','YOUTUBE_IMG_URL', input("YOUTUBE IMG URL : "))
set_key('.env','SPOTIFY_ARTIST_IMG_URL', input("SPOTIFY ARTIST IMG URL : "))
set_key('.env','SPOTIFY_ALBUM_IMG_URL', input("SPOTIFY ALBUM IMG URL : "))
set_key('.env','SPOTIFY_PLAYLIST_IMG_URL', input("SPOTIFY PLAYLIST IMG URL : "))
