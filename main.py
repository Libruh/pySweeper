import tkinter
from tkinter import *
from random import randrange

# 💣🏴

def boom():
    print("BOOM!")

def playGame(gameframe):
    bombQuantity = 15

    bombPositions = []
    for index in range(bombQuantity):
        bombPositions.append(randrange(100))

    textArray = []
    buttonArray = []

    count = 0
    for r in range(10):
        textRow = []
        buttonRow = []
        for c in range(10):
            text = StringVar()

            button = Button(gameframe, textvariable=text, fg="red", height=1, width=2, borderwidth=1)

            if count in bombPositions:
                text.set("💣")
                button.configure(command=boom)
                
            button.grid(row=r, column=c, padx = 1, pady=1)

            textRow.append(text)
            buttonRow.append(button)            
            count+=1

        textArray.append(textRow)
        buttonArray.append(buttonRow)



root = tkinter.Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Game", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

gameframe = Frame(root, relief=SUNKEN, padx=5, pady=5, bd=2)
gameframe.pack(side=BOTTOM, padx=15, pady=15)

playGame(gameframe)

root.config(menu=menubar)

root.mainloop()