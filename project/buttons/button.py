from abc import *

ID = 0

class Button(ABC):

    def __init__(self, content, x, y, width, heigth, unclicked = None, clicked = None):
        global ID

        self.id = ID

        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = heigth
        self.unclicked = unclicked
        self.clicked = clicked

        ID += 1

    @abstractmethod
    def action(self, event):
        pass
