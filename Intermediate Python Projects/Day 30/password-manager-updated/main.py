from tkinter import *
from tkinter import messagebox
import math
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# TODO: Use a list that stores the alphabet, numbers and symbols each
# TODO: Randomise between the 3 lists to generate a password
# TODO: Configure the textbook so that the randomised password is added to the textbox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    # Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 3)
    password = ""
    password_list = []

    # Could use a list comprehension here instead
    for i in range(0, nr_letters):
        password_list.append(random.choice(letters))
    for i in range(0, nr_symbols):
        password_list.append(random.choice(symbols))
    for i in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)  # shuffles the list

    for char in password_list:
        password += char  # adds characters to string

    password_txt.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# TODO: Create an alert when yes is pressed
# TODO: When yes is pressed for that alert, save the password using the following process below
# TODO: Create a file that will store all the passwords
# TODO: Create a function that will use the stored variables and append to the file
# TODO: Clear all the text boxes when enter is pressed


def save_password():
    title = website_txt.get()
    email = email_txt.get()
    password = password_txt.get()
    new_data = {
        title: {
            "email": email,
            "password": password,
        }
    }

    # contents = f"Email: {email}\n" \
    #            f"Password: {password}\n" \
    #            f"Is this okay?\n"
    # save = messagebox.askokcancel(title, message=contents)
    if len(title) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Make sure there are no empty fields")
    else:
        try:
            with open("passwords.json", "r") as file:
                # reading old data
                data = json.load(file)
                # updating with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("passwords.json", "w") as file:
                # adding to json file
                json.dump(data, file, indent=4)
        finally:
            website_txt.delete(0, END)
            password_txt.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = website_txt.get()

    with open("passwords.json", "r") as file:
        data = json.load(file)
        try:
            email_address = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="404 Error", message="Website cannot be found")
        else:
            messagebox.showinfo(title=f"{website}", message=f"email: {email_address}\n"
                                                            f"password: {password}\n")

# ---------------------------- UI SETUP ------------------------------- #

# TODO: Initialise window with dimensions
# TODO: Configure window with grid format for all widgets
# TODO: Create canvas and add image to the canvas
# TODO: Add labels and buttons to window


# window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# components
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=1, column=2)

website_lbl = Label(text="Website:", highlightthickness=0)
website_lbl.config(font=("Arial", 15, "normal"))
website_lbl.grid(row=2, column=1)

email_lbl = Label(text="Email/Username:", highlightthickness=0)
email_lbl.config(font=("Arial", 15, "normal"))
email_lbl.grid(row=3, column=1)

password_lbl = Label(text="Password:", highlightthickness=0)
password_lbl.config(font=("Arial", 15, "normal"))
password_lbl.grid(row=4, column=1)

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=5, column=2, columnspan=3)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=4, column=3)

search_btn = Button(text="Search", width=13, command=search)
search_btn.grid(row=2, column=3)

website_txt = Entry(width=21)
website_txt.grid(row=2, column=2)

email_txt = Entry(width=35)
email_txt.insert(0, "demiaoshin@gmail.com")
email_txt.grid(row=3, column=2, columnspan=3)

password_txt = Entry(width=21, textvariable='password', show="*")
password_txt.grid(row=4, column=2, columnspan=1)

window.mainloop()
