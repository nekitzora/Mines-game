import pygame
import random

# from .objects import player


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bomb_anim = [
            pygame.image.load('data/pic/bomb/b1.png'),
            pygame.image.load('data/pic/bomb/b2.png'),
            pygame.image.load('data/pic/bomb/b3.png'),
            pygame.image.load('data/pic/bomb/b4.png'),
            pygame.image.load('data/pic/bomb/b5.png'),
            pygame.image.load('data/pic/bomb/b6.png'),
            pygame.image.load('data/pic/bomb/b7.png'),
            pygame.image.load('data/pic/bomb/b8.png'),
            pygame.image.load('data/pic/bomb/b9.png'),
            pygame.image.load('data/pic/bomb/b10.png'),
            pygame.image.load('data/pic/bomb/b11.png'),
            pygame.image.load('data/pic/bomb/b12.png'),
            pygame.image.load('data/pic/bomb/b13.png'),
            pygame.image.load('data/pic/bomb/b14.png'),
        ]

        self.image = self.bomb_anim[0]
        self.rect = self.image.get_rect()
        self.anim_count = 0
        self.active = False
        self.explosions = pygame.sprite.Group()
        self.explosion_directions = []
        self.current_direction = None
        self.current_step = 0
        self.steps_per_direction = []  # Random steps for each direction
        self.player_hit = False  # Track if the player has been hit
        self.placed = False
        self.rect.topleft = (-50, -50)



   

    # def create_explosions(self, walls, enemies, player):
    #     if self.current_direction is not None:
    #         direction = self.explosion_directions[self.current_direction]
    #         x, y = self.rect.topleft
    #         pos_x = x + direction[0] * self.current_step
    #         pos_y = y + direction[1] * self.current_step
    #         if 0 <= pos_x <= 1500 and 0 <= pos_y <= 790:  # Ensure within screen bounds
    #             explosion = Explosion(pos_x, pos_y)
    #             self.explosions.add(explosion)
    #             if pygame.sprite.spritecollideany(explosion, walls):  # Stop if a wall is hit
    #                 self.current_direction += 1
    #                 self.current_step = 0
    #             else:
    #                 # Check for collisions with enemies
    #                 collided_enemies = pygame.sprite.spritecollide(explosion, enemies, True)
    #                 if collided_enemies:
    #                     for enemy in collided_enemies:
    #                         if enemy.have_key:
    #                             self.killed_enemy_with_key = True
    #                             set_spawn_key()
    #                         enemies.remove(enemy)
    #                         enemy.kill()
                
    #                 # Check for collision with player
    #                 if not self.player_hit and pygame.sprite.collide_rect(explosion, player):
    #                     player.player.hp -= 1
    #                     self.player_hit = True  # Mark player as hit to prevent multiple deductions
    #                     if player.player.hp == 0:
    #                         player.dead = True

    #                 self.current_step += 1
    #                 if self.current_step > self.steps_per_direction[self.current_direction]:  # Use random steps per direction
    #                     self.current_direction += 1
    #                     self.current_step = 1
    #         else:
    #             self.current_direction += 1
    #             self.current_step = 1

    #         if self.current_direction >= len(self.explosion_directions):
    #             self.current_direction = None  # Stop creating explosions when done
    #             self.placed = False


    # def draw_explosions(self, screen):
    #     self.explosions.update()
    #     self.explosions.draw(screen)








    # def spawn(self, x, y):
    #     self.rect.topleft = (x, y)
    #     self.active = True  # Bomb is now active
    #     self.anim_count = 0  # Reset animation count
    #     self.explosion_directions = [(50, 0), (-50, 0), (0, 50), (0, -50)]  # Directions to check
    #     self.steps_per_direction = [random.randint(1, 5) for _ in self.explosion_directions]  # Random steps for each direction
    #     self.current_direction = 0
    #     self.current_step = 1
    #     self.player_hit = False  # Reset player hit status for new bomb
    #     self.placed = True



     # def update(self, player, walls, enemies):
    #     if self.active:
    #         self.anim_count += 1
    #         if self.anim_count == len(self.bomb_anim):
    #             self.anim_count = 0
    #             # if player.rect.colliderect(self.bomb_anim[13]):
    #             #     player.hp -= 1
    #             #     bomb.player_hit = True
    #             self.active = False  # Deactivate bomb after animation
    #         elif self.anim_count == 12:
    #             if player.rect.colliderect(self.rect):
    #                 player.hp -= 1
    #                 self.player_hit = True
    #         else:
    #             self.image = self.bomb_anim[self.anim_count]
    #     else:
    #         self.create_explosions(walls, enemies, player)  # Create explosions sequentially