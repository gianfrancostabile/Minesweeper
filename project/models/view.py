from tkinter import *

class View(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("Minesweeper")

    def display(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()

    def generateFrameGrids(self, mMap):
        frame = Frame(self.root, padx=10, pady=10)
        frame.configure(background="light slate blue")

        width = mMap.difficultSelected.width
        height = mMap.difficultSelected.height

        for y in range(0, height):
            for x in range(0, width):
                celdXY = mMap.map[y][x]
                color = self.getColorByNumber(celdXY.content)
                button = Button(frame, text="{content}".format(content=celdXY.content), width=3, height=1, fg=color)
                button.grid(row=y, column=x)

        frame.pack()

    def getColorByNumber(self, content):
        color = "lavender"

        if content == -1:
            color = "black"
        elif content == 1:
            color = "deep sky blue"
        elif content == 2:
            color = "lime green"
        elif content == 3:
            color = "red"
        elif content == 4:
            color = "navy"
        elif content == 5:
            color = "firebrick"
        elif content == 6:
            color = "magenta"
        elif content == 7:
            color = "sienna"
        elif content == 8:
            color = "snow3"

        return color




