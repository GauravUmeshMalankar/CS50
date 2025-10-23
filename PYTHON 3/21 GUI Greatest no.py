import tkinter
from tkinter import *

root = tkinter.Tk()

x = IntVar()
y = IntVar()
z = IntVar()
s = StringVar()

def multiple():
    a = x.get()
    b = y.get()
    c = z.get()
    if (a>b and a>c):
        s.set(a,"is a greatest")
    elif(b>c):
        s.set(b,"is a greatest")
    else:
        s.set(c,"is a greatest")

def clr():
    s.set(" ")
    x.set(0)

l1 = Label(root, text="Enter a number:")
t1 = Entry(root, textvariable = x)
t2 = Entry(root, textvariable = y)
t3 = Entry(root, textvariable = z)
b1 = Button (root, text="Find", command= multiple)
b2 = Button(root, text="Cancel",command= clr)
l2 = Label(root,text = "Result:")
l3 = Label(root, textvariable=s)

l1.pack();
t1.pack();
t2.pack();
t3.pack();
b1.pack();
b2.pack();
l2.pack();
l3.pack();

root.mainloop()
