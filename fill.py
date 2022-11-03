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
set_key('.env','STRING_SESSION1', input("STRING_SESSION1 : "))
set_key('.env','BOT_TOKEN', input("BOT_TOKEN : "))
set_key('.env','MONGO_DB_URI', input("MONGO_DB_URI : "))
set_key('.env','MUSIC_BOT_NAME', input("MUSIC_BOT_NAME : "))
set_key('.env','OWNER_ID_ONE', input("OWNER_ID_ONE : "))
set_key('.env','OWNER_ID_TWO', input("OWNER_ID_TWO : "))
set_key('.env','LOG_GROUP_ID', input("LOG_GROUP_ID : "))
set_key('.env','MUSIC_BOT_NAME', input("MUSIC_BOT_NAME : "))
set_key('.env','AUTO_LEAVE_ASSISTANT_TIME', input("AUTO_LEAVE_ASSISTANT_TIME : "))
