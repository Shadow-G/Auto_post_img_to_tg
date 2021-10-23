#!usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import os
import time
import random
import requests

TOKEN = "" # token
CHAT = "" # @group
CHAT_ID = "" # -id

bot = telebot.TeleBot(TOKEN)

print("Telegram Bot is Start")

files = os.listdir("img")
if files == []:
    print("пусто")
#print(files) 

bots = True
while bots:
    img = random.choice(files)
    #print(img)
    url = "https://api.telegram.org/bot" + TOKEN + "/sendPhoto";
    files = {'photo': open("img/" + img, 'rb')}
    data = {'chat_id' : CHAT_ID}
    r= requests.post(url, files=files, data=data)
    
    os.remove(f"img/{img}")

    time.sleep(3600.0)

