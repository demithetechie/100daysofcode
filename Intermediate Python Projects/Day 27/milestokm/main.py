from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometres Converter")
window.minsize(width=200, height=200)

# creating labels and text entries
miles_label = Label(text="miles:")
km_label = Label(text="kilometres:")

miles_label.grid(row=0, column=0, sticky=W, pady=2)
km_label.grid(row=1, column=0, sticky=W, pady=2)

miles_entry = Entry(width=10)
km_label = Label(text=0)

miles_entry.grid(row=0, column=1, pady=2)
km_label.grid(row=1, column=1, pady=2)

def calculate():
    miles = int(miles_entry.get())
    km = round(miles * 1.609344, 4)
    km_label.config(text=km)


submit = Button(text="Calculate!", command=calculate)
submit.grid(row=3, pady=3)

window.mainloop()