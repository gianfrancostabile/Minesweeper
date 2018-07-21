
class MapType(object):

    def __init__(self, difficult, y, x, bombs):
        self.difficult = difficult
        self.y = y
        self.x = x
        self.bombs = bombs

    def __repr__(self):
        return "({}) {}x{} - {} bombs.".format(self.difficult, str(self.y), str(self.x), str(self.bombs))