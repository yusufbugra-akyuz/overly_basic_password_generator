import random

print('Welcome To Password Generator')

chars = 'abcdefghijklmnoprqstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZé!^+%&/()=?_>£#${[]}|@~ß´×µ”“„<>1234567890*-'

number = int(input('Amount of passwords to generate:'+" "))

length = int(input('Your password length'+" "))

print (f'here are your passwords:')

for passwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)