"""Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will serve the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']"""
from collections import deque
import time
import threading
class Queue:
    def __init__(self):
        self.que = deque()
    def enque(self,orders):
        self.length = len(orders)
        for order in orders:
            time.sleep(.5) 
            self.que.appendleft(order)
            print('new order : ',order)
    def deque(self):
        for i in range(self.length):
            time.sleep(2)
            print('serving the order : ',self.que.pop())
    
q = Queue()

orders = ['pizza','samosa','pasta','biryani','burger']

t1 = threading.Thread(target=q.enque, args=(orders,))
t2 = threading.Thread(target=q.deque)

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()