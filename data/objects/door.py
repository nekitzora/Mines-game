import pygame
import random

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.opened = False
        self.image = pygame.image.load('data/pic/door/door_closed.png')
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change(self):
        self.image = pygame.image.load('data/pic/door/door_opened.png')


