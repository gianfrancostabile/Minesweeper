from tkinter import *


class View(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("Minesweeper")

    def display(self):
        self.root.mainloop()

    def generateFrameGrids(self, mMap):

        frame = Frame(self.root, padx=10, pady=10)
        frame.configure(background="light slate blue")
        copy = Frame(self.root, padx=10, pady=10)
        copy.configure(background="light slate blue")

        width = mMap.difficultSelected.width
        height = mMap.difficultSelected.height

        for y in range(0, height):
            for x in range(0, width):
                celdXY = mMap.map[y][x]
                color = celdXY.getColorByNumber()

                label = Label(frame, text="{content}".format(content=celdXY.content), width=3, height=1, fg=color)
                label.grid(row=y, column=x)
                label.place_forget()

                button = Button(frame, text="", width=3, height=1)
                button.grid(row=y, column=x)

                def showContent(btn, lbl):
                    text, fg, background = lbl["text"], lbl["fg"], "grey"
                    btn["text"], btn["fg"], btn["background"] = text, fg, background

                button.config(command=lambda btn=button, lbl=label: showContent(btn, lbl))

        for y in range(0, height):
            for x in range(0, width):
                celdXY = mMap.map[y][x]
                color = celdXY.getColorByNumber()
                button = Button(copy, text="{content}".format(content=celdXY.content), width=3, height=1, fg=color)
                button.grid(row=y, column=x)

        frame.pack()
        copy.pack()

