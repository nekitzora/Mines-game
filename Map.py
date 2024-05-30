import pygame
import random
from classes.wall import Wall

not_destroying_walls = pygame.sprite.Group()
destroying_walls = pygame.sprite.Group()
destroying_walls_mass = []
all_walls = pygame.sprite.Group()

def build_map(screen):
    

    # not destroying walls
    

    # вверх
    for i in range(0, 1550, 50):
        wall = Wall(i, 0, False)
        not_destroying_walls.add(wall)

    # лево
    for i in range (50, 850, 50):
        wall = Wall(0, i, False)
        not_destroying_walls.add(wall)

    # право
    for i in range(50, 850, 50):
        wall = Wall(1500, i, False)
        not_destroying_walls.add(wall)

    # низ
    for i in range(50, 1550, 50):
        wall = Wall(i, 800, False)
        not_destroying_walls.add(wall)

    for y in range(100, 800, 100):
        for x in range(100, 1500, 100):
            wall = Wall(x, y, False)
            not_destroying_walls.add(wall)

    

    #destroying walls

    d_wall1 = Wall(random.randrange(50, 1450, 50), random.randrange(50, 750, 100), True)
    d_wall2 = Wall(random.randrange(50, 1450, 50), random.randrange(50, 750, 100), True)
    d_wall3 = Wall(random.randrange(50, 1450, 50), random.randrange(50, 750, 100), True)
    d_wall4 = Wall(random.randrange(50, 1450, 50), random.randrange(50, 750, 100), True)

    destroying_walls.add(d_wall1, d_wall2, d_wall3, d_wall4)

    for wall in destroying_walls:
        destroying_walls_mass.append(wall)

    all_walls.add(not_destroying_walls, destroying_walls)




def print_map(screen):
    all_walls.draw(screen)