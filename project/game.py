
import pygame
import sys
from board import Board

def main(board):
    screen = board.display_board()
    pygame.display.flip()


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                width_pressed = event.pos[0]
                height_pressed = event.pos[1]

                posX_pressed = int(width_pressed / 40)
                posY_pressed = int(height_pressed / 40)

                button_pressed = board.matrix[posY_pressed][posX_pressed]
                board.action(button_pressed, event, screen)


def reveal_neighbours(board, celd):
    y = len(board.matrix)
    x = len(board.matrix[0])


if __name__ == "__main__":
    pygame.init()
    board = Board()
    main(board)

