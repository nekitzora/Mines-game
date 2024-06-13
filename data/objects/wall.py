import pygame
import random

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, destroying):
        super().__init__()
        # image_destr = pygame.image.load('data/pic/wall/destroying_wall.png')
        # image_ndestr = pygame.image.load('data/pic/wall/wall.png')
        image_destr = [
            pygame.image.load('data/pic/wall/destroying/default.png'),
            pygame.image.load('data/pic/wall/destroying/default2.png'),
            pygame.image.load('data/pic/wall/destroying/default3.png'),
            pygame.image.load('data/pic/wall/destroying/default4.png'),            
            pygame.image.load('data/pic/wall/destroying/fury2.png'),
            pygame.image.load('data/pic/wall/destroying/neviem.png'),
            pygame.image.load('data/pic/wall/destroying/smile.png'),
            pygame.image.load('data/pic/wall/destroying/forever.png'),
            pygame.image.load('data/pic/wall/destroying/dota2.png'),
            pygame.image.load('data/pic/wall/destroying/fury.png'),
        ]
        image_ndestr = [
            pygame.image.load('data/pic/wall/not destroying/default.png'),
            pygame.image.load('data/pic/wall/not destroying/lian.png'),
            pygame.image.load('data/pic/wall/not destroying/tresk.png'),
            pygame.image.load('data/pic/wall/not destroying/look.png'),
            pygame.image.load('data/pic/wall/not destroying/slay.png'),
            pygame.image.load('data/pic/wall/not destroying/bomberman.png'),
        ]
        if destroying:
            if random.randint(0, 100) <= 95:
                self.image = image_destr[random.randrange(0,4)]
            else:
                self.image = image_destr[random.randrange(4,10)]
        else:
            if random.randint(0, 100) <= 95:
                if random.randint(0, 100) <= 70:
                    self.image = image_ndestr[0]
                else:
                    self.image = image_ndestr[random.randrange(1,3)]
            else:
                self.image = image_ndestr[random.randrange(3,6)]
        self.destroying = destroying
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)



