#!/usr/bin/env python3
import prompt
import random


def gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')
    count = 0
    print('Find the greatest common divisor of given numbers.')
    while count != 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print('Question:', num1, num2)
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 %= num2
            else:
                num2 %= num1
        if num1 != 0:
            res = num1
        else:
            res = num2
        usr_num = input('Your answer: ')
        if usr_num.isdigit() and int(usr_num) == res:
            print('Correct!')
            count += 1
        else:
            print(f"'{usr_num}' is wrong answer ;(. "
                  "Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')
