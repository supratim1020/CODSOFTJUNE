import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("570x650+100+100")
root.resizable(0, 0)
root.config(bg="#404258")

equation = ""


def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
    label_result.config(text=result)



inc_x=2
inc_y=50

label_result = Label(root, width=70, height=2, text="", font=("LMRoman10-Regular", 30,"bold"),bg="#CAEDFF")
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#279EFF",
       command=lambda: clear()).place(x=10+inc_x, y=100+inc_y)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#9500ff",
       command=lambda: show("/")).place(x=150+inc_x, y=100+inc_y)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#9500ff",
       command=lambda: show("%")).place(x=290+inc_x, y=100+inc_y)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#9500ff",
       command=lambda: show("*")).place(x=430+inc_x, y=100+inc_y)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("7")).place(x=10+inc_x, y=200+inc_y)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("8")).place(x=150+inc_x, y=200+inc_y)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("9")).place(x=290+inc_x, y=200+inc_y)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#9500ff",
       command=lambda: show("-")).place(x=430+inc_x, y=200+inc_y)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("4")).place(x=10+inc_x, y=300+inc_y)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("5")).place(x=150+inc_x, y=300+inc_y)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("6")).place(x=290+inc_x, y=300+inc_y)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#9500ff",
       command=lambda: show("+")).place(x=430+inc_x, y=300+inc_y)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("1")).place(x=10+inc_x, y=400+inc_y)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("2")).place(x=150+inc_x, y=400+inc_y)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("3")).place(x=290+inc_x, y=400+inc_y)
Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#00b392",
       command=lambda: show("0")).place(x=10+inc_x, y=500+inc_y)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037",
       command=lambda: show(".")).place(x=290+inc_x, y=500+inc_y)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037",
       command=lambda: calculate()).place(x=430+inc_x, y=400+inc_y)


root.mainloop()
