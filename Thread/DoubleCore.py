from machine import Pin
import _thread
from time import sleep

led = Pin("LED", Pin.OUT)

#sLock = _thread.allocate_lock()   #this is a semaphore 
#sLock.acquire()   #Take semaphore 
#sLock.release()   #Give semaphore 

def HelloWorld():
    count = 0
    while True:
        print(f"Hola mundo {count}")
        count +=1
        sleep(1)
        if count == 10:
            _thread.exit()

        
_thread.start_new_thread(HelloWorld,())

def main():
    while True:
        print("Hola desde el core 0")
        sleep(2)

contador = 0
while True:
    led.toggle()
    contador += 1
    sleep(0.1)
    if (contador == 100):
        main()
        

