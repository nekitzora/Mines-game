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
        if not sound_arena.played:    
            sound_arena.sound.play(-1)
            sound_arena.change_played()
        
        # move
        klavisha = pygame.key.get_pressed()
        player.move(klavisha, all_walls, door)
        for enemy in enemies:
            enemy.move(all_walls, door)
        
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

        if bomb.active:
            bomb_update(bomb)
        elif not bomb.active:
            # sound_bomb.play()
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
                bomb.explosions.empty()
                all_sprites.remove(bomb)

        if pygame.sprite.spritecollideany(player, keys):
            key.picked = True
            all_sprites.remove(key)

        if key.picked:
            d.change()
            d.opened = True

        if player.escaped:
            gaming = False
            pygame.quit()


        what = pygame.sprite.spritecollideany(player, upgrades)
        if what:
            despawn_upgrate(what)
        
        if player.hp == 0:
            gaming = False
            pygame.quit()

        if pygame.sprite.spritecollideany(player, enemies) and not enemy.player_hit:
            player.hp -= 1
            enemy.player_hit = True
            sound_damage.sound.play()

        if not pygame.sprite.spritecollideany(player, enemies):
            enemy.player_hit = False


        #frame
        if gaming:
            clock.tick(15)