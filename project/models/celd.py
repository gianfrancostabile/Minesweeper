
class Celd(object):

    def __init__(self, x, y):
        self.content = 0
        self.x = x
        self.y = y

    def change_to_mine(self):
        self.content = -1

    def change_to_number(self, number):
        self.content = number

    def change_to_empty(self):
        self.content = 0

    def getColorByNumber(self):
        color = "lavender"

        if self.content == -1:
            color = "black"
        elif self.content == 1:
            color = "deep sky blue"
        elif self.content == 2:
            color = "lime green"
        elif self.content == 3:
            color = "red"
        elif self.content == 4:
            color = "navy"
        elif self.content == 5:
            color = "firebrick"
        elif self.content == 6:
            color = "magenta"
        elif self.content == 7:
            color = "sienna"
        elif self.content == 8:
            color = "snow3"

        return color