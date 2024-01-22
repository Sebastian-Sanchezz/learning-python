import string

letter = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789!@#$%^&*()_+{}[]'

def go_program():
    option =  input('Input 1 for encriptation or 2 for descriptation: ')
    if option == '1':
        print(encriptation())
    elif option == '2':
        print(descriptation())
    else:
        print('Invalid option')

def encriptation():
    message = input('Enter the message: ')
    dict_e = dict(zip(letter,number))
    message_encripted = [dict_e[text] for text in message]
    return "".join(message_encripted)

def descriptation():
    message = input('Enter the message: ')
    dict_d = dict(zip(number,letter))
    message_descripted = [dict_d[text] for text in message]
    return "".join(message_descripted)

go_program()