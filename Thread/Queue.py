import heapq as queue

class MyQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def push(self, item):
        self.counter += 1
        queue.heappush(self.heap, (self.counter, item))

    def pop(self):
        if not self.heap:
            return -1
        _, item = queue.heappop(self.heap)
        return item
    
    def has_items(self):
        return len(self.heap) > 0


