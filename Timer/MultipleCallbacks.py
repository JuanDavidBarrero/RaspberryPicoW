import machine
import time

class TimerCallback:
    def __init__(self):
        self.timers = []

    def add_function(self, function, tiempo, periodic):
        timer = machine.Timer()
        if periodic:
            timer.init(period=int(tiempo * 1000), mode=machine.Timer.PERIODIC, callback=lambda t: function())
        else:
            timer.init(period=int(tiempo * 1000), mode=machine.Timer.ONE_SHOT, callback=lambda t: function())
        self.timers.append((function, timer)) 

    def remove_function(self, funcion):
        for f, timer in self.timers:
            if f == funcion:
                timer.deinit()  
                self.timers.remove((f, timer))  

def function1():
    print("\tFunction 1 executed")

def function2():
    print("\t\tFunction 2 executed")

def function3():
    print("\t\t\tFunction 3 executed")

timer = TimerCallback()
timer.add_function(function1, 2, True)
timer.add_function(function2, 5, False)
timer.add_function(function3, 10, True)

counter = 0

while 1:
    print(f"hello world {counter}")
    counter +=1
    if (counter == 15):
        print("remove the function 3")
        timer.remove_function(function3)
    if (counter == 9):
        print("remove the function 1")
        timer.remove_function(function1)
    
    time.sleep(1)
