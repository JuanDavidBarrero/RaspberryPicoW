import time
import board
import pwmio
from analogio import AnalogIn


led = pwmio.PWMOut(board.GP10, frequency=5000, duty_cycle=0)
Pot = AnalogIn(board.A0)

def voltage(value):
    return value * 3.3 /65536

while True:
    value = Pot.value
    led.duty_cycle = value
    print(f"The volage in the led is {voltage(value)}")
    time.sleep(0.1)
   