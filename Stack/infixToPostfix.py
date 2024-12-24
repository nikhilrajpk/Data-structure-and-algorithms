from collections import deque
def precedence(op):
    if op in ('+','-'):
        return 1
    elif op in ('*','/'):
        return 2
    elif op == '^':
        return 3
    return 0
def is_operator(char):
    return char in {'+','-','*','/','^'}
def infix_to_postfix(expression):
    stack = deque()
    output = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

infix_expr = "A+B*(C^D-E)"
postfix_expr = infix_to_postfix(infix_expr)
print("Infix Expression:", infix_expr)
print("Postfix Expression:", postfix_expr)