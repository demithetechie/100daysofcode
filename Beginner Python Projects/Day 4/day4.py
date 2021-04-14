import random

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

choice = int(input("What do you choose? Press 0 for Rock, 1 for Paper or 2 for Scissors"))

cpu_choice = random.randint(0, 2)

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)

print("Computer chose:")

if cpu_choice == 0:
  print(rock)
elif cpu_choice == 1:
  print(paper)
elif cpu_choice == 2:
  print(scissors)

if choice == 0 and cpu_choice == 2:
  print("You win!")
elif choice == 0 and cpu_choice == 0:
  print("It's a draw.")
elif choice == 0 and cpu_choice == 1:
  print("You lose.")
elif choice == 1 and cpu_choice == 0:
  print("You win!")
elif choice == 1 and cpu_choice == 1:
  print("It's a draw.")
elif choice == 1 and cpu_choice == 2:
  print("You lose.")
elif choice == 2 and cpu_choice == 1:
  print("You win!")
elif choice == 2 and cpu_choice == 2:
  print("It's a draw.")
elif choice == 2 and cpu_choice == 0:
  print("You lose.")