import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup.
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT


switch = DigitalInOut(board.GP10)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN

while True:
    if switch.value:
        led.value = False
    else:
        led.value = True
    print(switch.value)
    time.sleep(0.01)  # debounce delay
