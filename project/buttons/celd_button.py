
import pygame
from tkinter import *
from tkinter import messagebox
from buttons.button import Button

PICTURES = {}

class Celd_Button(Button):

    def __init__(self, celd, x, y, width, heigth):

        super().__init__(celd, x, y, width, heigth)

        global PICTURES
        self.charge_images()

        self.clicked = PICTURES.get(celd.content)
        self.unclicked = PICTURES.get("empty")
        self.unclicked = pygame.transform.scale(self.unclicked, (heigth, width))
        self.clicked = pygame.transform.scale(self.clicked, (heigth, width))


    def action(self, event = None):
        response = None

        if not event:
            if self.content.status_celd() == "Visible":
                self.content.show_content()
                response = self.clicked

            else:
                if self.content.content == 0:
                    response = "Display around"

        elif event.type == pygame.MOUSEBUTTONDOWN:
            response = self.unclicked = pygame.transform.scale(PICTURES.get(0), (self.height, self.width))

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_click = event.button

            if mouse_click == 1:
                if self.content.status_celd() == "Invisible":
                    if self.content.content == 0:
                        response = "Display around"
                    else:
                        if self.content.content == 9:
                            Tk().wm_withdraw()
                            messagebox.showinfo('Game Over...','Game Overrrr....')

                        self.content.show_content()
                        response = self.clicked

                elif self.content.status_celd() == "Visible":
                    response = "Display around"

            elif mouse_click == 3:
                status = self.content.right_click_action()

                if status == "Flag":
                    self.unclicked = PICTURES.get("flag")
                    response = self.unclicked = pygame.transform.scale(self.unclicked, (self.height, self.width))

                elif status == "Question":
                    self.unclicked = PICTURES.get("question")
                    response = self.unclicked = pygame.transform.scale(self.unclicked, (self.height, self.width))

                elif status == "Invisible":
                    self.unclicked = PICTURES.get("empty")
                    response = self.unclicked = pygame.transform.scale(self.unclicked, (self.height, self.width))

        return response

    def show_this(self):
        pass

    def load_image(self, url):
        try:
            image = pygame.image.load(url)
            image = image.convert()
        except pygame.error:
            raise SystemExit
        return image

    def charge_images(self):
        empty_not_visible = self.load_image("images/empty_not_visible.jpg")
        empty_visible = self.load_image("images/empty_visible.jpg")

        bomb = self.load_image("images/bomb.jpg")
        flag = self.load_image("images/flag.png")
        question = self.load_image("images/question.png")

        one = self.load_image("images/one.png")
        two = self.load_image("images/two.png")
        three = self.load_image("images/three.png")
        four = self.load_image("images/four.png")
        five = self.load_image("images/five.png")
        six = self.load_image("images/six.png")
        seven = self.load_image("images/seven.png")
        eight = self.load_image("images/eight.png")

        global PICTURES
        PICTURES = {
            "empty": empty_not_visible,
            0: empty_visible,
            9: bomb,
            "flag": flag,
            "question": question,
            1: one,
            2: two,
            3: three,
            4: four,
            5: five,
            6: six,
            7: seven,
            8: eight
        }

    def get_image(self, content):
        global PICTURES
        return PICTURES.get(content)