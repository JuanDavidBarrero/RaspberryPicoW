from machine import Pin, Timer
import time

led= Pin("LED", Pin.OUT)
red = Pin(2,Pin.OUT)

led.value(0)
red.value(0)
timer=Timer()

def callbackLed(pin):
    led.toggle()

timer.init(period=2000, mode=Timer.PERIODIC, callback=callbackLed)

while(True):
    red.toggle()
    time.sleep(1)
    