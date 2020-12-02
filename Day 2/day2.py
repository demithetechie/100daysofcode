print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip /= 100
tip += 1

price = (total/people) * tip
price = round(price, 2)
print(f"Each person should pay ${price}")