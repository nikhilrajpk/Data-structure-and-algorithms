# def reverse(string):
#     s = [''] * len(string)
#     j = 0
#     for i in range(len(string)-1,-1,-1):
#         s[j] = string[i]
#         j += 1
#     return ''.join(s)

def reverse(string, s, j, i):
    if i == -1:
        return ''.join(s)
    s[j] = string[i]
    return reverse(string, s, j+1, i-1)

string = input('enter the string:')
s = ['']*len(string)
print(reverse(string, s, j = 0,i = len(string)-1))