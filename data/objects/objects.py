# from . import *
from .bomb import Bomb
from .door import Door
from .enemy import Enemy
from .player import Player
from .wall import Wall
from .key import Key
from .upgrades import *
from .sound import GameSound

import pygame
import random

# ennf = E
pygame.mixer.init()
sound_bomb = GameSound('data/sound/bomb.mp3')
sound_damage = GameSound('data/sound/damage.mp3')
sound_arena = GameSound('data/sound/arena.mp3')


player = Player(50, 50, 10)



enemies = pygame.sprite.Group()


all_sprites = pygame.sprite.Group()
all_sprites.add(player)


not_destroying_walls = pygame.sprite.Group()
destroying_walls = pygame.sprite.Group()
destroying_walls_mass = []
all_walls = pygame.sprite.Group()


d = Door()
# all_walls.add(d)
door = pygame.sprite.Group()
door.add(d)

bomb = Bomb()

key = Key()
keys = pygame.sprite.Group()
keys.add(key)
all_sprites.add(key)


bomb_plus = Bomb_plus()
health_plus = Health_plus()
upgrades = pygame.sprite.Group()
upgrades.add(bomb_plus, health_plus)
all_sprites.add(upgrades)