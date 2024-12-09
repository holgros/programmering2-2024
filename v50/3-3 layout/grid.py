from tkinter import *
root = Tk()
for r in range(3):
   for c in range(4):
      w = Label(root, text='(%s,%s)'%(r,c), borderwidth=5 )
      w.grid(row=r,column=c)    # lägger widgeten i en grid i rad r och kolumn c
root.mainloop()
# se mer på t.ex. https://www.tutorialspoint.com/python/tk_grid.htm