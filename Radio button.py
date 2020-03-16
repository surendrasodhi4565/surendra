#importing every methods from the tkinter module
from tkinter import *

#createing master
root=Tk()

#declaring variable
var=IntVar()
var.set(0)

#create list
lang_list = [("Python",0), ("JAVA",1), ("jQuery",2), ("Javascript",3),("C",4),("C++",5)]

def ShowChoice():
    print("You selected choice number:",v.get())
l = Label (root, text="Select Your Favourite Programming Language:")
l.pack()

for txt,val in lang_list:
    r = Radiobutton (root, text=txt, variable=v, command=ShowChoice, value=val)
    r.pack()
