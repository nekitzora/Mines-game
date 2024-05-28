import pygame
import random

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        super().__init__()
        self.x = x
        self.y = y
        self.picked = False
        self.image = pygame.image.load('pic/key/KEY.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


kluch = Key(1300, 680)

keys = pygame.sprite.Group()
keys.add(kluch)