import pygame
import time
import menu

def main_menu(screen):
    menu.main_menu(screen)

def main():
    pygame.init()

    pygame.display.set_caption("Game")
    icon = pygame.image.load('data/pic/main_image.jpeg')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((1550, 850))

    main_menu(screen)

    pygame.quit()

if __name__ == "__main__":
    main()





