import tkinter
from tkinter import *
import sqlite3

root = tkinter.Tk()

a = IntVar()
b = StringVar()
c = IntVar()
s = StringVar()
s.set("Output:")

def check():
    try:
        db = sqlite3.connect("100 python db.db")
        cursor=db.cursor()
        a1=a.get()
        b1=b.get()
        c1=c.get()
      
        sql= "insert into emp values(' "+str(a1)+" ','"+b1+"','"+str(c1)+"')"
        cursor.execute(sql)
        db.commit()
        s.set("Record inserted successfully")
        db.close()
    except Exception as e:
        print("Check connection",e)

def clear():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    s.set("Output:")
   


l1 = Label(root, text = "Enter Empolyee Id:")
t1 = Entry(root, textvariable = a)
l2 = Label(root, text = "Enter Empolyee Name:")
t2 = Entry(root, textvariable = b)
l3 = Label(root, text = "Enter Empolyee Salary:")
t3 = Entry(root, textvariable = c) 
b1 = Button(root, text = "Insert", command=check)
b2 = Button(root, text = "Cancel", command=clear)
t4 = Label(root, textvariable =s)

l1.grid(row = 0, column = 0 )
t1.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
t2.grid(row = 1, column = 1)
l3.grid(row = 2, column = 0)
t3.grid(row = 2, column = 1)
b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
t4.grid(row = 4, column = 0)



root.mainloop()
