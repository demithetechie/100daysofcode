def add(n1, n2):
  """ Adds 2 integers together and returns the output """
  print(f"{n1} + {n2} = {n1 + n2}")
  return n1 + n2

def sub(n1, n2):
  """ Subtracts 2 integers and returns the output """
  print(f"{n1} - {n2} = {n1 - n2}")
  return n1 - n2

def multi(n1, n2):
  """ Multiplies 2 integers together and returns the output """
  print(f"{n1} * {n2} = {n1 * n2}")
  return n1 * n2

def divide(n1, n2):
  """ Divides 2 integers together and returns the output as a float """
  print(f"{n1} / {n2} = {n1 / n2}")
  return float(n1/n2)

operators = {
  "+": add, 
  "-": sub,
  "*": multi,
  "/": divide
  }

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

for key in operators:
  print(key)
  
choice = input("Which operator do you want? ")

function = operators[choice]
answer = function(num1, num2)

calcContinue = input("Would you like to continue with your calculation? Press 'y' for yes or 'n' for no: ")

while calcContinue == "y":
  num3 = int(input("What is the next number? "))

  for key in operators:
    print(key)
  
  choice = input("Which operator do you want? ")

  function = operators[choice]
  answer = function(answer, num3)

  calcContinue = input("Would you like to continue with your calculation? Press 'y' for yes or 'n' for no: ")

