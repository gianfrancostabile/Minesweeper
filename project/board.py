from random import randint
from celd import Celd
from map_type import MapType

class Board(object):

    def __init__(self):
        map_type = MapType("Easy", 9, 9, 10)
        self.create_empty_map(map_type)
        self.put_mines(map_type.bombs)
        self.put_numbers()

    def create_empty_map(self, difficult):
        self.matrix = [[difficult.y] * difficult.x for i in range(difficult.x)]
        for y in range(difficult.y):
            for x in range(difficult.x):
                self.matrix[y][x] = Celd(y, x)

    def put_mines(self, amount_mines):
        i = 0
        while i < amount_mines:
            y = randint(0, len(self.matrix) - 1)
            x = randint(0, len(self.matrix[y]) - 1)

            if not self.matrix[y][x].is_bomb():
                self.matrix[y][x].put_bomb()
                i += 1

    def put_numbers(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                bombs = self.amount_bombs_around(self.matrix[y][x])
                if 9 > bombs > -1:
                    self.matrix[y][x].put_number(bombs)

    def amount_bombs_around(self, celd):
        bombs = -1

        if not celd.is_bomb():
            x, y = celd.x - 1, celd.y - 1
            bombs, counterY, counterX = 0, 0, 0

            while counterY < 3:
                while counterX < 3:
                    if len(self.matrix) > y >= 0 and len(self.matrix[y]) > x >= 0:
                        if self.matrix[y][x].is_bomb():
                            bombs += 1
                    counterX += 1
                    x += 1
                counterY += 1
                y += 1
                counterX = 0
                x = celd.x - 1

        return bombs
