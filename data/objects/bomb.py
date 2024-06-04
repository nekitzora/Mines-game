import pygame
import random

# from .objects import player


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bomb_anim = [
            pygame.image.load('data/pic/bomb/b1.png'),
            pygame.image.load('data/pic/bomb/b2.png'),
            pygame.image.load('data/pic/bomb/b3.png'),
            pygame.image.load('data/pic/bomb/b4.png'),
            pygame.image.load('data/pic/bomb/b5.png'),
            pygame.image.load('data/pic/bomb/b6.png'),
            pygame.image.load('data/pic/bomb/b7.png'),
            pygame.image.load('data/pic/bomb/b8.png'),
            pygame.image.load('data/pic/bomb/b9.png'),
            pygame.image.load('data/pic/bomb/b10.png'),
            pygame.image.load('data/pic/bomb/b11.png'),
            pygame.image.load('data/pic/bomb/b12.png'),
            pygame.image.load('data/pic/bomb/b13.png'),
            pygame.image.load('data/pic/bomb/b14.png'),
        ]

        self.image = self.bomb_anim[0]
        self.rect = self.image.get_rect()
        self.anim_count = 0
        self.active = False
        self.explosions = pygame.sprite.Group()
        self.explosion_directions = []
        self.current_direction = None
        self.current_step = 0
        self.steps_per_direction = 1  # Random steps for each direction
        self.player_hit = False  # Track if the player has been hit
        self.placed = False
        self.rect.topleft = (-50, -50)
