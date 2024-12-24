"""_summary_
Program to replace the each character with the n th char by adding the key to the index.
Time complexity : O(n) for the loop and join operation. so dominant is taken.
Space complexity : O(n) for the mesg storing in s and join operation also returns n sized output.
"""
def replace_alphabet(string, key):
    new_key = key % len(string)
    s = ['']*len(string)
    for i in range(len(string)):
        pos = i + new_key
        if pos < len(string):
            s[i] = string[pos]
        else:
            s[i] = string[(pos%len(string))]
    return ''.join(s)

string = input('enter the string:')
key = int(input('enter the key:'))
print('string:',replace_alphabet(string,key))