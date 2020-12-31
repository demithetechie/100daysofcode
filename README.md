# 👩🏾‍💻100 days of code👩🏾‍💻

I will be starting the 100 days of code challenge with Python. Updates will be placed here daily from 1st December.
Proposed finish date: 11th March 2021

# Day 1 - Printing, Variables, Strings

Challenge: Band Name Generator

Use \n for a newline.

# Day 2 - Data Types (Strings, Integers, Floats and Booleans), Mathematical Operations, String and Number Manipulation, F strings

Challenge: Tip Calculator

Using indexes on strings to reference a character of a string. Strings can be added together to form longer strings.

```python
print("Hello"[0])
print("Hello"[4])
print("Hello"[-1])
```
The first print will return "H", the second will return "o" and the third will also return "o". An index of -1 always returns the last index of a string. This is very useful where you do not know the length of the string. An index of 0 always returns the first index of a string.

You can use _ in place of , when writing large numbers. Both numbers below are read the same way in Python.

```python
123456789
123_456_789 
```
Use `type()` function to return the data type of a variable. Exponents in Python are accomplished using the ** operator. The function `round()` rounds a float to the nearest whole number. It can take an additional parameter of how many decimal points the float should be rounded to. Floor division (division without the remainder) can be accomplished with the // operator. Modulus (the remainder of a division) can be accomplished with the % operator. `+=, -=, /= and *=` manipulate integer/float values by its previous value. 

F strings (formatted strings) are ways to embed expressions into a string using minimal syntax:

```python
score = 0
print(f"Your score is {score}")
```
Curly brackets are used to refer to a variable. The f must be writted before the string, to indicate to python that this is a f string.

# Day 3 - Conditional Statements, Logical Operators, Code Blocks and Scope

Challenge: Treasure Island

Use logical operators `and, or, not` to validate expressions in Python.

# Day 4 - Randomisation and Python Lists

Challenge: Rock, Paper, Scissors

Computers are deterministic, which means that they perform actions in a predictable way. The python random library uses a pseudorandom number generator. 

https://www.askpython.com/ = very good for finding out more about python modules, libraries and documentation.

A module is another file of code that can be used in your code. You can create additional modules in python by simply creating a new python file and referring to that file in the main python file by using `import filename`.

```python
# my_module file
pi = 3.14159

# main file
import my_module

print(my_module.pi)
```
This code will print `3.14159` to the console.

A list is a type of **data structure** (a data structure being a method to organise, store and represent data in code).
In python, lists are defined using square brackets:

```python
mylist = [item1, item2, item3]
```
Lists have order, meaning that you can use indexes to refer to an item in a list (similar to how individual characters can be referenced in a string)

# Day 5 - For loops, Range and Code Blocks

Challenge: Password Generator

Research the functions under the random module e.g. `shuffle()` and `choice()`

```python
my_list = ["name", "age", "surname"]
for name in my_list:
  print(name)
```
This will print:

```python
name
age
surname
```

# Day 6 - Functions, Code Blocks and While Loops

Challenge: Escaping the maze - using Karel

Most of the coding for this project was done on this website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Day 7 - Hangman project

Today is dedicated solely for the hangman project.

Link to view: https://repl.it/@DemiladeOshin/Day-7-Hangman-5-Start

# Day 8 - Functions and Inputs

Challenge: Caesar Cipher

Parameters are the name of the variable that the function deals with. Arguments are the raw value assigned to the parameter. 

A **positional argument** is when the arguments are assigned to the variables by their position in the function definition.

A **keyword argument** is when the keywords are used to assign values to specific variables when the funciton is called, meaning that the position of the value in the function definition doesn't matter.

```python
# positional
my_function(1, 2, 3)
# keyword
my_function(a=1, b=2, c=3)
```
# Day 9 - Dictionaries and Nesting

Challenge: Secret Auction Program

Important notes: A **dictionary** is a set of key:value pairs, where the key is unique for every item in the dictionary. In other languages, dictionaries are known as "associative arrays" or "associative memories". Dictionaries are an inbuilt data structure in python, and they are indexed with keys.

Dictionaries in python are initiated with curly brackets, and each item is seperated with commas:

```python
my_dictionary = {
  "Jack": "18", 
  "Bob": "19", 
  "James": "20"
}

print(my_dictionary["Jack"]) # This prints out 18

my_dictionary["Joe"] = "20" # This adds another item to the dictionary

del my_dictionary["Jack"] # This deletes the item "Jack" from the dictionary

print(my_dictionary) # When this is run, the dictionary will only have 3 items: Bob, James and Joe

my_dictionary["Bob"] = "24" # This reassigns "Bob" to "24"

for item in my_dictionary:
  print(item) # This prints out all the keys in the dictionary

```

### Nesting

Nesting helps us create more complex data structures, and it allows us to store more than one value per key.

```python
#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
}
```

# Day 10 - Functions and Outputs

Challenge: Calculator program

**Docstrings** are ways to create documentation for the functions that we write. This helps other programmers know what our functions are doing, and it also reminds us the purpose of a given function. To declare a docstring, you use three double quotes `""" docstring goes here """`.

You can use command + / to comment multiple lines at once (or control + / for Windows). You can also use docstrings outside of functions as multi-line comments.

# Day 11 - Blackjack Project

Coding a blackjack game in Python.
Code can be found in the day 11 folder

# Day 12 - Scope

Challenge: Number Guessing Game

Local and Global Scope

Local variables are defined within functions. They cannot be used outside of that function, it is only valid within the function.
Global variables can be used throughout the program and they can be used in functions as well. There are defined outside of functions.
Anything that you name in code, is known as a namespace.

There is no block scope in Python. Variables defined within an if block etc an be used throughout the program.

