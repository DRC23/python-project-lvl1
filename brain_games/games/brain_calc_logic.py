#!/usr/bin/env python3
import prompt
import random


def calc():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')
    count = 0
    print('What is the result of the expression?')
    operator = ['-', '+', '*']
    while count != 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        sign = random.sample(operator, 1)
        temp = str(num1) + ' ' + ''.join(sign) + ' ' + str(num2)
        num = eval(temp)
        print('Question:', temp)
        usr_num = input('Your answer: ')
        if usr_num.isdigit() and int(usr_num) == num:
            print('Correct!')
            count += 1
        else:
            print(f"'{usr_num}' is wrong answer ;(. "
                  "Correct answer was '{num}'.")
            print("Let's try again, {}!".format(name))
            return None
    print('Congratulations, {}!'.format(name))
