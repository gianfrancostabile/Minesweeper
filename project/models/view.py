from tkinter import *
import threading

class View(object):

    def __init__(self, mMap):
        self.root = Tk()
        self.root.title("Minesweeper")
        self.btn_map = []
        self.map = mMap

    def display(self):
        self.root.mainloop()

    def generateFrameGrids(self):

        frame = Frame(self.root, padx=10, pady=10)
        frame.configure(background="light slate blue")

        width = self.map.difficultSelected.width
        height = self.map.difficultSelected.height

        for y in range(0, height):
            btn_sublist = []
            for x in range(0, width):
                celdXY = self.map.celds[y][x]

                button = Button(frame, text="", width=3, height=1)
                button.grid(row=y, column=x)
                button.config(command=lambda btn=button, celd=celdXY: self.showContent(btn, celd))

                btn_sublist.append(button)
            self.btn_map.append(btn_sublist)

        frame.pack()

        frame = Frame(self.root, padx=10, pady=10)
        frame.configure(background="light slate blue")

        width = self.map.difficultSelected.width
        height = self.map.difficultSelected.height

        for y in range(0, height):
            btn_sublist = []
            for x in range(0, width):
                celdXY = self.map.celds[y][x]

                button = Button(frame, text="", width=3, height=1)
                button.grid(row=y, column=x)
                button["text"], button["fg"], button["background"] = celdXY.content, celdXY.getColorByNumber(), "grey"

                btn_sublist.append(button)
            self.btn_map.append(btn_sublist)

        frame.pack()

    def showContent(self, btn, celd):
        background = "grey"
        content, fg = celd.content, celd.getColorByNumber()
        btn_content = btn["text"]

        if content == -1:
            self.display_GameOver()
            btn["text"], btn["fg"], btn["background"] = content, fg, background

        elif content == 0 and not celd.showed:
            self.showContentEmpty(celd.x, celd.y)

        elif btn_content != "" and 9 > content > 0:
            countX, countY = 0, 0
            x2, y2 = celd.x - 1, celd.y - 1

            while countY < 3:
                while countX < 3:
                    try:
                        if x2 > -1 and y2 > -1:
                            celd2 = self.map.celds[y2][x2]
                            btn2 = self.btn_map[y2][x2]

                            if not celd2.showed and celd2.content == -1:
                                self.display_GameOver()

                            self.map.celds[y2][x2].showed = True
                            btn2["text"], btn2["fg"], btn2["background"] = celd2.content, celd2.getColorByNumber(), background
                    except Exception as e:
                        pass
                    finally:
                        countX = countX + 1
                        x2 = x2 + 1
                countY = countY + 1
                y2 = y2 + 1
                countX = 0
                x2 = celd.x - 1

        btn["text"], btn["fg"], btn["background"] = content, fg, background

    def showContentEmpty(self, x, y):
        threads = list()
        t1 = threading.Thread(target=self.showContentEmptyX, args=(x, y))
        threads.append(t1)
        t2 = threading.Thread(target=self.showContentEmptyY, args=(x, y))
        threads.append(t2)

        t1.start()
        t2.start()

    def showContentEmptyX(self, x, y):
        threads = list()
        t1 = threading.Thread(target=self.showContentEmptyXLeft, args=(x, y))
        threads.append(t1)
        t2 = threading.Thread(target=self.showContentEmptyXRight, args=(x, y))
        threads.append(t2)

        t1.start()
        t2.start()

    def showContentEmptyY(self, x, y):
        threads = list()
        t1 = threading.Thread(target=self.showContentEmptyYTop, args=(x, y))
        threads.append(t1)
        t2 = threading.Thread(target=self.showContentEmptyYBottom, args=(x, y))
        threads.append(t2)

        t1.start()
        t2.start()

    def showContentEmptyXLeft(self, x, y):
        celd = self.map.celds[y][x]
        while not celd.showed and celd.content == 0 and self.map.difficultSelected.width > x >= 0:
            celd = self.map.celds[y][x]
            btn = self.btn_map[y][x]
            btn["text"], btn["fg"], btn["background"] = celd.content, celd.getColorByNumber(), "grey"
            x = x - 1

    def showContentEmptyXRight(self, x, y):
        celd = self.map.celds[y][x]
        while not celd.showed and celd.content == 0 and self.map.difficultSelected.width > x >= 0:
            celd = self.map.celds[y][x]
            btn = self.btn_map[y][x]
            btn["text"], btn["fg"], btn["background"] = celd.content, celd.getColorByNumber(), "grey"
            x = x + 1

    def showContentEmptyYTop(self, x, y):
        celd = self.map.celds[y][x]
        while not celd.showed and celd.content == 0 and self.map.difficultSelected.height > x >= 0:
            celd = self.map.celds[y][x]
            btn = self.btn_map[y][x]
            btn["text"], btn["fg"], btn["background"] = celd.content, celd.getColorByNumber(), "grey"
            y = y - 1

    def showContentEmptyYBottom(self, x, y):
        celd = self.map.celds[y][x]
        while not celd.showed and celd.content == 0 and self.map.difficultSelected.height > x >= 0:
            celd = self.map.celds[y][x]
            btn = self.btn_map[y][x]
            btn["text"], btn["fg"], btn["background"] = celd.content, celd.getColorByNumber(), "grey"
            y = y + 1

    def display_GameOver(self):
        gameOverWindow = Tk()
        gameOverWindow.title("Minesweeper")
        btn_GameOver = Button(gameOverWindow, text="Game Over!!!", command=gameOverWindow.destroy)
        btn_GameOver.pack()