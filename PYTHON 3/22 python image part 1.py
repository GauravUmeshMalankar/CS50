import tkinter
from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("MY CODE")
root.iconbitmap('D:/6. CS50/PYTHON 3/playerGrey_walk1.ico')

t1  = Text(root, height=20,width=30)
t1.pack()

img = ImageTk.PhotoImage(Image.open("D:/6. CS50/PYTHON 3/out2.jpg"))

l1 = Button(image=img, command=DISABLED)
#l1 = Label(image= img)
l1.pack()

b1 = Button(root, text="Exit Program", command = root.destroy)
b1.pack()



root.mainloop()
