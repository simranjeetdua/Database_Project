#practice script to get familiar with tkinter library to create GUI

from tkinter import *

#it has two parts one being the window and the other being the the widgets

window=Tk() #window part

def kmtomiles():
    print("success")

b1=Button(window,text="Execute",command=kmtomiles)
b1.grid(row=0,column=0)  #simple button object

e1=Entry(window)
e1.grid(row=0,column=1) #simple entry object

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2) #simple text output object with edited height and width

window.mainloop()
