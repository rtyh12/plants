#!/usr/bin/python3
# coding=utf-8

# read options from config.py
import config
import messages
import commands

import telepot
from telepot.loop import MessageLoop
bot = telepot.Bot(config.bot_token)

from time import sleep
import datetime
import os

from pprint import pprint, pformat

def start_plants():
    while True:
        plant()
        sleep(config.thread_loop_timeout)

def plant():
    today = datetime.datetime.now()
    
    # if it's the right day and time
    if (today.weekday() == 0 or today.weekday() == 4) and today.hour >= 9:
        
        # if we haven't done our work for today yet...
        if not os.path.exists("tmp/job_well_done"):
            
            # ... send the message :D
            bot.sendMessage(config.groupid_MAIN, messages.get_message_content())
            
            # create a file so we know not to do it again today
            with open("tmp/job_well_done", "w") as f:
                f.close()
        
        # ... otherwise we're done. ^^
        else:
            pass
        
    # if it's any other day of the week
    else:
        
        # delete the file so we know to send the message again later
        if os.path.exists("tmp/job_well_done"):
            os.remove("tmp/job_well_done")
            
if __name__ == '__main__':
    telepot.loop.MessageLoop(bot, commands.handle).run_as_thread()
    
    start_plants()