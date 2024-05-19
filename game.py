import pygame
import random

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('MAP BUILDING/Destroing Wall.png')
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        



class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, speed):
        super().__init__()
        self.image = pygame.image.load('THINGS AND PARTICLESS/b1.png')
        self.x = start_x
        self.y = start_y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x, start_y)

    def move(self,walls):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_LEFT] and self.rect.x > 50:
            dx = -self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 1400:
            dx = self.speed
        if keys[pygame.K_UP] and self.rect.y > 50:
            dy = -self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 690:
            dy = self.speed

        # Предварительное перемещение
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= dx

        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.y -= dy




class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load('THINGS AND PARTICLESS/b6.png')
        self.x = int(random.randrange(60,1390))
        self.y = int(random.randrange(60,680))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.storona = int(random.randrange(1,4))
        self.krok = 0
        self.limit = int(random.randrange(0,100))





    def move(self, walls):


        if self.krok == self.limit:
            self.storona = int(random.randrange(1,4))
            self.krok = 0
            self.limit = int(random.randrange(0,50))

        dx = dy = 0

        if self.storona == 1 and self.krok < self.limit and self.rect.x > 50:
            dx = -self.speed
        if self.storona == 2 and self.krok < self.limit and self.rect.x < 1400:
            dx = self.speed
        if self.storona == 3 and self.krok < self.limit and self.rect.y > 50:
            dy = -self.speed
        if self.storona == 4 and self.krok < self.limit and self.rect.y < 690:
            dy = self.speed

        # Предварительное перемещение
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls):
            if self.rect.x == 1400 or self.rect.x == 50:
                self.storona = int(random.randrange(1,4))
            self.rect.x -= dx
        

        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls):
            if self.rect.x == 1400 or self.rect.x == 50:
                self.storona = int(random.randrange(1,4))
            self.rect.y -= dy

        self.krok += 1



def game():
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode((1500, 790))
    
    
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    player = Player(100, 100, 5)
    

    enemy = Enemy(10)

    all_sprites.add(player, enemy)
    

    wall1 = Wall(550, 550)
    wall2 = Wall(350, 350)
    walls.add(wall1, wall2)
    all_sprites.add(wall1, wall2)

    gaming = True
    while gaming:
        
        screen.fill((0, 0, 0))
        
        player.move(walls)
        enemy.move(walls)
        all_sprites.draw(screen)
        
  
        pygame.display.flip()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                pygame.quit()

        

        clock.tick(60)