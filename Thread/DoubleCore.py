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

        
_thread.start_new_thread(HelloWorld,())

while True:
    led.toggle()
    sleep(0.1)

