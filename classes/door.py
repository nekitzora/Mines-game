import pygame
import random

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.opened = False
        self.image = pygame.image.load('pic/door/door_closed.png')
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change(self):
        self.image = pygame.image.load('pic/door/door_opened.png')


door = Door(random.randrange(1050, 1450, 50), random.randrange(50, 750, 100))