import string
import json

alphabet = '    ' + ' ' + string.punctuation + string.ascii_letters + string.digits

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
def create_password(tab_password):
    adder = input('\033[1;33mPassword to add : ')
    namer = input('\033[1;36mPassword name : ')
    tab_password.append({'name': encrypt(namer, master_password), 'pass': encrypt(adder, master_password)})
    file = open(pather, 'w')
    file.write(json.dumps(tab_password))
    file.close()
    if input('\033[1;34mAdd new password ? [y/n] \033[0m') == 'y':
        create_password(tab_password)
    return tab_password
def find_password(passer, in_file):
    element= json.loads(in_file)
    i = 1
    while i < len(element):
        print(f'\033[1;32mPassword name n°{i} : ' + f'\033[1;35m{decrypt(element[i]['name'], passer)}')
        i += 1
    print(f'\033[1;32mPassword : \033[1;35m{decrypt(element[int(input('\033[1;33mPassword name number : '))]['pass'], passer)}')
    if input('\033[1;34mFind other password ? [y/n] \033[0m') == 'y':
        find_password(passer, in_file)
    return
    
todo = input('\033[1;34mCreate or select passwordGroup ? [c/s] \033[0m')
if todo == 'c':
    tab_password = []
    pather = input('\033[1;33mName and file path  : ') + '.json'
    file = open(pather, 'w')
    master_password = input('\033[1;36mMaster password : ')
    securiter = encrypt('yes', master_password)
    tab_password.append({'name': securiter})
    file.write(json.dumps(tab_password))
    file.close()
    if input('\033[1;34mAdd new password ? [y/n] \033[0m') == 'y':
        create_password(tab_password)
    else:
        print('\033[1;32mRegistred !\033[1;0m')
elif todo == 's':
    file = open(input('\033[1;33mFile path : '), 'r')
    passer = input('\033[1;36mMaster password : ')
    in_file = file.read()
    verify_pass = decrypt(json.loads(in_file)[0]['name'], passer)
    if verify_pass == 'yes':
        find_password(passer, in_file)
    else:
        print('\033[1;31mWrong master password !\033[0m')
else:
    print(f'\033[1;31merror : \'{todo}\'\033[0m')