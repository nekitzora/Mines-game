import pygame
import random

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, destroying):
        super().__init__()
        if destroying:
            self.image = pygame.image.load('pic/wall/destroying_wall.png')
            # self.destroying = True
        else:
            self.image = pygame.image.load('pic/wall/wall.png')
            # self.destroying = False
        self.destroying = destroying
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        
        
        



class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, speed):
        super().__init__()
        self.walk_left = [
            pygame.image.load('pic/sprites/player/left_going/1.png'),
            pygame.image.load('pic/sprites/player/left_going/2.png')
        ]
        self.walk_right = [
            pygame.image.load('pic/sprites/player/right_going/1.png'),
            pygame.image.load('pic/sprites/player/right_going/2.png')
        ]
        self.walk_front = [
            pygame.image.load('pic/sprites/player/going_front/1.png'),
            pygame.image.load('pic/sprites/player/going_front/2.png')
        ]
        self.walk_back = [
            pygame.image.load('pic/sprites/player/back_going/1.png'),
            pygame.image.load('pic/sprites/player/back_going/2.png')
        ]
        self.stay = [
            pygame.image.load('pic/sprites/player/stay/front.png'),
            pygame.image.load('pic/sprites/player/stay/back.png'),
            pygame.image.load('pic/sprites/player/stay/left.png'),
            pygame.image.load('pic/sprites/player/stay/right.png')
        ]
        self.image = self.stay[0]
        self.x = start_x
        self.y = start_y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x, start_y)
        self.anim_count = 0
        

    def move(self, key, walls):
        
        dx = dy = 0

        if key[pygame.K_LEFT] and self.rect.x > 50:
            dx = -self.speed
            self.image = self.walk_left[self.anim_count]
            self.anim_count += 1
            if self.anim_count >= len(self.walk_left):
                self.anim_count = 0
        if key[pygame.K_RIGHT] and self.rect.x < 1400:
            dx = self.speed
            self.image = self.walk_right[self.anim_count]
            self.anim_count += 1
            if self.anim_count >= len(self.walk_right):
                self.anim_count = 0
        if key[pygame.K_UP] and self.rect.y > 50:
            dy = -self.speed
            self.image = self.walk_back[self.anim_count]
            self.anim_count += 1
            if self.anim_count >= len(self.walk_back):
                self.anim_count = 0
        if key[pygame.K_DOWN] and self.rect.y < 690:
            dy = self.speed
            self.image = self.walk_front[self.anim_count]
            self.anim_count += 1
            if self.anim_count >= len(self.walk_front):
                self.anim_count = 0
            
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= dx
            if key[pygame.K_LEFT]:
                self.image = self.stay[2]
            elif key[pygame.K_RIGHT]:
                self.image = self.stay[3]

        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.y -= dy
            if key[pygame.K_UP]:
                self.image = self.stay[1]
            elif key[pygame.K_DOWN]:
                self.image = self.stay[0]




class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.walk_back = [
            pygame.image.load('pic/sprites/enemy/back/down.png'),
            pygame.image.load('pic/sprites/enemy/back/middle.png'),
            pygame.image.load('pic/sprites/enemy/back/up.png'),
            pygame.image.load('pic/sprites/enemy/back/middle.png'),
        ]
        self.walk_front = [
            pygame.image.load('pic/sprites/enemy/front/down.png'),
            pygame.image.load('pic/sprites/enemy/front/middle.png'),
            pygame.image.load('pic/sprites/enemy/front/up.png'),
            pygame.image.load('pic/sprites/enemy/front/middle.png'),
        ]
        self.walk_left = [
            pygame.image.load('pic/sprites/enemy/left/down.png'),
            pygame.image.load('pic/sprites/enemy/left/middle.png'),
            pygame.image.load('pic/sprites/enemy/left/up.png'),
            pygame.image.load('pic/sprites/enemy/left/middle.png'),
        ]
        self.walk_right = [
            pygame.image.load('pic/sprites/enemy/right/down.png'),
            pygame.image.load('pic/sprites/enemy/right/middle.png'),
            pygame.image.load('pic/sprites/enemy/right/up.png'),
            pygame.image.load('pic/sprites/enemy/right/middle.png'),
        ]
        self.image = self.walk_front[0]
        self.x = int(random.randrange(60,1390))
        self.y = int(random.randrange(60,680))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.storona = int(random.randrange(1,5))
        self.krok = 0
        self.limit = int(random.randrange(0,100))
        self.anim_count = 0


    def move(self, walls):
        if self.krok >= self.limit:
            self.storona = int(random.randrange(1, 5))
            self.krok = 0
            self.limit = int(random.randrange(0, 50))

        dx = dy = 0

        if self.storona == 1 and self.rect.x > 50:
            dx = -self.speed
            self.image = self.walk_left[self.anim_count]
        elif self.storona == 2 and self.rect.x < 1400:
            dx = self.speed
            self.image = self.walk_right[self.anim_count]
        elif self.storona == 3 and self.rect.y > 50:
            dy = -self.speed
            self.image = self.walk_back[self.anim_count]
        elif self.storona == 4 and self.rect.y < 690:
            dy = self.speed
            self.image = self.walk_front[self.anim_count]

        self.anim_count = (self.anim_count + 1) % len(self.walk_left)


        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= dx
            self.storona = int(random.randrange(1, 5))

        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.y -= dy
            self.storona = int(random.randrange(1, 5))

        self.krok += 1



def game():
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Game")
    icon = pygame.image.load('pic/main_image.jpeg')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((1500, 790))
    
    
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    player = Player(100, 100, 10)
    

    enemy = Enemy(10)
    enemy2 = Enemy(10)

    enemys = []

    enemys.append(enemy)
    enemys.append(enemy2)

    all_sprites.add(player, enemy, enemy2)
    

    wall1 = Wall(550, 550, False)
    wall2 = Wall(350, 350, False)
    walls.add(wall1, wall2)
    all_sprites.add(wall1, wall2)

    gaming = True
    while gaming:
        key = pygame.key.get_pressed()
        
        screen.fill((0, 0, 0))
        
        player.move(key, walls)

        for enemy in enemys:
            enemy.move(walls)
        all_sprites.draw(screen)
        
  
        pygame.display.flip()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                pygame.quit()

        

        clock.tick(10)