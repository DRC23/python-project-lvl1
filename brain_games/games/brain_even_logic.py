#!/usr/bin/env python3
from random import randint
import prompt


def parity_check():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 3:
        num = randint(1, 100)
        print('Question:', num)
        user_num = input('Your answer: ')
        if (num % 2 == 0 and user_num == 'yes') or (num % 2 == 1 and user_num == 'no'):
            print('Correct')
            count += 1
        else:
            if user_num == 'yes':
                correct = 'no'
            else:
                correct = 'yes'
            print("'{}' is wrong answer ;(. Correct answer was '{}'".format(user_num, correct))
            return None
    print('Congratulations, {}!'.format(name))
