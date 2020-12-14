# Number Guessing Game
# With 2 modes: Easy and Hard
import random
from art import logo

def randomnumber():
  number = random.randint(0,101)
  return number

print(logo)
num = randomnumber()
guesses = 0
userGuess = 0
numberGuessed = False

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 0 and 100...")
print(f"Debugging: the number is {num}")
mode = input("Choose a mode: easy 'e' or hard 'h': ")

if mode == 'e':
  guesses = 10
elif mode == 'h':
  guesses = 5

while not numberGuessed:
  print(f"You have {guesses} attempts to guess the number")
  userGuess = int(input("Make a guess: "))

  if userGuess == num:
    print("Well done, you guessed the number!!")
    numberGuessed = True
  elif userGuess > num:
    print("Too high.")
    guesses -= 1
  elif userGuess < num:
    print("Too low.")
    guesses -= 1

  if guesses == 0:
    print("You've run out of guesses you lose")
    break