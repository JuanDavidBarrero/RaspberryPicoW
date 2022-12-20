from machine import Pin, ADC, PWM
from time import sleep

pot = ADC(Pin(26))
frequency = 5000
led = PWM(Pin(2))
led.freq(frequency)
led.duty_u16(0)

while True:
    pot_value = pot.read_u16()
    led.duty_u16(pot_value)
    
    