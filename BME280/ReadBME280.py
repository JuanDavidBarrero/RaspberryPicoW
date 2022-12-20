from machine import Pin, I2C
import time
from bme280 import BME280

i2c = I2C(0,sda=Pin(20), scl=Pin(21), freq=400000)
bme280 = BME280(i2c=i2c,address=0x77)

while True:
    temp, pressure, hum = bme280.values
    print("--------------------")
    print(f"temperature: {temp}")
    print(f"pressure: {pressure}")
    print(f"humidity: {hum}")
    print("--------------------\n")
    time.sleep(1)