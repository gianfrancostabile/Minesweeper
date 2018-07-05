
class Celd(object):

    def __init__(self):
        self.content = 0

    def change_to_mine(self):
        self.content = -1

    def change_to_number(self, number):
        self.content = number

    def change_to_empty(self):
        self.content = 0
