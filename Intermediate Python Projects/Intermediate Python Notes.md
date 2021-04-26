# 👩🏾‍💻100 days of code👩🏾‍💻

# Day 15 - Intermediate🎉 - Local Development Environment Setup

Using PyCharm:

PyCharm has various features including:  

> **Spell Check** - This spell checks the words you are typing, so that you don't have unneseccary spelling errors in your code.  
> 
> **More Space** - PyCharm allows for more files to code with. You can also split screen by right clicking on the file and pressing "Split to right" or "Split to left". 
> 
> **Built In Linter** - This picks out bits of code and lets you know if you are writing in the correct style of coding. PEP 8 is the style used in PyCharm. Helps you improve the way you code in python.  
> 
> **Local History** - This allows you to see changes to the code. You can go back to the last 12 hours to figure out what you were coding beforehand. Use the show history tab to view local history.  
> 
> **View Structure of code** - This allows you to see all the functions and variables declared in your code. You can use the structure pane to view how you code is organised.  
> 
> **Refactor** - Allows you to rename functions without changing every occurence of the function

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

The aim is to create a Turtle racing game where the user bets on which colour turtle will win the race, and then each turtle is instantiated and they move at random paces. 

Important concepts in this project: Using for loops to create multiple instances of an object, using a while loop to get each turtle to move.

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

Creating and managing multiple classes, detecting and controlling interactions with each object using inequalities and if statements. Keeping score of which player is winning the game and allowing 2 players to control each paddle, left and right.

# Day 23 - Turtle Crossing Capstone Project

Similar to pong game, creating classes and detecting when the turtle has reached the end of the map. Continuously creating objects while the game is running, and creating an neverending loop for the game, with the difficulty increasing after each level.

# Day 24 - Files, Directories and Paths

When it comes to file writing, it is common to use `with open('file.txt', 'r') as file:` which means that any code that is under this block is run and we don't need to include the file.close() method.

Relative file path: These paths are usually from ur current directory, and don't include every folder that links to the file. The relative file path tends to be shorter than the absolute file path.

Absolute file path: This always contains the root folder down to the target file, including every directory within the path.

# Day 25 - Working with CSV data and Pandas module

**Pandas** is a library that allows us to process, prepare and manage data before analysing it. It includes some elements of data visualisation as well. It is a powerful library that provides you with functions that allow you to manipulate data for various purposes, most commonly related to data analysis and machine learning.

# Day 26 - List Comprehension and the NATO Alphabet

List comprehensions allows us to create lists using one line of code, as long as all the items follow the same rule for the comprehension. 

It makes the code look neater as well as reducing the complexity.

Dictionary comprehensions are often used as well to create dictionaries effectively.

# Day 27 - Using Tkinter: Creating a miles to kilometers converter

**Tkinter** is a python library that allows you to create GUIs (Graphical User Interfaces). This can help with coding applications where having a GUI helps a lot more than simply relying on the console.

Tkinter contains a lot of widgets that you can include in your window, such as radio buttons, labels, combo boxes, scrollers and more.

# Day 28 - Using Tkinter: Creating a Pomodoro timer

Python supports dynamic typing, which is where variable types can be changed as the program is running.
Static typing is the opposite of this, which is where variable types are assigned from compilation, and cannot be changed as the code is running.

# Day 29 - Creating a Local Password Manager Application

The function `grid()` allows you to allocate widgets to a specific row and column of the window. This allows us to create more effective user interfaces.

Tkinter also allows you to create popup windows, such as `messagebox.showinfo` and `messagebox.askyesno`. These pop up windows are very useful to use alongside the main window.

# Day 30 - Password Manager Upgrade: Catching Exceptions and Working with JSON files 

### Handling exceptions

It's important to handle exceptions in advance wherever possible, so that we can deal with the error before it is thrown. Handling exceptions helps us see how our code could behave unexpectedly, and how we can combat this without the program crashing. The main keywords in python for handling exceptions are: **try, except, else** and **finally**.

> **try**: With try, we can place code that we think may throw an error. Examples of code like this could  be opening a file that may not exist.
> 
> **except**: This code block is run if an exception is thrown. It's good coding practice to specify the > error after the except (such as `except KeyError`) as this makes it easier to deal with different exceptions. You can also represent the error as an errormessage (`except KeyError as errormessage`) which is useful for when the program has to alert the user of an error.
>
> **else**: This code block is run if the try block does not throw any exceptions. In which case, the code can continue as expected here. E.g. if the file opened successfully, you can read from the file or add to the file in this block.
>
> **finally**: This code block is run regardless of whether the try block throws an exception or not. This block isn't always used, but it can be useful if you have code that must run despite any errors or exceptions.

With these code blocks we can successfully handle exceptions and deal with them as they come, thus making our code much more reusable.

### Dealing with JSON files

JSON files are very similar to python dictionaries, and they allow us to search, add and delete local data very swiftly. The 3 main functions used in this project are: **json.dump(), json.load(), json.update().**

> **json.dump()**: This function allows you to add data to the json file.
>
> **json.load()**: This function allows you to load data from the json file.
>
> **json.update()**: This function allows you to update data from the json file.

# Day 31 - Capstone Project: Flash Card Application