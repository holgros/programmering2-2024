# "side" innebär att widgets läggs bredvid varandra, istället för ovanför varandra
from tkinter import *
root = Tk()
w = Label(root, text="red", bg="red", fg="white")
w.pack(padx=5, pady=10, side=LEFT)  # "side=LEFT" betyder att widgeten läggs första lediga plats från vänster
w = Label(root, text="green", bg="green", fg="black")
w.pack(padx=5, pady=20, side=LEFT)
w = Label(root, text="blue", bg="blue", fg="white")
w.pack(padx=5, pady=20, side=LEFT)
mainloop()
