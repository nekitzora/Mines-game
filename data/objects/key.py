import pygame
# import random

class Key(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.picked = False
        self.image = pygame.image.load('data/pic/key/key.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (-50, -50)


