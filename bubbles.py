#import modules
from machine import Pin
import time

#setup the sensor
lightsensor = Pin(21, Pin.IN)

#setup the motor
IN1=Pin(4,Pin.OUT)
IN2=Pin(5,Pin.OUT)
IN3=Pin(13,Pin.OUT)
IN4=Pin(14,Pin.OUT)

#create motor step sequence
sequence = [[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]]
def rotate_45():
    steps_45_deg = 64
    for i in range(steps_45_deg):
        for step in sequence:
            IN1.value(step[0])
            IN2.value(step[1])
            IN3.value(step[2])
            IN4.value(step[3])
            time.sleep_ms(2)

#loop to rotate
while True:
    if lightsensor.value() == 0:
        print("Coin detected, gumball dispensing")
        rotate_45()
        time.sleep(1)
    else:
        print("No coin detected")
    time.sleep(0.1)
