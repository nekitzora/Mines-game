import pygame

from Map import player
# from classes.wall import destroying_walls as walls_mass
# from maps.Map import build_map
from Map import destroying_walls_mass as walls_mass
from Map import keys
from classes.key import kluch as keyy
from Map import enemies
from classes.door import door
from classes.bomb import bomb
# from classes.wall import walls
from Map import all_walls as walls
from Map import print_map



def game(screen):
    clock = pygame.time.Clock()
    # pygame.init()

    all_sprites = pygame.sprite.Group()
    

    
    
    

    all_sprites.add(player, enemies)
    
    all_sprites.add(door)

    # destroying_wall = build_map()

    gaming = True
    while gaming:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and bomb.placed == False:
            bomb.spawn(player.rect.x, player.rect.y)
            all_sprites.add(bomb)

        screen.fill((0, 100, 0)) 
        
        player.move(key, walls)

        for enemy in enemies:
            enemy.move(walls)

        if bomb.active:
            bomb.update()
        elif not bomb.active:
            bomb.create_explosions()
            bomb.draw_explosions(screen)
            for explosion in bomb.explosions:
                collided_walls = pygame.sprite.spritecollide(explosion, walls, False)
                for wall in collided_walls:
                    if wall in walls_mass:
                        walls.remove(wall)
                        walls_mass.remove(wall)
                        wall.kill()
            if all(not explosion.active for explosion in bomb.explosions):
                bomb.explosions.empty()  # Clear all explosion sprites
                all_sprites.remove(bomb)  # Remove bomb sprite

        all_sprites.draw(screen)
        print_map(screen)

        screen.blit(player.hp_im[player.hp], (1400, 100))
        
        if pygame.sprite.spritecollideany(player, keys):
            keyy.picked = True
            door.opened = True

        if not keyy.picked:
            keys.draw(screen)

        if door.opened:
            door.change()

        # if pygame.sprite.spritecollideany(player, enemies) and not enemy.player_hit:
        #     player.hp -= 1
        #     enemy.player_hit = True

        if not pygame.sprite.spritecollideany(player, enemies):
            enemy.player_hit = False

        if player.hp == 0:
            player.dead = True

        

        pygame.display.flip()

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                pygame.quit()

        if pygame.sprite.collide_rect(player, door) and door.opened:
            gaming = False
            pygame.quit()

        if player.dead:
            gaming = False
            pygame.quit()

        if gaming:
            clock.tick(10)
