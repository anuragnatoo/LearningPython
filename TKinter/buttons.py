from tkinter import *
window = Tk()
def handleClick():
    print("Button Clicked!")

btn = Button(window,bd=10,bg="Black",fg="White",text="Click Me!",padx=50,pady=50,command=handleClick)
btn.place(x=50,y=50)

window.mainloop()
