from tkinter import *
window = Tk()
ftop = Frame(window)
fbot = Frame(window)

ftop.pack()
fbot.pack(side=BOTTOM)
lbl1 = Label(ftop,text="TOP FRAME")
lbl2 = Label(fbot,text="BOTTOM FRAME")
lbl3 = Label(window,text="BETWEEN")
lbl1.pack()
lbl2.pack()
lbl3.pack()
window.mainloop()