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

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

systemInput = random.randint(0,len(choices))

if userInput == 0 and systemInput == 2 or userInput == 1 and systemInput == 0 or userInput == 2 and systemInput == 1:
  print(f"You\'re choice: {choices[userInput]}\n")
  print(f"Computer\'s choice: {choices[systemInput]}\n")
  print("You Win.")
elif userInput == 0 and systemInput == 1 or userInput == 1 and systemInput == 2 or userInput == 2 and systemInput == 0:
  print(f"You\'re choice: {choices[userInput]}\n")
  print(f"Computer\'s choice: {choices[systemInput]}\n")
  print("You Lose.")
else:
  print("Draw.")