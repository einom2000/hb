# Guess the Number!

from random import *

secret_number = randint(10000, 99999)
print('I got a secret number! Can you guess what it is? ')

bingo = False
score = 90000

while not bingo:
    number = input('please guess: ')
    if len(number) == 5 and number.isdigit():
        number = int(number)
        if number > secret_number:
            print('Your guess is too big!')
            print('pls try again!')
            score -= 1
        elif number < secret_number:
            print('Your guess is too small!')
            print('pls try again!')
            score -= 1
        else:
            print('Bingo!')
            bingo = True

print('My secret number is: ', secret_number)
if score < 0:
    score = 0
print('Your score is ', score // 90)
