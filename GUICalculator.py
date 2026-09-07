from tkinter import *
from threading import *
from mathparse import mathparse

expr = ''

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(mathparse.parse(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light blue")
    root.title("Calculator")
    root.geometry("400x600")

    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=120, ipady=20)

    # Number buttons
    btn1 = Button(root, text='1', fg='black', bg='white', command=lambda: press(1), height=3, width=7)
    btn1.grid(row=3, column=0)
    btn2 = Button(root, text='2', fg='black', bg='white', command=lambda: press(2), height=3, width=7)
    btn2.grid(row=3, column=1)
    btn3 = Button(root, text='3', fg='black', bg='white', command=lambda: press(3), height=3, width=7)
    btn3.grid(row=3, column=2)
    btn4 = Button(root, text='4', fg='black', bg='white', command=lambda: press(4), height=3, width=7)
    btn4.grid(row=5, column=0)
    btn5 = Button(root, text='5', fg='black', bg='white', command=lambda: press(5), height=3, width=7)
    btn5.grid(row=5, column=1)
    btn6 = Button(root, text='6', fg='black', bg='white', command=lambda: press(6), height=3, width=7)
    btn6.grid(row=5, column=2)
    btn7 = Button(root, text='7', fg='black', bg='white', command=lambda: press(7), height=3, width=7)
    btn7.grid(row=7, column=0)
    btn8 = Button(root, text='8', fg='black', bg='white', command=lambda: press(8), height=3, width=7)
    btn8.grid(row=7, column=1)
    btn9 = Button(root, text='9', fg='black', bg='white', command=lambda: press(9), height=3, width=7)
    btn9.grid(row=7, column=2)
    btn0 = Button(root, text='0', fg='black', bg='white', command=lambda: press(0), height=3, width=7)
    btn0.grid(row=9, column=0)

    # Operator buttons
    plus = Button(root, text='+', fg='black', bg='red', command=lambda: press('+'), height=3, width=7)
    plus.grid(row=3, column=3)
    minus = Button(root, text='-', fg='black', bg='red', command=lambda: press('-'), height=3, width=7)
    minus.grid(row=5, column=3)
    mult = Button(root, text='*', fg='black', bg='red', command=lambda: press('*'), height=3, width=7)
    mult.grid(row=7, column=3)
    div = Button(root, text='/', fg='black', bg='red', command=lambda: press('/'), height=3, width=7)
    div.grid(row=9, column=3)

    # Other buttons
    eq = Button(root, text='=', fg='black', bg='red', command=equal, height=3, width=7)
    eq.grid(row=9, column=2)
    clr = Button(root, text='Clear', fg='black', bg='red', command=clear, height=3, width=7)
    clr.grid(row=9, column=1)
    dot = Button(root, text='.', fg='black', bg='red', command=lambda: press('.'), height=3, width=7)
    dot.grid(row=11, column=0)

    root.mainloop()

