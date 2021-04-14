from art import logo
import random as r

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
isPlaying = False

def createUserHand():
  """creates user hand"""
  userHand = []
  userHand.append(r.choice(cards))
  userHand.append(r.choice(cards))
  return userHand

def createCPUHand():
  """creates cpu hand"""
  cpuHand = []
  cpuHand.append(r.choice(cards))
  cpuHand.append(r.choice(cards))
  return cpuHand

def newCard(userHand):
  """adds new card to user hand"""
  userHand.append(r.choice(cards))
  return userHand

game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if game == "y":
  isPlaying = True
  print(logo)
elif game == "n":
  isPlaying = False

while isPlaying == True: 
  userHand = createUserHand()
  cpuHand = createCPUHand()

  userTotal = sum(userHand)
  cpuTotal = sum(cpuHand)
  blackJack = False

  while not blackJack:
    print(f"Your cards: {userHand}, current score: {userTotal}")
    print(f"Computer's first hand: {cpuHand[0]}")
    card = input("Type 'y' to get another card, type 'n' to pass: ")
      
    if card == "y":
      userHand = newCard(userHand)
      userTotal = sum(userHand)
    elif card == "n": 
      blackJack = True

    if userTotal > 21 or cpuTotal > 21:
      blackJack = True

  userClose = 21 - userTotal 
  cpuClose = 21 - cpuTotal

  if userTotal > 21 and cpuTotal > 21:
    print(f"Your final hand: {userHand}, final score: {userTotal}")
    print(f"Computer's final hand: {cpuHand}, final score: {cpuTotal}")
    print("Push!")
  elif userTotal > 21:
    print(f"Your final hand: {userHand}, final score: {userTotal}")
    print(f"Computer's final hand: {cpuHand}, final score: {cpuTotal}")
    print("You lose!")
  elif cpuTotal > 21:
    print(f"Your final hand: {userHand}, final score: {userTotal}")
    print(f"Computer's final hand: {cpuHand}, final score: {cpuTotal}")
    print("You win!")
  elif userClose == cpuClose:
    print(f"Your final hand: {userHand}, final score: {userTotal}")
    print(f"Computer's final hand: {cpuHand}, final score: {cpuTotal}")
    print("Push!")
  elif userClose < cpuClose:
    print(f"Your final hand: {userHand}, final score: {userTotal}")
    print(f"Computer's final hand: {cpuHand}, final score: {cpuTotal}")
    print("You win!")
  elif cpuClose < userClose:
    print(f"Your final hand: {userHand}, final score: {userTotal}")
    print(f"Computer's final hand: {cpuHand}, final score: {cpuTotal}")
    print("You lose!")

  game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

  if game == "y":
    isPlaying = True
    clear()
  elif game == "n":
    isPlaying = False