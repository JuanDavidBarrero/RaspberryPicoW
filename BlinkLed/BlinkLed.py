from machine import Pin
import time

led_1 = Pin("LED", Pin.OUT)
while True:
    # Paso 4
    led_1.value(1)
    time.sleep(1)
    led_1.value(0)
    time.sleep(1)