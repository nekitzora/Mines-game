import pygame
from Map import enemies
from classes.bomb import bomb
# import random

class Key(pygame.sprite.Sprite):
    def __init__(self, x = -50, y = -50):
        super().__init__()
        self.x = x
        self.y = y
        self.picked = False
        self.image = pygame.image.load('pic/key/KEY.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def set_kluch_spawn(self):
        if bomb.killed_enemy_with_key:
            for enemy in enemies:
                if enemy.have_key:
                    self.x = enemy.x
                    self.y = enemy.y

kluch = Key()