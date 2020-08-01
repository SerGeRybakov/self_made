"""Rock, scissors, paper"""

import random

dic = {
    1: 'rock',
    2: 'scissors',
    3: 'paper'
}

total_score = int(input('Enter the goal to score: '))
comp_score = 0
player_score = 0
rnd = 1
print(f'\n'
      f'Playing till {total_score}. Comp:{comp_score}. You: {player_score}.'
      f'\nLet\'s start!'
      f'\n')
while comp_score < total_score and player_score < total_score:
    print(f'Round {rnd}')

    player_action = int(input('Print "1" for rock, "2" for scissors or "3" for paper: '))
    while player_action not in dic.keys():
        print('\nWrong choice!')
        player_action = int(input('Print "1" for rock, "2" for scissors or "3" for paper: '))
    else:
        player_action = dic[player_action]
        rd = random.randint(1, 3)
        comp_action = dic[rd]
        print(f'You hit "{player_action}" vs. "{comp_action}" Comp\'s hit.')

        if player_action == comp_action:
            player_score += 0.5
            comp_score += 0.5
            print('Deuce. Hit again!')
        elif player_action == dic[1] and comp_action == dic[2]:
            player_score += 1
            print('You win. Rock beats scissors.')
        elif player_action == dic[2] and comp_action == dic[3]:
            player_score += 1
            print('You win. Scissors beat paper.')
        elif player_action == dic[3] and comp_action == dic[1]:
            player_score += 1
            print('You win. Paper beats rock.')
        elif comp_action == dic[1] and player_action == dic[2]:
            comp_score += 1
            print('You lose. Rock beats scissors.')
        elif comp_action == dic[2] and player_action == dic[3]:
            comp_score += 1
            print('You lose. Scissors beat paper.')
        elif comp_action == dic[3] and player_action == dic[1]:
            comp_score += 1
            print('You lose. Paper beats rock.')
    rnd += 1
    print(f'\nComp: {comp_score}. You: {player_score}.\nPlaying till {total_score}.')
    print()

else:
    if player_score > comp_score:
        print('\nVICTORY!!! You are the champion!!!\n')
    elif player_score == comp_score:
        print('\nDEUCE!!! You\'re not good enough still!!!\n')
    else:
        print('\nHA-HA-HA!!! You\'re a loser!!!\n')

print(input('Press any key for exit'))
