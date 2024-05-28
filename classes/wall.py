import pygame

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



