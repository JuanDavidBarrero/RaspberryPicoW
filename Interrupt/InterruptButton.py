from machine import Pin
from time import sleep

status = False

def handle_interrupt(pin):
    led.toggle()
    global status
    status = True
    
led = Pin("LED", Pin.OUT)
button = Pin(2, Pin.IN)

button.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
    if status:
        print("interruption occurred")
        status = False