You can use the term `global` to refer to variables created in global scope. However, you should avoid modifying global variables as it is not good coding practice and it is prone to errors.

# Day 13 - Debugging practice

No challenge for today.

# Day 14 - Higher Lower Project

Completing the higher lower project.

# Day 15 - Intermediate🎉 - Local Development Environment Setup

Using PyCharm:

PyCharm has various features including:  

**Spell Check** - This spell checks the words you are typing, so that you don't have unneseccary spelling errors in your code.  

**More Space** - PyCharm allows for more files to code with. You can also split screen by right clicking on the file and pressing "Split to right" or "Split to left". 

**Built In Linter** - This picks out bits of code and lets you know if you are writing in the correct style of coding. PEP 8 is the style used in PyCharm. Helps you improve the way you code in python.  

**Local History** - This allows you to see changes to the code. You can go back to the last 12 hours to figure out what you were coding beforehand. Use the show history tab to view local history.  

**View Structure of code** - This allows you to see all the functions and variables declared in your code. You can use the structure pane to view how you code is organised.  

**Refactor** - Allows you to rename functions without changing every occurence of the function

# Day 16 - Introduction to Object Oriented Programming

Challenge: Coffee Machine using OOP

**OOP** is based on objects and it helps to simplify real world problems into code. It makes use of polymorphism, inheritance and more to manipulate data related to objects. Objects have methods and attributes (public and private class). Attributes are private and methods are public. Attributes can only be modified by functions.

An attribute is a way to store data about an object. A method allows us to manipulate attributes. Methods are functions that objects can perform.

OOP has classes and objects. A class is a template for creating objects, and it includes the methods and attributes of the object. An object is an instantiation of a class (class instantiation). The object is what is manipulated by the program.

PyPI has a collection of various packages that other developers have created for people to use in their own code. Code reusability is important when developing new functions and procedures.

# Day 17 - The quiz project and benefits of OOP

Creating classes in python requires the following syntax:
```python
class ClassName
```

Creating attributes in python:

```python
def __init__(self, name, age):
      self.name = name
      self.age = age
```
Method are created as new functions. All methods need to have the self parameter.

# Day 18 - Turle graphics, tuples and importing modules

A **tuple** is a data structure in python, which is created using parathesis. Tuple values cannot be changed, they are immutable. Tuples are useful for data that you do not want to change. They can also act as keys in python dictionaries.

# Day 19 - More Turtle Graphics, Event listeners, State and multiple instances

Building a turtle racing game using multiple instances of the turtle class. 

Documentation is a description of all the possible functions that a library can perform. Documentation is useful because it helps us find out which functions we can use with certain libraries. Documentation also includes what the parameters of each function are, and what data type the result will be after the function has been executed.

It's good to check out the documentation of the library that you want to use, and to have a look at the functions that can be performed. Most of the time, you will be going back and forth between the documentation and your own code, which is perfectly fine. 

The idea is not to memorise all the functions, but to be able to use them when you need them.

# Day 20 - Build the snake game Part 1 - Animation and Control

The snake game makes use of an array of python turtles, which all follow the head of the snake. This means that controlling movement with the snake is simple, as each segment of the snake follows the head, so only the head needs to change direction each time.

The snake game is being coded with 3 seperate files alongside the main.py file, to make the code more reusable and effective. Using OOP with python turtle is helpful to manage the attributes and methods of the snake.

# Day 21 - Build the snake game Part 2 - Inheritance and List Slicing

Use `super()` to inherit a previous class.

```python
Class Fish(Animal):
  def __init__(self):
    super().__init__()
```
List slicing is done using colons:

```python
mylist[2:5] # returns the 3rd, 4th and 5th item in the list
mylist[2:] # returns everything after the 2nd item in the list
mylist[:3] # returns the last 3 items in the list
mylist[2:6:2] # returns every 2nd item between the 2th item and the 6th item (3rd and 5th item)
```
# Day 22 - Build Pong: Famous Arcade Game

Creating various instances of an object, detecting collisions between the ball and the pong paddle. Ball movement goes diagonal across x and y axis.

# Day 23 - Turtle Crossing Capstone Project

Similar gameplay to crossy road. As the level goes up, the speed of the cars increase.

# Day 24 - Files, Directories and Paths

Added a highscore file to Snake so that the game saves the highest score on the device.

# Day 25 - Working with CSV data and Pandas module

Pandas module allows us to perform data analysis on big datasets. Pandas has 2 main data structures: Data Frames and Series. Data Frames are similar to tables, Series are similar to lists.

# Day 26 - List Comprehension and the NATO Alphabet

List comprehension: `new_list = [new_item for item in list]`

Dictionary comprehension: `new_dict = {new_key:new_value for item in list}` or `new_dict = {new_key:new_value for (key, value) in dict.items()}`

Comprehensions help us to reduce the amount of code we are writing, whilst still performing exactly the same way. They are very useful for lists and dictionaries, as mentioned above. 

# Day 27 - Tkinter, `*args and **kwargs` and Creating GUIs

Tkinter is a module used to create UIs in python. Some functions have default values for arguments, meaning that we only need to provide the required arguments. We can still change the values for the default arguments if needed.

`*args` allows you to have an unlimited number of arguments for a function. It requires one asterick, and the name does not need to be args. This alows you to loop through each argument as a tuple and perform the function on each argument.

`**kwargs` allows you to have an unlimited number of keyword arguments for a function. It requires 2 astericks, and yet again, the name does not need to be kwargs. 

# Day 28 - Tkinter, Dynamic Typing and the Pomodoro Calendar

# Day 29 - Building a Password Manager GUI App

# Day 30 - Errors, Exceptions and JSON Data

# Day 31 - Flash Card App Capstone Project

# Day 32 - ???

