import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    value = get_voltage(analog_in)
    print(f"the voltage is {value}")
    time.sleep(0.1)