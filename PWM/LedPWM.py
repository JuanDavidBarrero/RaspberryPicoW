from machine import Pin, PWM
from time import sleep

frequency = 5000
led = PWM(Pin(2))
led.freq(frequency)
led.duty_u16(0)

while True:
    for duty_cycle in range(0, 65535,100):
        led.duty_u16(duty_cycle)
        print(duty_cycle)
        sleep(0.005)
        
    for duty_cycle in range(65535, 0,-100):
        led.duty_u16(duty_cycle)
        print(duty_cycle)
        sleep(0.005)
    