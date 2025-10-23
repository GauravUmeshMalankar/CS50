import tkinter
from tkinter import *
from PIL import ImageTk, Image

root= Tk()
# We will make the title of our app as Image Viewer
root.title("Image Viewer")
 


# Set the geometry of Tkinter Frame
#root.geometry("700x450")



 





img1 = ImageTk.PhotoImage(Image.open("D:/6. CS50/PYTHON 3/out2.jpg"))
img2 = ImageTk.PhotoImage(Image.open("D:/6. CS50/PYTHON 3/out.jpg"))
img3 = ImageTk.PhotoImage(Image.open("D:/6. CS50/PYTHON 3/GUI Images/img3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("D:/6. CS50/PYTHON 3/GUI Images/img4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("D:/6. CS50/PYTHON 3/GUI Images/img5.jpg"))
img6 = ImageTk.PhotoImage(Image.open("D:/6. CS50/PYTHON 3/GUI Images/img6.jpg"))

image_list=[img1,img2,img3,img4,img5,img6]

l1 = Label(root, image=img1)
l1.grid(row=0, column = 0, columnspan=3)



def autoplay(imgno):
    global l1
    global b1
    global b2

    l1.grid_forget()
    l1= Label(image = image_list[imgno-1])
    l1.grid(row=0, column = 0, columnspan=3)

    for img in image_list(imgno):
        
        
        
    

def forward(imgno):
    global l1
    global b1
    global b2

    l1.grid_forget()
    l1= Label(image = image_list[imgno-1])
    l1.grid(row=0, column = 0, columnspan=3)
    b1 = Button(root, text="Next",command=lambda:forward(imgno+1))
    b2 = Button(root, text="Back",command=lambda:backward(imgno-1))

    if imgno == 6:
        b1 = Button(root, text="Next", state=DISABLED)

    b1.grid(row= 1,column=2)
    b2.grid(row= 1,column=0)


    

def backward(imgno):
    global l1
    global b1
    global b2

    
    l1.grid_forget()
    l1= Label(image = image_list[imgno-1])
    l1.grid(row=0, column = 0, columnspan=3)
    b1 = Button(root, text="Next",command=lambda:forward(imgno+1))
    b2 = Button(root, text="Back",command=lambda:backward(imgno-1))

    if imgno == 1:
        b2 = Button(root, text="Back", state=DISABLED)

    b1.grid(row= 1,column=2)
    b2.grid(row= 1,column=0)






b1 = Button(root, text="Next",command=lambda:forward(2))
t1 = Button(root, text="Exit",command= root.destroy)
b2 = Button(root, text="Back",command=backward)

b1.grid(row= 1,column=2)
t1.grid(row= 1,column=1)
b2.grid(row= 1,column=0)

b3 = Button(root, text="Play",command=lambda:forward(imgno+1))
b3.grid(row=2,column=1)

root.mainloop()
