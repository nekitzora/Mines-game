import pygame
import random


# def load_anim(direction, appearance):
#     if direction == 'back':
#         if appearance == 'normal':
#             result = [
#                 pygame.image.load('data/pic/sprites/enemy/normal/back/down.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/back/middle.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/back/up.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/back/middle.png'),
#             ]
#             return result
#         else:
#             result = [
#                 pygame.image.load('data/pic/sprites/enemy/not normal/back/1.png'),
#                 pygame.image.load('data/pic/sprites/enemy/not normal/back/2.png'),
#                 pygame.image.load('data/pic/sprites/enemy/not normal/back/3.png'),
#             ]
#             return result
#     elif direction == 'front':
#         if appearance == 'normal':
#             result = [
#                 pygame.image.load('data/pic/sprites/enemy/normal/front/down.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/front/middle.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/front/up.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/front/middle.png'),
#             ]
#             return result
#         else:
#             result = [
#                 pygame.image.load('data/pic/sprites/enemy/not normal/front/1.png'),
#                 pygame.image.load('data/pic/sprites/enemy/not normal/front/2.png'),
#                 pygame.image.load('data/pic/sprites/enemy/not normal/front/3.png'),
#             ]
#             return result
#     elif direction == 'left':
#         if appearance == 'normal':
#             result = [
#                 pygame.image.load('data/pic/sprites/enemy/normal/left/down.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/left/middle.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/left/up.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/left/middle.png'),
#             ]
#             return result
#         else:
#             result = [
#                 pygame.image.load('data/pic/sprites/enemy/not normal/left/1.png'),
#                 pygame.image.load('data/pic/sprites/enemy/not normal/left/2.png'),
#                 pygame.image.load('data/pic/sprites/enemy/not normal/left/3.png'),
#             ]
#             return result
#     elif direction == 'right':
#         if appearance == 'normal':
#             result = [
#                 pygame.image.load('data/pic/sprites/enemy/normal/right/down.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/right/middle.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/right/up.png'),
#                 pygame.image.load('data/pic/sprites/enemy/normal/right/middle.png'),
#             ]
#             return result
#         else:
#             result = [
#                 pygame.image.load('data/pic/sprites/enemy/not normal/right/1.png'),
#                 pygame.image.load('data/pic/sprites/enemy/not normal/right/2.png'),
#                 pygame.image.load('data/pic/sprites/enemy/not normal/right/3.png'),
#             ]
#             return result
                
            

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, have_key):
        super().__init__()
        # self.appearance = random.randrange(1, 100)
        
        
        self.walk_back = [
            pygame.image.load('data/pic/sprites/enemy/normal/back/down.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/back/middle.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/back/up.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/back/middle.png'),
        ]
        self.walk_front = [
            pygame.image.load('data/pic/sprites/enemy/normal/front/down.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/front/middle.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/front/up.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/front/middle.png'),
        ]
        self.walk_left = [
            pygame.image.load('data/pic/sprites/enemy/normal/left/down.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/left/middle.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/left/up.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/left/middle.png'),
        ]
        self.walk_right = [
            pygame.image.load('data/pic/sprites/enemy/normal/right/down.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/right/middle.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/right/up.png'),
            pygame.image.load('data/pic/sprites/enemy/normal/right/middle.png'),
        ]

        # if self.appearance <= 80:
        #     self.walk_back = load_anim('back', 'normal')
        #     self.walk_front = load_anim('front', 'normal')
        #     self.walk_left = load_anim('left', 'normal')
        #     self.walk_right = load_anim('right', 'normal')
        # else:
        #     self.walk_back = load_anim('back', 'not normal')
        #     self.walk_front = load_anim('front', 'not normal')
        #     self.walk_left = load_anim('left', 'not normal')
        #     self.walk_right = load_anim('right', 'not normal')

       
        self.image = self.walk_front[0]
        
        self.speed = speed
        # self.x = random.randrange(50, 1450, 50)
        # self.y = random.randrange(50, 750, 100)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.storona = int(random.randrange(1,5))
        self.krok = 0
        self.limit = int(random.randrange(50, 200, 50))
        self.anim_count = 0
        self.player_hit = False
        self.have_key = have_key

    # def set_spawn(self):
        


    def move(self, walls, door):
        if self.krok >= self.limit:
            self.storona = int(random.randrange(1, 5))
            self.krok = 0
            self.limit = int(random.randrange(50, 200, 50))

        dx = dy = 0

        if self.storona == 1:
            dx = -self.speed
            self.image = self.walk_left[self.anim_count]
        elif self.storona == 2:
            dx = self.speed
            self.image = self.walk_right[self.anim_count]
        elif self.storona == 3:
            dy = -self.speed
            self.image = self.walk_back[self.anim_count]
        elif self.storona == 4:
            dy = self.speed
            self.image = self.walk_front[self.anim_count]

        self.anim_count = (self.anim_count + 1) % len(self.walk_left)


        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls) or pygame.sprite.spritecollideany(self, door):
            self.rect.x -= dx
            self.storona = int(random.randrange(1, 5))

        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls) or pygame.sprite.spritecollideany(self, door):
            self.rect.y -= dy
            self.storona = int(random.randrange(1, 5))

        self.krok += 1




