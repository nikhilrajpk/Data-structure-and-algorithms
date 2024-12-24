from collections import deque
# class Stack:
#     def __init__(self):
#         self.stack = deque()
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         print(self.stack.pop())
#     def peek(self):
#         print('element at the top:',self.stack[-1])
#     def isempty(self):
#         print(True) if len(self.stack) == 0 else print(False)
#     def display(self):
#         print('stack:',self.stack)
#     def reverse(self,string):
#         for i in string:
#             self.push(i)
#         self.display()
#         while self.stack:
#             print(self.pop())
        
            
# s = Stack()
# s.push(1)
# s.push(2)
# s.peek()
# s.pop()
# s.pop()
# s.isempty()
# s.display()
# print(s.valid_bracket('([]{}'))
# s.reverse('hai')


def reverse(string):
    stack = deque()
    for i in string:
        stack.append(i)
    print(stack)
    while stack:
        print(stack.pop())
    
reverse('hai')