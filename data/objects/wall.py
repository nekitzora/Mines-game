import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, destroying):
        super().__init__()
        image_destr = pygame.image.load('data/pic/wall/destroying_wall.png')
        image_ndestr = pygame.image.load('data/pic/wall/wall.png')
        if destroying:
            self.image = image_destr
            # self.destroying = True
        else:
            self.image = image_ndestr
            # self.destroying = False
        self.destroying = destroying
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)



