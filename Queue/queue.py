class Node:
    next = None
    def __init__(self,data):
        self.data = data
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def enqueue(self,data):
        node = Node(data)
        if self.last is None:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        return
    def dequeue(self):
        if self.first is None:
            print('empty')
            return
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return
    def display(self):
        if self.last is None:
            print('empty')
            return
        temp = self.first
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        return
    
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()