import pygame
import draw
import main 

from data.objects.functions import *
from data.objects.objects import *

pygame.init()
clock = pygame.time.Clock()

set_walls()
set_enemy()

def game(screen):

    gaming = True
    paused = False
    font = pygame.font.Font("data/pic/fonts/joystix monospace.otf", 36)

    enter_pressed = False  # Флаг для отслеживания нажатия клавиши Enter

    while gaming:
        if not sound_arena.played:    
            sound_arena.sound.play(-1)
            sound_arena.change_played()
        
        klavisha = pygame.key.get_pressed()
        player.move(klavisha, all_walls, door)
        for enemy in enemies:
            enemy.move(all_walls, door)
        
        draw.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                    enter_pressed = False  # Сброс флага при нажатии ESCAPE
                elif event.key == pygame.K_RETURN:  # Проверка нажатия клавиши Enter
                    if not enter_pressed:  # Если клавиша Enter не была нажата ранее
                        enter_pressed = True
                    else:  # Если клавиша Enter была нажата ранее
                        paused = not paused
                        enter_pressed = False  # Сброс флага при нажатии ENTER
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_rect.collidepoint(pygame.mouse.get_pos()):
                    paused = False
                elif menu_rect.collidepoint(pygame.mouse.get_pos()):
                    paused = False
                    sound_arena.stop()  # Остановка музыки
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

            pygame.display.flip()

        if klavisha[pygame.K_SPACE] and bomb.placed == False:
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
            screen.fill((0, 0, 0))  # Очистим экран
            lose_font = pygame.font.Font(None, 100)
            lose_text = lose_font.render("YOU LOSE", True, (255, 0, 0))
            restart_text = font.render("Restart", True, (255, 255, 255))
            menu_text = font.render("Menu", True, (255, 255, 255))
            lose_rect = lose_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
            restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            menu_rect = menu_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
            screen.blit(lose_text, lose_rect)
            screen.blit(restart_text, restart_rect)
            screen.blit(menu_text, menu_rect)
            pygame.display.flip()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_rect.collidepoint(pygame.mouse.get_pos()):
                            # Перезапуск игры
                            game(screen)
                        elif menu_rect.collidepoint(pygame.mouse.get_pos()):
                            # Возврат в главное меню
                            sound_arena.stop()  # Остановка музыки
                            main.main()

        if pygame.sprite.spritecollideany(player, enemies) and not enemy.player_hit:
            player.hp -= 1
            enemy.player_hit = True
            sound_damage.sound.play()

        if not pygame.sprite.spritecollideany(player, enemies):
            enemy.player_hit = False

        if gaming:
            clock.tick(15)

if __name__ == "__main__":
    screen = pygame.display.set_mode((1550, 850))
    sound_arena = GameSound("data/sound/arena.mp3")
    game(screen) 
