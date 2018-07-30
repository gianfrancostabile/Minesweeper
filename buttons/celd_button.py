
import pygame
from images import picture

class CeldButton(object):

    def __init__(self, celd, x, y, width, height):
        self.content = celd
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        button_clicked = picture.get_picture(celd.content)
        self.clicked = pygame.transform.scale(button_clicked, (height, width))
        button_unclicked = picture.get_picture("empty")
        self.unclicked = pygame.transform.scale(button_unclicked, (height, width))

    def reveal(self):
        return self.content.reveal()

    def put_bomb(self):
        self.content.put_bomb()
        self.clicked = picture.get_picture(9)
        self.clicked = pygame.transform.scale(self.clicked, (self.height, self.width))

    def put_number(self, number):
        self.content.put_number(number)
        self.clicked = picture.get_picture(number)
        self.clicked = pygame.transform.scale(self.clicked, (self.height, self.width))