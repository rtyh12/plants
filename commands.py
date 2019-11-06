from plants import bot
import messages

def handle(msg):
    print("hello")
    
    if msg['text'] == '/msg':
        send = ""
        
        for i in range(3):
            bot.sendMessage(msg['chat']['id'], messages.get_message_content())
            
    if msg['text'] == '/help':
        send = """Commands:
         
        /msg - send 3 random plant messages. 😌"""
        bot.sendMessage(msg['chat']['id'], send)
    
    #pprint(msg)