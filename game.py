import pygame
import random
def game():
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode((1500, 790))

    player = pygame.image.load('THINGS AND PARTICLESS/b1.png')
    player_x = 100
    player_y = 100

    player_speed = 3

    enemy = pygame.image.load('THINGS AND PARTICLESS/b6.png')
    enemy_x = int(random.randrange(60,1390))
    enemy_y = int(random.randrange(60,680))
    enemy_speed = 10
    k = int(random.randrange(1,4))
    granica = 0
    limit = int(random.randrange(0,1000))

    gaming = True
    while gaming:
        screen.fill((0, 0, 0))
        screen.blit(player, (player_x, player_y))
        screen.blit(enemy, (enemy_x, enemy_y))
        player_rect = player.get_rect(topleft=(player_x, player_y))
        enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))

        

        
        if granica == limit:
            k = int(random.randrange(1,4))
            granica = 0
            limit = int(random.randrange(0,50))
        
        if k == 1 and granica < limit and enemy_x <= 1400:
            enemy_x += enemy_speed
            if enemy_x == 1400:
              k = int(random.randrange(1,4))  
            
        elif k == 2 and granica < limit and enemy_x >= 50:
            enemy_x -= enemy_speed
            if enemy_x == 50:
              k = int(random.randrange(1,4)) 
            
        elif k == 3 and granica < limit and enemy_y <= 690:
            enemy_y += enemy_speed
            if enemy_y == 690:
              k = int(random.randrange(1,4)) 
            
        elif k == 4 and granica < limit and enemy_y >= 50:
            enemy_y -= enemy_speed
            if enemy_y == 50:
              k = int(random.randrange(1,4)) 
            
        granica += 1



        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif key[pygame.K_RIGHT] and player_x < 1400:
            player_x += player_speed
        elif key[pygame.K_UP] and player_y > 50:
            player_y -= player_speed
        elif key[pygame.K_DOWN] and player_y < 690:
            player_y += player_speed

        
        #pygame.display.update()
        pygame.display.flip()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                pygame.quit()

        if player_rect.colliderect(enemy_rect):
            gaming = False
            pygame.quit()

        clock.tick(60)