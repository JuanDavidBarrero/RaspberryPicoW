import network
import urequests as request
import time
from machine import Pin
import secrets

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

led = Pin("LED", Pin.OUT)

while( not(wlan.isconnected()) ):
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)
    
led.value(1)

response = request.get('https://reqres.in/api/users')

parsed = response.json()

for person in parsed["data"]:
    print(f"Hello {person["id"]} {person["first_name"]} {person["last_name"]}")