from machine import Pin, TouchPad
import time

Q0=Pin(15,Pin.OUT)
Q1=Pin(2,Pin.OUT)
Q2=Pin(4,Pin.OUT)
Q3=Pin(5,Pin.OUT)

touchpin1 = TouchPad(Pin(33))  #green
touchpin2 = TouchPad(Pin(32))  #yellow
touchpin3 = TouchPad(Pin(27))  #red
threshold=300

#while(1):
    #Q0.value(1)
    #Q1.value(1)
    #time.sleep(10)
    #Q0.value(0)
    #Q1.value(0)
    #time.sleep(5)


while (True):
    capacitiveValue1 = touchpin1.read()
    capacitiveValue2 = touchpin2.read()
    capacitiveValue3 = touchpin3.read()

    if (capacitiveValue1 < threshold) or (capacitiveValue2 < threshold) or (capacitiveValue3 < threshold):
        print("Jeremy in action!")
        Q0.value(1)
        Q1.value(1)
        time.sleep(1)
    else:
        print("Jeremy is asleep.")
        Q0.value(0)
        Q1.value(0)
        time.sleep(1)
