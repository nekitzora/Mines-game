import pygame
import random

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
        self.player_hit = False


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


enemy1 = Enemy(10)
enemy2 = Enemy(10)
enemy3 = Enemy(10)
enemy4 = Enemy(10)


enemies = pygame.sprite.Group()
enemies.add(enemy1,enemy2,enemy3,enemy4)

