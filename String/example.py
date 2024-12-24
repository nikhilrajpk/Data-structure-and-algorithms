# Ceaser cipher
# string = input('enter the mesg:')
# key = int(input('enter the key:'))
# new_key = key%26
# new_mesg = ['']*len(string)
# for i in range(len(string)):
#     new_char = ord(string[i]) + new_key
#     if new_char <= 122:
#         new_mesg[i] = chr(new_char)
#     else:
#         new_mesg[i] = chr(96 + (new_char%122))
# print(''.join(new_mesg))

#count of alphabet  aaabbc   3a2b1c
# string = input('enter the string:')
# ans = []
# current = 0
# while current < len(string):
#     next = current + 1
#     count = 1
#     while next < len(string) and string[current] == string[next]:
#         count += 1
#         next += 1
#     ans.append(str(count))
#     ans.append(string[current])
#     current = next
# print(''.join(ans))


#reverse
# string = input('enter the string:')
# new = []
# for i in range(len(string)-1,-1,-1):
#     new.append(string[i])
# print(''.join(new))

# import sys

# my_list = []
# print(f"Initial size: {sys.getsizeof(my_list)} bytes")

# for i in range(10):
#     my_list.append(i)
#     print(f"After appending {i+1} elements: {sys.getsizeof(my_list)} bytes")
