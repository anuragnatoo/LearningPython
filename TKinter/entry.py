from tkinter import *
window = Tk()
def PrintValue():
    print("The String you just typed is",userinput.get())
userinput = StringVar()
userinput.trace("w",lambda name,index,mode:PrintValue())
e = Entry(window,fg="Red",bg="Black",bd=4,textvariable=userinput)
e.pack()
window.mainloop()