import random
import string
import json

alphabet = '    ' + ' ' + string.punctuation + string.ascii_letters + string.digits

def genPassword(length, special='true'):
    simple_alphabet = string.ascii_letters + string.digits
    pwd = ""
    i = 0
    while i < length:
        if special == 'true':
            pwd += random.choice(alphabet)
        else:
            pwd += random.choice(simple_alphabet)
        i = i + 1
    return pwd
def vigenere(message, key, direction=1):
    key_index = 0
    encrypted_message = ''
    for char in message:
        key_char = key[key_index % len(key)]
        key_index += 1
        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset*direction) % len(alphabet)
        encrypted_message += alphabet[new_index]
    return encrypted_message

def decrypt(message, key):
    return vigenere(message, key, -1)
def encrypt(message, key):
    return vigenere(message, key)

def reader(pather):
    file = open(pather, 'r')
    returning = file.read()
    file.close()
    return returning
def writer(pather, elementer):
    file = open(pather, 'w')
    file.write(elementer)
    file.close()

def create_password(tab_password, master_password, pather):
    adder = input('\033[1;33mPassword to add : ')
    namer = input('\033[1;36mPassword name : ')
    tab_password.append({'name': encrypt(namer, master_password), 'pass': encrypt(adder, master_password)})
    print('\n\033[1;32mPassword added successfully !')
    writer(pather, json.dumps(tab_password))
def remove_password(pather, passer):
    element= json.loads(reader(pather))
    if len(element) != 1:
        i = 1
        while i < len(element):
            print(f'\033[1;32mPassword name n°{i} : ' + f'\033[1;35m{decrypt(element[i]['name'], passer)}')
            i += 1
        remove_this = input('\033[1;33mPassword to remove : ')
        element.pop(int(remove_this))
        writer(pather, json.dumps(element))
        print('\n\033[1;32mPassword removed successfully !\033[0m')
    else:
        print('This password group is empty !')

def create_file():
    tab_password = []
    pather = input('\033[1;33mName and file path  : ') + '.json'
    master_password = input('\033[1;36mMaster password : ')
    securiter = encrypt('yes', master_password)
    tab_password.append({'name': securiter})
    writer(pather, json.dumps(tab_password))
    print('\n\033[1;32mFile created successfully !')
def delete_file():
    print('delete file')

def find_password(passer, in_file):
    element= json.loads(in_file)
    i = 1
    while i < len(element):
        print(f'\033[1;32mPassword name n°{i} : ' + f'\033[1;35m{decrypt(element[i]['name'], passer)}')
        i += 1
    print(f'\n\033[1;32mPassword : \033[1;35m{decrypt(element[int(input('\033[1;33mPassword name number : '))]['pass'], passer)}')

def identify():
    path = input('\033[1;33mFile path : ')
    passer = input('\033[1;36mMaster password : ')
    in_file = reader(path)
    verify_pass = decrypt(json.loads(in_file)[0]['name'], passer)
    if verify_pass == 'yes':
        print('\n\033[1;32mAccess allowed')
        return [True, passer, path, json.loads(in_file)]
    else:
        print('\n\033[1;31mAccess denied : wrong master password !\033[0m')
        defaulter()

def defaulter():
    todo = input('\033[1;37mPS passwordManager>\033[1;90m ')
    if todo == 'create' or todo == 'ct':
        create_file()
        defaulter()
    elif todo == 'select' or todo =='slct':
        pather = input('\033[1;33mFile path : ')
        passer = input('\033[1;36mMaster password : ')
        in_file = reader(pather)
        verify_pass = decrypt(json.loads(in_file)[0]['name'], passer)
        if verify_pass == 'yes':
            find_password(passer, in_file)
            defaulter()
        else:
            print('\033[1;31mWrong master password !\033[0m')
            defaulter()
    elif todo == 'add':
        result = identify()
        if result[0] == True:
            create_password(result[3], result[1], result[2])
            defaulter()
    elif todo == 'remove' or todo == 'rm':
        result = identify()
        remove_password(result[2], result[1])
        defaulter()
    elif todo == 'delete':
        delete_file()
        defaulter()
    elif todo == 'gpwd' or todo == 'genpwd':
        print(f'\033[1;32mPassword generated : \033[1;35m{genPassword(int(input('\033[1;33mPassword length : ')), input('\033[1;36mAdd special characters [true/false] '))}\033[0m')
        defaulter()
    elif todo == 'help' or todo == 'h':
        print('\033[1;37m - create :\n    \033[1;90m    To create a password group (JSON file)')
        print('\033[1;37m - delete : \n\033[1;90m    To delete a password group')
        print('\033[1;37m - add :\n\033[1;90m    To add a password in a group')
        print('\033[1;37m - remove, rm :\n\033[1;90m    To remove a password in a group')
        print('\033[1;37m - select, slct :\n\033[90m    To get password in a group')
        print('\033[1;37m - gpwd, genpwd :\n\033[90m    To generate a password with a length')
        print('\033[1;37m - help, h :\n\033[1;90m    For help\033[0m')
        defaulter()
    elif todo == 'quit' or todo == 'exit' or todo == 'q':
        print('\033[0m')
    elif todo == '':
        defaulter()
    else:
        print(f'\033[1;31merror : \'{todo}\'\033[0m')
        defaulter()

defaulter()