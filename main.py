import pygame

from game import game
from maps.Map import build_map

pygame.init()
pygame.display.set_caption("Game")
icon = pygame.image.load('pic/main_image.jpeg')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1500, 790))

build_map(screen)
game(screen)
#main_menu()





