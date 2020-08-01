"""Guess number - a small game"""

import random as rd

possible_min = 1
possible_max = 100

level = {
    '1': 3,
    '2': 5,
    '3': 10
}

actions = '<', '>', '='

chosen_level = 0
count = 0
while chosen_level not in level:
    chosen_level = input('Select difficulty: 1 - hard, 2 - medium, 3 - easy: ')
    print()
    if chosen_level not in level:
        print('No such level. Try again.')
    else:
        count = level[chosen_level]
        break

attempts = 1
suggested_num = rd.randint(possible_min, possible_max)
print(f"Attempt № {attempts} of {count}.\nI think it's {suggested_num}.")
told_action = input(f'Is suggested number lower (<) or bigger (>) than yours or it equals (=) it? ')
print()

try:
    while attempts < count:
        while told_action not in actions:
            print('Your answer is out of range. Try again.')
            told_action = input(f'Is suggested number lower (<) or bigger (>) than yours or it equals (=) it? ')
            print()
        else:
            if told_action == '=':
                print("\n============\nComp won!!!\nGAME OVER\n============")
                break
            elif told_action == '<':
                possible_min = suggested_num + 1
            elif told_action == '>':
                possible_max = suggested_num - 1
            else:
                print("============\nComp lost!!!\nGAME OVER\n============")
            suggested_num = rd.randint(possible_min, possible_max)
            attempts += 1
            print(f"Attempt № {attempts} of {count}.\nI think it's {suggested_num}.")
            told_action = input(f'Is suggested number lower (<) or bigger (>) than yours or it equals (=) it? ')
            print()
    else:
        if told_action == '=':
            print("\n============\nComp won!!!\nGAME OVER\n============")
        else:
            print("============\nComp lost!!!\nGAME OVER\n============")
except ValueError:
    print("============\nYou are f****ng cheater!!!\nGet outta here! \nGAME OVER\n============")

print(input('Press any key for exit'))
