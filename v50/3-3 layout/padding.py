# "padding" innebär ett mellanrum
from tkinter import *
root = Tk()
w = Label(root, text="Red Sun", bg="red", fg="white")
# extern padding i y-led
w.pack(fill=X, pady=10)
w = Label(root, text="Green Grass", bg="green", fg="black")
# extern padding i x-led
w.pack(fill=X, padx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
# intern padding i y-led
w.pack(fill=X, ipady=10)    # observera "ipady" (intern padding) istället för "pady" (extern padding)
# extern padding i x-led med olika avstånd åt höger och åt vänster
w.pack(padx=(0, 20))    # padding i x-led 0px åt vänster och 20 px åt höger
mainloop()
