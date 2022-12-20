from machine import UART, Pin
import time

Serial = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))
count = 0
dataRx = ''
dataTx = ''

while True:
    if (dataRx == b'9' or dataRx == b'19'):
        dataTx = f"hola mundo {count}"
    else: 
        dataTx = f"{count}"
        
    Serial.write(dataTx)  
    dataRx = Serial.readline()     
    print(dataRx)
    count = count +1
    time.sleep(0.2)