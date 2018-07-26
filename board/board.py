
import pygame, os
from tkinter import *
from tkinter import messagebox
from random import randint
from .celd import Celd
from buttons.celd_button import Celd_Button
from images import picture

os.environ['SDL_VIDEO_CENTERED'] = '1'

STACK_REVEAL = list()

class Board(object):

    def __init__(self, map_type):
        self.create_empty_map(map_type)
        self.put_bombs(map_type.bombs)
        self.put_numbers()
        self.visible = False
        self.difficult_selected = map_type

    def create_empty_map(self, difficult):
        self.matrix = [[difficult.y] * difficult.x for i in range(difficult.y)]

        for y in range(difficult.y):
            for x in range(difficult.x):
                side = 40
                posX = x * side
                posY = y * side

                new_celd = Celd(y, x)
                self.matrix[y][x] = Celd_Button(new_celd, posX, posY, side, side)

    def put_bombs(self, amount_mines):
        i = 0
        while i < amount_mines:
            y = randint(0, len(self.matrix) - 1)
            x = randint(0, len(self.matrix[y]) - 1)

            if not self.matrix[y][x].content.is_bomb():
                self.matrix[y][x].put_bomb()
                i += 1

    def put_numbers(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                bombs = self.amount_bombs_around(self.matrix[y][x])
                if 9 > bombs > -1:
                    self.matrix[y][x].put_number(bombs)


    def amount_bombs_around(self, button):
        bombs = -1
        celd = button.content

        if not celd.is_bomb():
            x, y = celd.x - 1, celd.y - 1
            bombs, counterY, counterX = 0, 0, 0

            for i in range(3):
                for j in range(3):
                    if len(self.matrix) > y >= 0 and len(self.matrix[0]) > x >= 0:
                        if self.matrix[y][x].content.is_bomb():
                            bombs += 1
                    x += 1
                y += 1
                x = celd.x - 1

        return bombs

    def display_board_hide(self):
        self.visible = False

        square_side = 40

        y = len(self.matrix)
        x = len(self.matrix[0])

        pos_height = y * square_side
        pos_width = x * square_side

        screen = pygame.display.set_mode((pos_width, pos_height))

        for i in range(y):
            for j in range(x):
                celd_button = self.matrix[i][j]
                screen.blit(celd_button.unclicked, (celd_button.x, celd_button.y))

        pygame.display.flip()
        return screen

    def display_board_visible(self):
        self.visible = True
        square_side = 40

        y = len(self.matrix)
        x = len(self.matrix[0])

        pos_height = y * square_side
        pos_width = x * square_side

        screen = pygame.display.set_mode((pos_width, pos_height))

        for i in range(y):
            for j in range(x):
                celd_button = self.matrix[i][j]
                screen.blit(celd_button.clicked, (celd_button.x, celd_button.y))

        pygame.display.flip()
        return screen

    def action(self, button, event, screen):
        mouse_click = event.button

        if mouse_click == 1:
            self.reveal(button, screen)
            self.verify_victory()

        elif mouse_click == 3:
            if not button.content.visible:
                status = button.content.right_click_action()

                if status == "Flag":
                    button.unclicked = picture.get_picture("flag")
                elif status == "Question":
                    button.unclicked = picture.get_picture("question")
                elif status == "Invisible":
                    button.unclicked = picture.get_picture("empty")

                button.unclicked = pygame.transform.scale(button.unclicked, (button.width, button.height))
                screen.blit(button.unclicked, (button.x, button.y))
                pygame.display.flip()
                self.verify_victory()

    def reveal(self, button, screen):
        global STACK_REVEAL
        STACK_REVEAL.append(button)

        celd = button.content
        if celd.status_celd() == "Invisible":
            button.reveal()
            screen.blit(button.clicked, (button.x, button.y))
            pygame.display.flip()

            if celd.is_empty():
                self.reveal_neighbours(button, screen)

        elif celd.status_celd() == "Visible" and 2 > len(STACK_REVEAL) >= 0:
            self.reveal_neighbours(button, screen)

        STACK_REVEAL.remove(button)

    def reveal_neighbours(self, button, screen):
        celd = button.content
        posX, posY = celd.x - 1, celd.y - 1

        len_matrix_y = len(self.matrix)
        len_matrix_x = len(self.matrix[0])

        for y in range(3):
            for x in range(3):
                if len_matrix_y > posY >= 0 and len_matrix_x > posX >= 0:
                    neighbour = self.matrix[posY][posX]
                    self.reveal(neighbour, screen)
                posX += 1
            posY += 1
            posX = celd.x - 1

    def game_over(self):
        Tk().wm_withdraw()
        messagebox.showinfo('', "Game over. Press (R) to restart - Press (ESC) to change difficulty")

    def victory(self):
        Tk().wm_withdraw()
        messagebox.showinfo('', "VICTORY!!!")

    def verify_victory(self):
        bombs = self.difficult_selected.bombs
        counterBombs, celdsRevealed = 0, 0
        maxRevealed = (len(self.matrix) * len(self.matrix[0])) - bombs
        victory = True

        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                celd = self.matrix[y][x].content

                if celd.status_celd() == "Visible":
                    if celd.is_bomb():
                        victory = False
                        break
                    else:
                        celdsRevealed += 1
                else:
                    if celd.is_bomb():
                        counterBombs += 1

        if counterBombs == bombs and celdsRevealed == maxRevealed and victory:
            self.victory()
        elif not victory:
            self.display_board_visible()
            self.game_over()

