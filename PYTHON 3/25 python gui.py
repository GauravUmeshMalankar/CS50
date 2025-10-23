import tkinter
from tkinter import *

root = tkinter.Tk()

t1  = Text(root, height = 20 , width  =30)
#photo = PhotoImage(file="D:/6. CS50/PYTHON 3/out2.jpg")
photo = PhotoImage(file="bridge.jpg")

t1.insert(END,'\n')
t1.image_create(END, image = photo)
t1.pack(side= LEFT)

t2.Text(root,height = 20, width = 30)
scroll = Scrollbar(root, command = t2.yview)
t2.config(yscrollcommand = scroll.set)
t2.tag_config('bold_ittalics',font= ('Arial',12,'bold','italic'))
t2.tag_config('big',font=('Verdana',20,'bold'))
t2.tag_bind('Click','<I>',lambda e,t1 = t2, :t.insert, (END,'Thanks!'))

q = " bridge "

t2.insert(END,q,'color')
t2.insert(END,'click here \n','click')
t2.pack(side = LEFT)
scroll.pack(side = "RIGHT", fill = y)

B=tk.Button(self.root,text="quit",command=lambda:sys.exit())
B.grid()

root.mainloop()
