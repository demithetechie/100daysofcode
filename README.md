# 👩🏾‍💻100 days of code👩🏾‍💻

I will be starting the 100 days of code challenge with Python. Updates will be placed here daily from 1st December.
Proposed finish date: 11th March 2021

# Day 1 - Printing, Variables, Strings

Challenge: Band Name Generator

Important notes: Use \n for a newline.

# Day 2 - Data Types (Strings, Integers, Floats and Booleans), Mathematical Operations, String and Number Manipulation, F strings

Challenge: Tip Calculator

Important notes: Using indexes on strings to reference a character of a string. Strings can be added together to form longer strings.

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

Important notes: Use logical operators `and, or, not` to validate expressions in Python.

# Day 4 - Randomisation and Python Lists

Challenge: Rock, Paper, Scissors

Important notes: Computers are deterministic, which means that they perform actions in a predictable way. The python random library uses a pseudorandom number generator. 

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

Important notes: Research the functions under the random module e.g. `shuffle()` and `choice()`

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

Important notes: Most of the coding for this project was done on this website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Day 7 - Hangman project

Today is dedicated solely for the hangman project.

Link to view: https://repl.it/@DemiladeOshin/Day-7-Hangman-5-Start

# Day 8 - Functions and Inputs

Challenge: Caesar Cipher

Important notes: Parameters are the name of the variable that the function deals with. Arguments are the raw value assigned to the parameter. 

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
```
