import random


def game():
    user = input("Enter Rock (R), Paper(P) or Scissor(S): ")
    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return 'Its a tie!'
    elif (user == 'R'and computer == 'S') or (user == 'P' and computer == 'R') or (user == 'S' and computer == 'P'):
        return f'You won! Computer chose {computer}.'
    else:
        return f'You lost! Computer chose {computer}.'


print(game())
