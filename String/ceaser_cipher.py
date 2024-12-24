def new_string(mesg, key):
    new_key = key % 26
    new_mesg = ['']*len(mesg)
    for i in range(len(mesg)):
        letter_ascii = ord(mesg[i]) + new_key
        if letter_ascii <= 122:
            new_mesg[i] = chr(letter_ascii)
        else:
            new_mesg[i] = chr(96+(letter_ascii % 122))
    return ''.join(new_mesg)
    
mesg = input('enter the mesg:')
key = int(input('enter the key:'))
print('new mesg:',new_string(mesg,key))