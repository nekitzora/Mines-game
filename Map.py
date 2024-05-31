import pygame
import random
from classes.wall import Wall
from classes.player import Player
from classes.enemy import Enemy

not_destroying_walls = pygame.sprite.Group()
destroying_walls = pygame.sprite.Group()
destroying_walls_mass = []
all_walls = pygame.sprite.Group()
player = Player(50, 50, 10)
enemies = pygame.sprite.Group()
keys = pygame.sprite.Group()


# kluch = Key(1300, 680)

# keys = pygame.sprite.Group()
# keys.add(kluch)


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

    teritoria = random.randrange(1,3)
    for i in range(1, 50):
        if teritoria == 1:
            wall = Wall(random.randrange(150, 1500, 50), random.randrange(50, 800, 50), True)
            destroying_walls.add(wall)
        else:
            wall = Wall(random.randrange(50, 1500, 50), random.randrange(150, 800, 50), True)
            destroying_walls.add(wall)
        teritoria = random.randrange(1,3)



    maximum = 6
    have_key = random.randrange(1, maximum + 1)
    teritoria = random.randrange(1,3)
    for i in range(1, maximum + 1):
        
        if teritoria == 1:
            x = random.randrange(150, 1500, 50)
            y = random.randrange(50, 800, 50)
        else:
            x = random.randrange(50, 1500, 50)
            y = random.randrange(150, 800, 50)


        if i == have_key:
            enemy = Enemy(x, y, 10 ,True)
        else:
            enemy = Enemy(x, y, 10, False)
        enemies.add(enemy)


    # d_wall1 = Wall(random.randrange(50, 1450, 50), random.randrange(50, 750, 100), True)
    # d_wall2 = Wall(random.randrange(50, 1450, 50), random.randrange(50, 750, 100), True)
    # d_wall3 = Wall(random.randrange(50, 1450, 50), random.randrange(50, 750, 100), True)
    # d_wall4 = Wall(random.randrange(50, 1450, 50), random.randrange(50, 750, 100), True)

    

    for wall in destroying_walls:
        destroying_walls_mass.append(wall)

    all_walls.add(not_destroying_walls, destroying_walls)




def print_map(screen):
    # all_walls.draw(screen)
    destroying_walls.draw(screen)
    not_destroying_walls.draw(screen)