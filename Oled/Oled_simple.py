from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0,sda=Pin(20), scl=Pin(21), freq=400000)
oled = SSD1306_I2C(128, 32, i2c)

count = 0

while True:
    text = f"hola mundo {count}"
    oled.text(text, 10, 15)
    count += 1 
    oled.show()
    time.sleep(1)
    oled.fill(0)
    oled.show()