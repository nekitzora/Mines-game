import pygame
from classes.wall import Wall



def build_map(screen = None):
    walls = pygame.sprite.Group()

    wall1 = Wall(550, 550, False)
    wall2 = Wall(350, 350, False)
    wall3 = Wall(600, 200, True)




    walls.add(wall1, wall2, wall3)

    destroying_walls = []
    for wall in walls:
        if wall.destroying == False:
            destroying_walls.append(wall)
    if screen != None:
        walls.draw(screen)

    return destroying_walls