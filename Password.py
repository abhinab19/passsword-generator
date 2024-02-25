import random

print('Welcome to password generator')


chars = 'abcdefghijklmnopqwxyzABCDEFGHIJKLMNOPQWXYZ!@#$%^&*(),.0123456789'


number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Input length of your password: ')
length = int(length)

print('\nhere is your password:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)    


