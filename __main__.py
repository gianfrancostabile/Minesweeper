
import pygame
from images import picture
from board.board import Board

def main():
    board = Board()
    screen = board.display_board_hide()

    try:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()

                elif event.type == pygame.MOUSEBUTTONUP and not board.visible:
                    width_pressed = event.pos[0]
                    height_pressed = event.pos[1]

                    posX_pressed = int(width_pressed / 40)
                    posY_pressed = int(height_pressed / 40)

                    button_pressed = board.matrix[posY_pressed][posX_pressed]

                    board.action(button_pressed, event, screen)

                elif event.type == pygame.MOUSEBUTTONDOWN and not board.visible:
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
    main()

