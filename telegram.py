import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'on':
       bot.sendMessage(chat_id, on(11))
    elif command =='off':
       bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('758897921:AAH4pFvDrKsUlJ1vfs5u-fLhm54vv-HFffI')
bot.message_loop(handle)
print 'I am listening...'

while 1:
        try:
             time.sleep(10)

        except keyboardInterrupt:
                print("program interprited")
                GPIO.cleanup()
                exit()
        except:
                print("other error")
                GPIO.cleanup()