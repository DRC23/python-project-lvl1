#!/usr/bin/env python3
import prompt
import random


def prime():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != 3:
        
        print('Question:', num)
        usr_answer = input('Your answer: ')
        if usr_answer == 'yes':
            print('Correct!')
            count += 1
        else:
            print(f"'{usr_num}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')
    
