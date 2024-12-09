from tkinter import *
from tkinter import messagebox
top = Tk()
def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text ="Hello", command = helloCallBack)
B.pack()
# placerar en 100*100 pixlar stor knapp 50 pixlar åt höger och 25 pixlar nedåt från övre vänsterkanten
B.place(x=50, y=25, height=100, width=100)
top.mainloop()
# se mer på t.ex. https://www.tutorialspoint.com/python/tk_place.htm