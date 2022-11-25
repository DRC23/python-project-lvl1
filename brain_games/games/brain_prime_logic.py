#!/usr/bin/env python3
import prompt
import random


def is_prime(num):
    flag = True
    if num > 3 and num % 2 != 0:
        stop = num // 2 + 1
        for i in range(3, stop, 2):
            if num % i == 0:
                flag = False
                return flag
        return flag
    elif num > 3 and num % 2 == 0:
        flag = False
        return flag
    else:
        return flag


def prime():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')

    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != 3:
        number_random = random.randint(4, 100)
        flag = is_prime(number_random)
        print('Question:', number_random)
        usr_ans = input("Your answer: ")
        if (usr_ans == 'yes' and flag) or (usr_ans == 'no' and not flag):
            print("Correct!")
            count += 1
        else:
            if flag:
                right_ans = 'yes'
            else:
                right_ans = 'no'
            print(f"'{usr_ans}' is wrong answer ;(. "
                  f"Correct answer was '{right_ans}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f"Congratulations, {name}!")
