import time, datetime
import telepot
from telepot.loop import MessageLoop
now = datetime.datetime.now()
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    command = command.lower()
    print('Received:%s'%command)
    if '/hi' in command:
    	Iot_wala_bot.sendMessage(chat_id,str("Hi! CircuitDigest"))
    elif '/start' in command:
    	Iot_wala_bot.sendMessage(chat_id,str("Hi! please use / in the front of command example /hi we can discuss on my project ARgoggle(EDITH) and my asistant Arish"))
    elif '/time' in command:
    	Iot_wala_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif '/logo' in command:
    	Iot_wala_bot.sendPhoto (chat_id, photo = "http://kanhakidukan.onweb.im/icon/1.png")
    elif '/file' in command:
    	Iot_wala_bot.sendDocument (chat_id, document=open('arish.txt'))
    elif '/audio' in command:
    	Iot_wala_bot.sendAudio(chat_id,audio=open('Ry.mp3','rb'))
    elif '/video' in command:
    	Iot_wala_bot.sendVideo(chat_id,video=open('Arish.mp4','rb'))
Iot_wala_bot= telepot.Bot('5713094539:AAETLmjGo9mgWRdVQ16cRwxxt5nIeAalbFY')
print (Iot_wala_bot.getMe())
MessageLoop(Iot_wala_bot,action).run_as_thread()
print ('Up and Running....')
while 1:
    time.sleep(10)