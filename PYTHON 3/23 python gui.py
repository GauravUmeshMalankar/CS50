# List widget

import tkinter
from tkinter import *

root = tkinter.Tk()

l1 = Listbox(root)
l1.insert(0,"   ")
l1.insert(1,"Mango")
l1.insert(2,"Pear")
l1.insert(3,"Banana")
l1.insert(4,"Cherry")
l1.insert(5,"Apple")

l1.pack()


root.mainloop()
