import willie
import time
import sys
import select
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, False)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, False)


GPIO.setup(27, GPIO.OUT)
GPIO.output(27, False)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, False)
GPIO.setup(9, GPIO.OUT)
GPIO.output(9, False)

GPIO.setup(2, GPIO.OUT)
GPIO.output(2, False)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, False)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)


array = [11, 7, 8, 25]
array2 =[27, 22, 10, 9]
array3 =[2, 3, 4, 17]

vip1_is_turning = False
vip1_is_straight = False
gat1_is_turning = False
gat1_is_straight = False
vip1_str8_time = 0
vip2_str8_time = 0
vip1_turn_time = 0
vip2_turn_time = 0
gat1_str8_time = 0
gat2_str8_time = 0
gat1_turn_time = 0
gat2_turn_time = 0

def vip1forward():
    global vip1_str8_time
    global vip1_is_straight
    vip1_str8_time = time.time()
    vip1_is_straight = True
    GPIO.output(array[1], True)
    GPIO.output(array[0], False)
    GPIO.output(array[2], True)
    GPIO.output(array[3], False)


def frog1forward():
    GPIO.output(array3[1], False)
    GPIO.output(array3[0], True)
    GPIO.output(array3[2], False)
    GPIO.output(array3[3], True)

def frog1stop():
    GPIO.output(array3[1], False)
    GPIO.output(array3[0], False)
    GPIO.output(array3[2], False)
    GPIO.output(array3[3], False)        

def gat1counter():
    global gat1_turn_time
    global gat1_is_turning
    gat1_is_turning = True
    gat1_turn_time = time.time()
    GPIO.output(array2[1], False)
    GPIO.output(array2[0], True)
    GPIO.output(array2[2], True)
    GPIO.output(array2[3], False)

def gat1reverse():
    global gat1_str8_time
    global gat1_is_straight
    gat1_is_straight = True
    gat1_str8_time = time.time()
    GPIO.output(array2[0], False)
    GPIO.output(array2[1], True)
    GPIO.output(array2[2], True)
    GPIO.output(array2[3], False)

def gat1forward():
    global gat1_str8_time
    global gat1_is_straight
    gat1_is_straight = True
    gat1_str8_time = time.time()
    GPIO.output(array2[1], False)
    GPIO.output(array2[0], True)
    GPIO.output(array2[3], True)
    GPIO.output(array2[2], False)
        
def vip1reverse():
    global vip1_str8_time
    global vip1_is_straight
    vip1_is_straight = True
    vip1_str8_time = time.time()
    GPIO.output(array[0], True)
    GPIO.output(array[1], False)
    GPIO.output(array[3], True)
    GPIO.output(array[2], False)

def gat1clock():
    global gat1_turn_time
    global gat1_is_turning
    gat1_is_turning = True
    gat1_turn_time = time.time()
    GPIO.output(array2[1], True)
    GPIO.output(array2[0], False)
    GPIO.output(array2[2], False)
    GPIO.output(array2[3], True) 
        

def vip1stop():
    vip1_is_turning = False
    vip1_is_straight = False
    GPIO.output(array[0], False)
    GPIO.output(array[1], False)
    GPIO.output(array[2], False)
    GPIO.output(array[3], False)

def gat1stop():
    gat1_is_turning = False
    gat1_is_straight = False
    GPIO.output(array2[0], False)
    GPIO.output(array2[1], False)
    GPIO.output(array2[2], False)
    GPIO.output(array2[3], False)
        
def vip1clock():
    vip1_turn_time = time.time()
    GPIO.output(array[1], True)
    GPIO.output(array[0], False)
    GPIO.output(array[3], True)
    GPIO.output(array[2], False)

def vip1counter():
    vip1_turn_time = time.time()
    GPIO.output(array[0], True)
    GPIO.output(array[1], False)
    GPIO.output(array[2], True)
    GPIO.output(array[3], False)        


@willie.module.interval(0.375)
def checkTimeouts(bot):
    forconst = 0.5
    turnconst = 2.5

    if vip1_is_turning and time.time() - vip1_turn_time > turnconst:
        vip1stop()
    elif vip1_is_straight and time.time() - vip1_str8_time > forconst:
        vip1stop()
    elif gat1_is_turning and time.time() - gat1_turn_time > turnconst:
        gat1stop()
    elif gat1_is_straight and time.time() - gat1_str8_time > forconst:
        gat1stop()



@willie.module.rule('([^\s]+)')
def helloworld(bot, trigger):
    cmd = trigger.bytes.decode(encoding='UTF-8')

    if cmd == "for1":
        bot.say("asdfExecuting " + cmd)
        vip1forward()
    elif cmd == "rev1":
        bot.say("Executing " + cmd)
        vip1reverse()
    elif cmd == "clock1":
        bot.say("Executing " + cmd)
        vip1clock()
    elif cmd == "count1":
        bot.say("Executing " + cmd)
        vip1counter()
    elif cmd == "for2":
        bot.say("Executing " + cmd)
        gat1forward()
    elif cmd == "rev2":
        bot.say("Executing " + cmd)
        gat1reverse()
    elif cmd == "clock2":
        gat1clock()
    elif cmd == "count2":
        gat1counter()
