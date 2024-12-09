# genom att packa widgets i en logisk hierarki ("nästlade" widgets) kan man åstadkomma komplicerad layout
from tkinter import *
root = Tk() # root = hela fönstret
# skapa en Frame-widget inuti fönstret
topframe = Frame(root)
# skapa en Frame-widget "leftframe" inuti topframe
leftframe = Frame(topframe)
# inuti leftframe läggs tre knappar ovanför varandra
button1 = Button(leftframe, text="Knapp 1")
button1.pack()
button2 = Button(leftframe, text="Knapp 2")
button2.pack()
button3 = Button(leftframe, text="Knapp 3")
button3.pack()
leftframe.pack(side=LEFT)   # leftframe läggs längst till vänster i föräldraelementet (topframe)
# skapa en Text-widget "text" inuti topframe
text = Text(topframe, width=50, height=5)
text.pack(side=LEFT)    # text läggs nästa lediga plats vänsterifrån (efter leftframe) i föräldraelementet (topframe)
topframe.pack() # topframe (och allt dess innehåll) läggs längst upp i föräldraelementet (root)
# skapa en Label-widget "label" inuti fönstret
label = Label(root, text="Layout med Tkinter!")
label.pack()    # label läggs på nästa lediga plats uppifrån (efter topframe) i föräldraelementet (root)
mainloop()
