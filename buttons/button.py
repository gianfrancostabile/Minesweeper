

class Button(object):

    def __init__(self, content, x, y, width, heigth, unclicked = None, clicked = None):
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = heigth
        self.unclicked = unclicked
        self.clicked = clicked

    def action(self, event):
        pass
