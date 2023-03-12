import threading
import random
import time

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1
        self.arr = [None] * capacity
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, item):
        with self.not_full:
            while self.size == self.capacity:
                self.not_full.wait(timeout=1)
            with self.lock:
                self.rear = (self.rear + 1) % self.capacity
                self.arr[self.rear] = item
                self.size += 1
                self.not_empty.notify()

    def dequeue(self):
        with self.not_empty:
            while self.size == 0:
                self.not_empty.wait(timeout=1)
            with self.lock:
                item = self.arr[self.front]
                self.front = (self.front + 1) % self.capacity
                self.size -= 1
                self.not_full.notify()
                return item

class ProducerThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            num = random.randint(1, 10)
            time.sleep(num)
            self.queue.enqueue(num)

class ConsumerThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            num = random.randint(1, 10)
            time.sleep(num)
            item = self.queue.dequeue()
            print(item)

if __name__ == '__main__':
    q = Queue(5)
    producer = ProducerThread(q)
    consumer = ConsumerThread(q)
    producer.start()
    consumer.start()
