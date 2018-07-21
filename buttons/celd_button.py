
import pygame
from images import picture
from .button import Button

class Celd_Button(Button):

    def __init__(self, celd, x, y, width, height):

        super().__init__(celd, x, y, width, height)

        picture.charge_pictures()

        self.clicked = picture.get_picture(celd.content)
        self.clicked = pygame.transform.scale(self.clicked, (height, width))
        self.unclicked = picture.get_picture("empty")
        self.unclicked = pygame.transform.scale(self.unclicked, (height, width))

    def action(self, event):
        pass

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