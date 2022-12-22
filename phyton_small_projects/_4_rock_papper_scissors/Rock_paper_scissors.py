rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

table = [rock, paper, scissors]
computer_move = random.randint(0, 2)
user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_move > 2 or user_move < 0:
    print("You typed an invalid number, you lose!")
else:
    print(table[user_move])

    print(f"Computer choose:")
    print(table[computer_move])

    if user_move == 0 and computer_move == 2:
        print("You win!")
    elif computer_move == 0 and user_move == 2:
        print("You lose!")
    elif computer_move > user_move:
        print("You lose!")
    elif computer_move < user_move:
        print("You win!")
    elif computer_move == user_move:
        print("It's a draw!")