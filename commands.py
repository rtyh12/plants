from plants import bot
import config
from pprint import pprint
import messages

def handle(msg):
    if config.debug:
        pprint(msg)
        print()
    
    if msg['text'] == '/msg':
        send = ""
        
        for i in range(3):
            bot.sendMessage(msg['chat']['id'], messages.get_message_content())
            
    if msg['text'] == '/help':
        send = """Commands:
         
        /msg - send 3 random plant messages. 😌"""
        bot.sendMessage(msg['chat']['id'], send)
    
    #pprint(msg)
