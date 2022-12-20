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

url = "https://reqres.in/api/users/2"
 
headers = {"Content-Type": "application/json"}
 
data = { "name": "morpheus", "job": "warrior", "updatedAt": "2022-12-20T13:29:36.989Z" }
 
response = request.put(url, headers=headers, json=data)

if (response.status_code >= 200):
    parsed = response.json()
    print(f"User updated with name {parsed["name"]} and now with the job {parsed["job"]}")
else:
    print("Fail could not updated the user")
    

