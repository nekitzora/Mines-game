import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.explosion_anim = [
            pygame.image.load('data/pic/bomb/b11.png'),
            pygame.image.load('data/pic/bomb/b12.png'),
            pygame.image.load('data/pic/bomb/b13.png'),
            pygame.image.load('data/pic/bomb/b14.png'),
        ]
        self.image = self.explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.anim_count = 0
        self.active = True

    def update(self):
        if self.active:
            self.anim_count += 1
            if self.anim_count == len(self.explosion_anim):
                self.anim_count = 0
                self.active = False  # Deactivate explosion after animation
            else:
                self.image = self.explosion_anim[self.anim_count]