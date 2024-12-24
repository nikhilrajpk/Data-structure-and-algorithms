from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        print( self.stack.pop())
    def peep(self):
        print(self.stack[-1])
    def is_empty(self):
        True if len(self.stack) == 0 else False
    def size(self):
        print(len(self.stack))
    def display(self):
        for i in self.stack:
            print(i,end=',')

s = Stack()
s.push(1)
s.push(2)
s.peep()
s.display()