# calculator using GUI
from tkinter import *
window = Tk()
window.geometry('400x400')
e = Entry(window, width=55, borderwidth=20)
e.place(x=0, y=0)


def btclick(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(num))


b = Button(window, text='1', width=15, command=lambda: btclick(1), bg="pink", fg="black")
b.place(x=10, y=60)
b = Button(window, text='2', width=15, command=lambda: btclick(2), bg="pink")
b.place(x=80, y=60)
b = Button(window, text='3', width=15, command=lambda: btclick(3), bg="pink", )
b.place(x=10, y=120)
b = Button(window, text='4', width=15, command=lambda: btclick(4), bg="pink")
b.place(x=80, y=120)
b = Button(window, text='5', width=15, command=lambda: btclick(5), bg="pink")
b.place(x=10, y=180)
b = Button(window, text='6', width=15, command=lambda: btclick(6), bg="pink")
b.place(x=80, y=180)
b = Button(window, text='7', width=15, command=lambda: btclick(7), bg="pink")
b.place(x=10, y=240)
b = Button(window, text='8', width=15, command=lambda: btclick(8), bg="pink")
b.place(x=80, y=240)
b = Button(window, text='9', width=15, command=lambda: btclick(9), bg="pink")
b.place(x=10, y=300)
b = Button(window, text='0', width=15, command=lambda: btclick(0), bg="pink")
b.place(x=80, y=300)


def add():
    firstno = e.get()
    global math
    math = 'addition'
    global a
    a = int(firstno)
    e.delete(0, END)


b = Button(window, text='+', width=15, command=add, bg="purple")
b.place(x=170, y=60)


def sub():
    firstno = e.get()
    global math
    math = 'subtract'
    global a
    a = int(firstno)
    e.delete(0, END)


b = Button(window, text='-', width=15, command=sub, bg="purple")
b.place(x=170, y=120)


def multiply():
    firstno = e.get()
    global math
    math = 'multiply'
    global a
    a = int(firstno)
    e.delete(0, END)


b = Button(window, text='*', width=15, command=multiply, bg="purple")
b.place(x=170, y=180)


def divide():
    firstno = e.get()
    global math
    math = 'divide'
    global a
    a = int(firstno)
    e.delete(0, END)


b = Button(window, text='/', width=15, command=divide, bg="purple")
b.place(x=170, y=240)


def pow():
    firstno = e.get()
    global math
    math = 'pow'
    global a
    a = int(firstno)
    e.delete(0, END)


b = Button(window, text='**', width=15, command=pow, bg="purple")
b.place(x=170, y=300)


def percent():
    firstno = e.get()
    global math
    math = 'percent'
    global a
    a = int(firstno)
    e.delete(0, END)


b = Button(window, text='%', width=15, command=percent, bg="purple")
b.place(x=10, y=350)


def equal():
    secondno = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, a + int(secondno))
    elif math == 'subtract':
        e.insert(0, a - int(secondno))
    elif math == 'multiply':
        e.insert(0, a * int(secondno))
    elif math == 'divide':
        e.insert(0, a / int(secondno))
    elif math == 'pow':
        e.insert(0, a ** int(secondno))
    elif math == 'percent':
        e.insert(0, a / 100 * int(secondno))


b = Button(window, text='=', width=15, command=equal, bg="purple")
b.place(x=80, y=350)


def clear():
    e.delete(0, END)


b = Button(window, text='clear', width=15, command=clear, bg="green")
b.place(x=170, y=350)
window.mainloop()
