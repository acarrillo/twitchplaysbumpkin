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



def vip1forward():
        GPIO.output(array[1], True)
        GPIO.output(array[0], False)
        GPIO.output(array[2], True)
        GPIO.output(array[3], False)


def frog1forward():
        GPIO.output(array3[1], False)
        GPIO.output(array3[0], False)
        GPIO.output(array3[2], False)
        GPIO.output(array3[3], True)

def frog1stop():
        GPIO.output(array3[1], False)
        GPIO.output(array3[0], False)
        GPIO.output(array3[2], False)
        GPIO.output(array3[3], False)        

def gat1counter():
        GPIO.output(array2[1], False)
        GPIO.output(array2[0], True)
        GPIO.output(array2[2], True)
        GPIO.output(array2[3], False)

def gat1reverse():
        GPIO.output(array2[0], False)
        GPIO.output(array2[1], True)
        GPIO.output(array2[2], True)
        GPIO.output(array2[3], False)


def gat1forward():
        GPIO.output(array2[1], False)
        GPIO.output(array2[0], True)
        GPIO.output(array2[3], True)
        GPIO.output(array2[2], False)
        
def vip1reverse():
        GPIO.output(array[0], True)
        GPIO.output(array[1], False)
        GPIO.output(array[3], True)
        GPIO.output(array[2], False)

def gat1clock():
        GPIO.output(array2[1], True)
        GPIO.output(array2[0], False)
        GPIO.output(array2[2], False)
        GPIO.output(array2[3], True) 
        

def vip1stop():
        GPIO.output(array[0], False)
        GPIO.output(array[1], False)
        GPIO.output(array[2], False)
        GPIO.output(array[3], False)

def gat1stop():
        GPIO.output(array2[0], False)
        GPIO.output(array2[1], False)
        GPIO.output(array2[2], False)
        GPIO.output(array2[3], False)
        
def vip1clock():
        GPIO.output(array[1], True)
        GPIO.output(array[0], False)
        GPIO.output(array[3], True)
        GPIO.output(array[2], False)

def vip1counter():
        GPIO.output(array[0], True)
        GPIO.output(array[1], False)
        GPIO.output(array[2], True)
        GPIO.output(array[3], False)        

while True:
    time.sleep(1)
    vip1forward()
    gat1reverse()
    frog1forward()
    time.sleep(1)
    
    vip1clock()
    gat1counter()
    time.sleep(1)
    
    vip1counter()
    gat1clock()
    time.sleep(1)
    
    vip1reverse()
    gat1forward()
    time.sleep(1)
    while True:
        vip1stop()
        gat1stop()
        frog1stop()
    

    



