import json
import time
import os
import random

class DataHandler:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            with open('datos.json', 'r') as file:
                loaded_data = json.load(file)
                if isinstance(loaded_data, list):
                    return loaded_data
        except:
            pass
        return []

    def save_data(self):
        with open('datos.json', 'w') as file:
            json.dump(self.data, file)

    def remove_last_data(self):
        if self.data:
            self.data.pop()

    def add_data(self, new_item):
        self.data.append(new_item)
        self.save_data()
        print(f"Added a new item: {new_item}")

    def read_data(self):
        if self.data:
            last_value = self.data[-1]
            self.remove_last_data()
            self.save_data()
            return last_value
        else:
            print("No data in the queue.")
            return None

# Create an instance of the DataHandler class
data_handler = DataHandler()

ep10 = time.time()
ep2 = time.time()

while True:
    if time.time() - ep10 > 100:
        last_value = data_handler.read_data()
        if last_value:
            print(f"Last value: {last_value}")
        ep10 = time.time()

    if time.time() - ep2 > 1:
        new_item = {
            "num": random.randint(1, 100),
            "num2": random.randint(1, 100)
        }
        data_handler.add_data(new_item)
        ep2 = time.time()
