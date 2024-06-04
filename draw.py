import pygame
from data.objects import objects

def draw(screen):
    pygame.display.flip()
    screen.fill((0, 100, 0)) 

    #sprites
    objects.all_sprites.draw(screen)

    #door
    objects.door.draw(screen)

    #walls
    objects.destroying_walls.draw(screen)
    objects.not_destroying_walls.draw(screen)

    #player hp
    screen.blit(objects.player.hp_im[objects.player.hp], (1450, 0))
    
def draw_explosions(bomb, screen):
    bomb.explosions.update()
    bomb.explosions.draw(screen)