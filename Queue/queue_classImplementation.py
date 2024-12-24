from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self,data):
        self.queue.appendleft(data)
    def dequeue(self):
        print('first element : ',self.queue.pop())
    def is_empty(self):
        print(True) if len(self.queue) == 0 else print(False)
    def size(self):
        print('size of the queue:',len(self.queue))
    def display(self):
        print('queue : ')
        for i in self.queue:
            print(i,end=' ')
        
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.size()
q.display()
