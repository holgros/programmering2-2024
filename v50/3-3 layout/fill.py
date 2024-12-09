# metoden pack lägger widgets ovanpå varandra - argument som t.ex. fill kan användas för att justera utseendet
from tkinter import *
root = Tk()
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()
#w.pack(fill=X)
w = Label(root, text="Green Grass", bg="green", fg="black")
#w.pack()
w.pack(fill=X)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
#w.pack()
w.pack(fill=X)
root.mainloop()
# se mer på t.ex. https://www.tutorialspoint.com/python/tk_pack.htm