class Node:
    next = None
    def __init__(self,data):
        self.data = data
class Queue:
    def __init__(self):
        self.left = None
        self.right = None
    def enqueue(self,data):
        node = Node(data)
        if self.right is None:
            self.left = node 
            self.right = node
        else:
            self.right.next = node
            self.right = node
    def dequeue(self):
        print('removing',self.left.data)
        self.left = self.left.next
        if self.left is None:
            self.right = None
    def display(self):
        if self.right is None:
            print('empty')
            return
        temp = self.left
        while temp:
            print(temp.data)
            temp = temp.next
            
            
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.display()