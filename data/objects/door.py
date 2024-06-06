import pygame
import random

class Door(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.opened = False
        self.image = pygame.image.load('data/pic/door/door_closed.png')
        self.x = -50
        self.y = -50
        self.rect = self.image.get_rect()
        self.rect.topleft = (-50, -50)

    def change_open(self):
        self.image = pygame.image.load('data/pic/door/door_opened.png')

    def change_close(self):
        self.image = pygame.image.load('data/pic/door/door_closed.png')


