import pygame
# import data
from data.objects.functions import *
from data.objects.objects import *
import draw
clock = pygame.time.Clock()

set_walls()
set_enemy()


def game(screen):
    gaming = True
    while gaming:
        
        # move
        klavisha = pygame.key.get_pressed()
        player.move(klavisha, all_walls)
        for enemy in enemies:
            enemy.move(all_walls)
        
        #draw
        draw.draw(screen)


        #checks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                pygame.quit()
        
        if klavisha[pygame.K_SPACE] and bomb.placed == False:
            spawn_bomb(bomb, player.rect.x, player.rect.y)
            all_sprites.add(bomb)
            # spawn_key(kluch, player.rect.x, player.rect.y)

        if bomb.active:
            bomb_update(bomb)
        elif not bomb.active:
            create_explosions(bomb)
            draw.draw_explosions(bomb, screen)
            for explosion in bomb.explosions:
                collided_walls = pygame.sprite.spritecollide(explosion, all_walls, False)
                for wall in collided_walls:
                    if wall in destroying_walls_mass:
                        all_walls.remove(wall)
                        destroying_walls_mass.remove(wall)
                        wall.kill()
            if all(not explosion.active for explosion in bomb.explosions):
                bomb.explosions.empty()  # Clear all explosion sprites
                all_sprites.remove(bomb)  # Remove bomb sprite

        # if bomb.killed_enemy_with_key:
        #     for enemy in enemies:
        #         if enemy.have_key:
        #             kluch = Key(enemy.x, enemy.y)
        #             keys.add(kluch)
        #             all_sprites.add(keys)


        #frame
        if gaming:
            clock.tick(15)