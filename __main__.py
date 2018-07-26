
import pygame
import time
from images import picture
from board.board import Board
from board.map_type import MapType

easy = MapType("Easy", 8, 8, 10)
medium = MapType("Medium", 16, 16, 40)
hard = MapType("Hard", 16, 30, 99)
MAP_TYPE = easy

def intro():
    global MAP_TYPE

    screen = pygame.display.set_mode((400, 510))
    easy_button = picture.load_picture("images/difficulties/easy.png")
    easy_button = pygame.transform.scale(easy_button, (400, 170))
    start_easy_button = (0, 0)
    medium_button = picture.load_picture("images/difficulties/medium.png")
    medium_button = pygame.transform.scale(medium_button, (400, 170))
    start_medium_button = (0, 170)
    hard_button = picture.load_picture("images/difficulties/hard.png")
    hard_button = pygame.transform.scale(hard_button,  (400, 170))
    start_hard_button = (0, 340)

    screen.blit(easy_button, start_easy_button)
    screen.blit(medium_button, start_medium_button)
    screen.blit(hard_button, start_hard_button)

    pygame.display.flip()

    x_pressed, y_pressed = 0, 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if start_easy_button[1] + 170 >= y_pressed >= start_easy_button[1] and start_easy_button[0] + 400 >= x_pressed >= start_easy_button[0]:
                    MAP_TYPE = easy
                    running = False
                elif start_medium_button[1] + 170 >= y_pressed >= start_medium_button[1] and start_medium_button[0] + 400 >= x_pressed >= start_medium_button[0]:
                    MAP_TYPE = medium
                    running = False
                elif start_hard_button[1] + 170 >= y_pressed >= start_hard_button[1] and start_hard_button[0] + 400 >= x_pressed >= start_hard_button[0]:
                    MAP_TYPE = hard
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_pressed, y_pressed = pygame.mouse.get_pos()

def main():
    global MAP_TYPE
    board = Board(MAP_TYPE)
    screen = board.display_board_hide()

    width_pressed, height_pressed = 0, 0
    posX_pressed, posY_pressed = 0, 0
    running = True
    while running:
        for event in pygame.event.get():
            try:
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()

                    elif event.key == pygame.K_ESCAPE:
                        pass

                if not board.visible:
                    if event.type == pygame.MOUSEBUTTONUP:
                        button_pressed = board.matrix[posY_pressed][posX_pressed]
                        board.action(button_pressed, event, screen)

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        width_pressed = event.pos[0]
                        height_pressed = event.pos[1]

                        posX_pressed = int(width_pressed / 40)
                        posY_pressed = int(height_pressed / 40)

                        button_pressed = board.matrix[posY_pressed][posX_pressed]

                        if button_pressed.content.status_celd() == "Invisible":
                            pic = picture.get_picture(0)
                            pic = pygame.transform.scale(pic, (button_pressed.width, button_pressed.height))
                            screen.blit(pic, (button_pressed.x, button_pressed.y))
                            pygame.display.flip()
            except pygame.error:
                pass

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Minesweeper")
    pygame.display.set_icon(picture.get_picture("icon"))

    intro()
    main()

