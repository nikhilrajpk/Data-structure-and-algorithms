class Node:
    next = None
    def __init__(self,data):
        self.data = data
class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        return
    def pop(self):
        if self.top is None:
            print('empty')
            return
        self.top = self.top.next
        return
    
    def display(self):
        if self.top is None:
            print('empty')
            return
        temp = self.top
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        return
            
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.display()