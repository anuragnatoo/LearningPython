from tkinter import *
window=Tk()

c = Canvas(window,width=600,height=100)
c.pack()
c.create_line(0,0,600,100, fill="Green")
c.create_line(600,0,0,100,fill="Red")
c.create_rectangle(100,80,300,60,fill="Red")
c.create_oval(100,80,300,60,fill="Blue")
window.mainloop()