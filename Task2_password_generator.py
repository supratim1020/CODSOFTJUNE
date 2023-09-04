import tkinter
from tkinter import *
from tkinter import ttk
import string
import random
import pyperclip

# main window
root = Tk()
root.title("Password Generator")
root.geometry("440x400+100+200")
root.resizable(False, False)


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    length = int(ENTRY.get())
    selected_strength = strength.get()

    if selected_strength == "Weak":
        All = small_alphabets + capital_alphabets
    elif selected_strength == "Medium":
        All = small_alphabets + capital_alphabets + numbers
    elif selected_strength == "Strong":
        All = small_alphabets + capital_alphabets + numbers + special_characters
    else:
        All = small_alphabets + capital_alphabets + numbers + special_characters

    Password = random.choices(All, k=length)
    Password = ''.join(Password)
    Password_Field.delete(0, 'end')
    Password_Field.insert(0, Password)


def Copy():
    Copy = Password_Field.get()
    pyperclip.copy(Copy)


# heading
title_lbl = Label(root, text="Password  Generator", font=("Qrada", 18, "bold"), bg="#774360", fg="white")
title_lbl.place(x=0, y=0, width=440, height=45)

# length
Length = Label(root, text="Length", font=("Century Gothic", 22, "bold"), fg="teal")
Length.place(x=12, y=60, width=130, height=49)

ENTRY = Spinbox(root, highlightthickness=1, highlightbackground="black", font=("Verdana Regular", 18), bg="#CAEDFF", from_=5, to=18)
ENTRY.place(x=150, y=69, width=150, height=35)

# strength
Strength = Label(root, text="Strength", font=("Century Gothic", 22, "bold"), fg="teal")
Strength.place(x=10, y=112, width=140, height=47)

strength = ttk.Combobox(root, font=("Verdana Regular", 18), background="#CAEDFF")
strength["values"] = ("Select", "Weak", "Medium", "Strong")
strength.current((0))
strength.place(x=150, y=120, width=150, height=35)

# generate button
Generate_Button = Button(root, command=generator, text="Generate", font=("Celebes", 18), bg="#B25068", fg="white")
Generate_Button.place(x=120, y=170, width=200, height=35)

# lower portion
Password_Field = Entry(root, font=("Monaco", 18), bg="#352F44", fg="#fff3b0")
Password_Field.place(x=70, y=265, width=300, height=40)

Copy_Button = Button(root, command=Copy, text="Copy", font=("Dubai", 18), bg="#40916c", fg="white")
Copy_Button.place(x=120, y=315, width=200, height=35)

root.mainloop()
