
import pygame
from board import Board
from buttons.celd_button import Celd_Button

BUTTON_LIST = []

def main():
    global BUTTON_LIST
    board = Board()

    posX, posY = 0, 0
    square_side = 40

    y = len(board.matrix)
    x = len(board.matrix[0])

    BUTTON_LIST = [[y] * x for i in range(x)]

    pos_height = y * square_side
    pos_width = x * square_side

    screen = pygame.display.set_mode((pos_width, pos_height))

    for i in range(y):
        for j in range(x):
            celd = board.matrix[i][j]

            new_button = Celd_Button(celd, posX, posY, square_side, square_side)
            BUTTON_LIST[i][j] = new_button

            screen.blit(new_button.unclicked, (posY, posX))
            posX += 40
        posY += 40
        posX = 0

    pygame.display.flip()


    status = True
    while status:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                width_pressed = event.pos[0]
                height_pressed = event.pos[1]

                posX_pressed = int(width_pressed / 40)
                posY_pressed = int(height_pressed / 40)

                button_pressed = BUTTON_LIST[posY_pressed][posX_pressed]
                response = button_pressed.action(event)

                if isinstance(response, str):
                    if response == "Display around":
                        countX, countY = 0, 0
                        x2, y2 = posX_pressed-1, posY_pressed-1

                        while countY < 3:
                            while countX < 3:
                                if y > y2 >= 0 and x > x2 >= 0:
                                    btn_around = BUTTON_LIST[y2][x2]

                                    if btn_around.content.status_celd() == "Invisible":
                                        response = btn_around.clicked
                                        screen.blit(response, (btn_around.x, btn_around.y))

                                countX += 1
                                x2 += 1
                            countY += 1
                            y2 += 1
                            countX = 0
                            x2 = posX_pressed-1

                elif isinstance(response, pygame.Surface):
                    screen.blit(response, (button_pressed.x, button_pressed.y))

                pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    main()

