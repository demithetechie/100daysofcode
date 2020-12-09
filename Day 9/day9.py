print("Welcome to the secret auction program.")
biddings = {} # empty dictionary
isFinished = False # to check if biddings are over

while not isFinished:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  moreBidders = input("Are there any other bidders? Type 'yes' or 'no' ")
  if moreBidders == "no":
    isFinished = True
    break
  biddings[name] = bid
  clear()

highest = 0
name = ""
for person in biddings:
  if biddings[person] > highest:
    highest = biddings[person]
    name = person

print(f"The highest bidder was {name} with ${biddings[name]}")