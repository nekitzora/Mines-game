import pygame
import draw
import main 

from data.objects.functions import *
from data.objects.objects import *

pygame.init()
clock = pygame.time.Clock()

def game(screen):

    set_walls()
    set_enemy()
    set_player()
    set_music()

    gaming = True
    paused = False
    font = pygame.font.Font("data/pic/fonts/joystix monospace.otf", 36)
    game_over_font = pygame.font.Font("data/pic/fonts/joystix monospace.otf", 100)
    win_font = pygame.font.Font("data/pic/fonts/joystix monospace.otf", 100)

    enter_pressed = False  
    game_over = False 
    win = False  

    return_rect = None
    menu_rect = None

    while gaming:
        if not sound_arena.played:    
            sound_arena.sound.play(-1)
            sound_arena.change_played()

        if not win and not game_over:
            klavisha = pygame.key.get_pressed()
        if not paused: 
            player.move(klavisha, all_walls, door) 
            for enemy in enemies:
                enemy.move(all_walls, door)
        
        draw.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                    enter_pressed = False  
                elif event.key == pygame.K_RETURN: 
                    if not enter_pressed:
                        enter_pressed = True
                    else:
                        paused = not paused
                        enter_pressed = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_rect and return_rect.collidepoint(pygame.mouse.get_pos()):
                    paused = False

                if menu_rect and menu_rect.collidepoint(pygame.mouse.get_pos()):
                    paused = False
                    game_over = False
                    win = False
                    gaming = False
                    sound_arena.sound.stop()
                    delete_all()
                    despawn_player()
                    sound_loss.sound.stop()
                    sound_win.sound.stop()
                    main.main()

                if game_over or win:
                    if menu_rect and menu_rect.collidepoint(event.pos):
                        paused = False
                        game_over = False
                        win = False
                        gaming = False
                        sound_arena.sound.stop()
                        delete_all()
                        despawn_player()
                        sound_loss.sound.stop()
                        sound_win.sound.stop()
                        main.main()

        if paused:
            pause_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            pause_surface.fill((0, 0, 0, 128))
            screen.blit(pause_surface, (0, 0))
                
            return_text = font.render("Return", True, (255, 255, 255))
            menu_text = font.render("Menu", True, (255, 255, 255))
            return_rect = return_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            menu_rect = menu_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

            if return_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (100, 100, 100), return_rect)
            elif menu_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (100, 100, 100), menu_rect)

            screen.blit(return_text, return_rect)
            screen.blit(menu_text, menu_rect)

        if klavisha[pygame.K_SPACE] and not bomb.placed and not paused:
            spawn_bomb(bomb, player.rect.x, player.rect.y)
            all_sprites.add(bomb)

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
                bomb.explosions.empty()
                all_sprites.remove(bomb)

        if pygame.sprite.spritecollideany(player, keys):
            key.picked = True
            all_sprites.remove(key)
            keys.remove(key)

        if key.picked:
            d.change_open()
            d.opened = True

        if player.escaped and not sound_win.played:
            win = True
            sound_arena.sound.stop()  
            sound_win.sound.play() 
            sound_win.played = True

        what = pygame.sprite.spritecollideany(player, upgrades)
        if what:
            despawn_upgrate(what)
            
        if player.hp == 0 and not sound_loss.played:
            game_over = True
            sound_arena.sound.stop()
            sound_loss.sound.play()
            sound_loss.played = True

        if pygame.sprite.spritecollideany(player, enemies) and not enemy.player_hit:
            player.hp -= 1
            enemy.player_hit = True
            sound_damage.sound.play()

        if not pygame.sprite.spritecollideany(player, enemies):
            enemy.player_hit = False

        if game_over or win:
            despawn_player()

        if game_over and gaming:
            game_over_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            game_over_surface.fill((0, 0, 0, 128))
            screen.blit(game_over_surface, (0, 0))
            
            game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
            menu_text = font.render("Menu", True, (255, 255, 255))
            game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            menu_rect = menu_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))

            if menu_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (100, 100, 100), menu_rect)

            screen.blit(game_over_text, game_over_rect)
            screen.blit(menu_text, menu_rect)


        if win and gaming:
            win_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            win_surface.fill((0, 0, 0, 128))
            screen.blit(win_surface, (0, 0))
            
            win_text = win_font.render("You Win!", True, (0, 255, 0))
            menu_text = font.render("Menu", True, (255, 255, 255))
            win_rect = win_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            menu_rect = menu_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))

            if menu_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (100, 100, 100), menu_rect)

            screen.blit(win_text, win_rect)
            screen.blit(menu_text, menu_rect)
      
        if gaming:
            clock.tick(15)
        
if __name__ == "__main__":
    screen = pygame.display.set_mode((1550, 850))
    sound_arena = GameSound("data/sound/arena.mp3")
    game(screen)
