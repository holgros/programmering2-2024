from tkinter import *
root = Tk()
# skapa Canvas med blå bakgrundsfärg, höjd 250 pixlar och bredd 300 pixlar
canv = Canvas(root, bg="blue", height=250, width=300)
# lägg in en bildfil; första två parametrarna är förskjutning i x- och y-led
filename = PhotoImage(file = "bild.gif")
image = canv.create_image(250, 200, image=filename)
# rita en cirkelbåge; första parametrarna anger position och storlek, de sista två anger bågens krökning i grader
arc = canv.create_arc(10, 20, 140, 210, start=30, extent=120, fill="red")
# rita en linje; de första parametrarna är parvisa koordinater
line = canv.create_line(20, 20, 250, 250, 100, 20, width=10, fill="green")
canv.pack()
root.mainloop()
