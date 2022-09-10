#!/usr/bin/env python3
import prompt
import random


def progression():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')
    count = 0
    print('What number is missing in the progression?')
    while count != 3:
        start_num = random.randint(1, 11)
        step = random.randint(1, 10)
        del_num = random.randint(1, 10)
        stop = start_num + step * 10
        temp = list(range(start_num, stop, step))
        print('Question:', *temp[: del_num - 1], '..', *temp[del_num:])
        usr_num = input('Your answer: ')
        if usr_num.isdigit() and int(usr_num) == temp[del_num - 1]:
            print('Correct!')
            count += 1
        else:
            print(f"'{usr_num}' is wrong answer ;(. Correct answer was '{temp[del_num-1]}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')
    
