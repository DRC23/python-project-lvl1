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
        is_user_response_yes = num % 2 == 0 and user_num == 'yes'
        is_user_response_no = num % 2 == 1 and user_num == 'no'
        if is_user_response_yes or is_user_response_no:
            print('Correct')
            count += 1
        else:
            if user_num == 'yes':
                correct = 'no'
            else:
                correct = 'yes'
            print(f"'{user_num}' is wrong answer ;(. "
                  f"Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f"Congratulations, {name}!")
