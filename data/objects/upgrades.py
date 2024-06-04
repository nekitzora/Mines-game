import pygame

class Bomb_plus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/pic/upgrades/bomb.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (-50, -50)
        self.name = 'bomb'


class Health_plus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/pic/upgrades/health.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (-50, -50)
        self.name = 'health'