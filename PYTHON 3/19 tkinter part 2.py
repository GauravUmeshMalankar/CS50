import tkinter
from tkinter import *
root = tkinter.Tk()

x = IntVar()
s = StringVar()
s.set("Result:")

def fact():
    n=x.get()
    f=1
    for i in range(1,n+1):
        f*=i
    s.set(f"Factorial of {n} ={f}")

def clr():
    s.set("Result:")
    
    x.set(0)

l1 = Label(root, text= "Enter no:")#.grid(row=0,column=0)
t1 = Entry(root, textvariable = x)#.grid(row=0,column=1)
b1 = Button(root, text="Find Factorial", command= fact)#.grid(row=1,column=0)
b2 = Button(root, text="Cancel",command=clr)#.grid(row=1,column=1)
l2 = Label(root, textvariable= s)#.grid(row=2,column=0)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
l2.grid(row=2,column=0)

l1.pack();
t1.pack();
b1.pack();
b2.pack();
l2.pack();

root.mainloop()
