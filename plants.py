#!/usr/bin/python3
# coding=utf-8

# read options from config.py
import config

import telepot
from telepot.loop import MessageLoop
bot = telepot.Bot(config.botKey)

from time import sleep
import datetime
import os

from pprint import pprint, pformat

def startPlants():
    while True:
        #print("plants.")
        plant()
        sleep(100)

def plant():
    today = datetime.datetime.now()
    
    # if it's the right day and time
    if (today.weekday() == 0 or today.weekday() == 4) and today.hour >= 9:
        
        # if we haven't done our work for today yet...
        if not os.path.exists("job_well_done"):
            
            # ... send the message :D
            bot.sendMessage(config.groupid, "💦🌱🌿😌")
            
            # create a file so we know not to do it again today
            with open("job_well_done", "w") as f:
                f.close()
        
        # ... otherwise we're done. ^^
        else:
            pass
        
    # if it's any other day of the week
    else:
        
        # delete the file so we know to send the message again later
        if os.path.exists("job_well_done"):
            os.remove("job_well_done")        

#print("starting thread...")
startPlants()
#Thread(target=startPlants).start()
