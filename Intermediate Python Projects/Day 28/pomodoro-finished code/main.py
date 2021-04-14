from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:00")
    timer_lbl.config(text="Timer")
    reps = 0
    tick_lbl.config(text="✓")
    




# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if reps == 8:
        timer_lbl.config(text="LONG BREAK")
        count_down(long)
    elif reps % 2 == 0:
        timer_lbl.config(text="SHORT BREAK")
        count_down(short)
    else:
        timer_lbl.config(text="STUDY!")
        count_down(work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds <= 9:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        tick_lbl.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# creating a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# labels
timer_lbl = Label(text="Timer", highlightthickness=0)
timer_lbl.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "normal"))
timer_lbl.grid(row=1, column=2)

tick_lbl = Label(text="✓", highlightthickness=0, fg=GREEN, bg=YELLOW)
tick_lbl.grid(row=4, column=2)

# buttons
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=3, column=1)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=3, column=3)


window.mainloop()
