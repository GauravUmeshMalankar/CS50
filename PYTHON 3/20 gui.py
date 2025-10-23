import tkinter
from tkinter import *

root = tkinter.Tk()

x = IntVar()
s = StringVar()
s.set(" ")
def even():
    n = x.get()
    if (n%2 == 0):
        s.set(f"{n} is Even number")

    else:
        s.set(f"{n} is Odd number")

def clr():
    s.set(" ")
    x.set(0)


l1 = Label(root, text="Enter a number:")
t1 = Entry(root, textvariable = x)
b1 = Button (root, text="Find", command= even)
b2 = Button(root, text="Cancel",command= clr)
l2 = Label(root,text = "Result:")
l3 = Label(root, textvariable=s)

"""
t1.grid(row = 0 , column = 1)
l1.grid(row = 0 , column = 0)
b1.grid(row = 1, column = 0)
b2.grid(row = 1, column = 1)
l2.grid(row = 2, column = 0)
l3.grid(row = 2, column = 1)
"""

l1.pack();
t1.pack();
b1.pack();
b2.pack();
l2.pack();
l3.pack();

root.mainloop()
