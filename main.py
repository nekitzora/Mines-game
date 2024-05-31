import pygame
import game


pygame.init()
pygame.display.set_caption("Game")
icon = pygame.image.load('data/pic/main_image.jpeg')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1550, 850))

game.game(screen)





