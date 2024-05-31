import pygame

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
        self.hp = 4
        self.hp_im = [
            pygame.image.load('pic/sprites/heart/0.png'),
            pygame.image.load('pic/sprites/heart/1.png'),
            pygame.image.load('pic/sprites/heart/2.png'),
            pygame.image.load('pic/sprites/heart/3.png'),
            pygame.image.load('pic/sprites/heart/4.png'),
        ]
        self.hp_image = self.hp_im[self.hp]
        self.dead = False
        

    def move(self, key, walls):
        
        dx = dy = 0

        if key[pygame.K_LEFT]:
            dx = -self.speed
            self.image = self.walk_left[self.anim_count]
            self.anim_count += 1
            if self.anim_count >= len(self.walk_left):
                self.anim_count = 0
        if key[pygame.K_RIGHT]:
            dx = self.speed
            self.image = self.walk_right[self.anim_count]
            self.anim_count += 1
            if self.anim_count >= len(self.walk_right):
                self.anim_count = 0
        if key[pygame.K_UP]:
            dy = -self.speed
            self.image = self.walk_back[self.anim_count]
            self.anim_count += 1
            if self.anim_count >= len(self.walk_back):
                self.anim_count = 0
        if key[pygame.K_DOWN]:
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





