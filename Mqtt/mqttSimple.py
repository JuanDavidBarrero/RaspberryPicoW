import network
import urequests as request
from umqtt import MQTTClient
import time
from machine import Pin
import ujson as json
import random
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

print(f"connected ip {wlan.ifconfig()}")
led.value(1)

mqtt_server = 'ip_server'
client_id = 'juan154254'
topic_pub = b'hola/mundo'
topic_sub = b'test/topic'

def sub_callback(topic, msg):
    #print((topic, msg.decode()))
    parsed =json.loads(msg.decode())
    print(f"the name is {parsed["nombre"]} and his pet is {parsed["mascota"]}")

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, port=1883,keepalive=3600)
    client.set_callback(sub_callback)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()


try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
        myDict = {'name':'Juan', 'age':24, 'skills':["C++","Python"], 'random':random.randint(0,10)}
        jsonStr = json.dumps(myDict)
        client.publish(topic_pub, jsonStr)
        client.check_msg()
        time.sleep(3)