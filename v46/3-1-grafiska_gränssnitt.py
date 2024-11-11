from tkinter import *						# importera
root = Tk()								    # skapa rot-fönster
b = Button(root, text ="Tryck mig!")		# skapa widget

e = Entry(root)	                            # skapa widget (inmatningsfält)
e.pack()			                        # packa

def click_handler(self):			        # skapa en "callback"-funktion
    print("Någon klickade på knappen!")     # skriv till konsolen
    print("Du skrev", e.get())              # läs input och skriv till konsolen
    lbl["text"] = "Du skrev: " + e.get()    # läs input och skriv till fönstret
b.bind("<Button-1>", click_handler)	        # knyt funktionen till händelse (vänster musknappsklick)

b.pack()									# packa

lbl = Label(root)
lbl.pack()

root.mainloop()							    # visa fönstret
