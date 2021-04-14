# 👩🏾‍💻100 days of code👩🏾‍💻

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

# Day 23 - Turtle Crossing Capstone Project

# Day 24 - Files, Directories and Paths

# Day 25 - Working with CSV data and Pandas module

# Day 26 - List Comprehension and the NATO Alphabet
