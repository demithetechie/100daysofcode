from tkinter import *
import random
import pandas as pd
import time

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
FOREIGN_LANGUAGE = "French"
FIRST_LANGUAGE = "English"

# DATA STRUCTURES
current_word = {}
to_learn = {}
learnt = {}

# CREATING WINDOW
window = Tk()
window.title("Flashy!!")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(row=1, column=1, columnspan=2)

lang_word = canvas.create_text(400, 150, font=FONT_LANG, text=FOREIGN_LANGUAGE)
actual_word = canvas.create_text(400, 263, font=FONT_WORD)

# FUNCTIONS


def reveal_card():
    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(lang_word, text=FIRST_LANGUAGE, fill="white")
    canvas.itemconfig(actual_word, text=current_word[FIRST_LANGUAGE], fill="white")


def correct():
    learnt[current_word[FOREIGN_LANGUAGE]] = current_word[FIRST_LANGUAGE]
    current_word.clear()
    new_word()


def wrong():
    to_learn[current_word[FOREIGN_LANGUAGE]] = current_word[FIRST_LANGUAGE]
    current_word.clear()
    new_word()


def new_word():
    global flip
    window.after_cancel(flip)
    number = random.randint(0, 100)
    french_word = words[FOREIGN_LANGUAGE][number]
    english_word = words[FIRST_LANGUAGE][number]
    current_word[FOREIGN_LANGUAGE] = french_word
    current_word[FIRST_LANGUAGE] = english_word
    canvas.itemconfig(canvas_image, image=front_card_img)
    canvas.itemconfig(lang_word, text=FOREIGN_LANGUAGE, fill="black")
    canvas.itemconfig(actual_word, text=french_word, fill="black")
    flip = window.after(3000, func=reveal_card)


flip = window.after(3000, func=reveal_card)

try:
    data = pd.read_csv("data/french_words.csv")
    words = data.to_dict()
except FileNotFoundError:
    print("failed")
else:
    new_word()


# ADDING COMPONENTS

cross_image = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=cross_image, highlightthickness=0, command=wrong)
cross_btn.grid(row=2, column=1)

tick_image = PhotoImage(file="images/right.png")
tick_btn = Button(image=tick_image, highlightthickness=0, command=correct)
tick_btn.grid(row=2, column=2)

flip = window.after(3000, func=reveal_card)


window.mainloop()


