import pygame
import random
from classes.wall import walls
from classes.enemy import enemies
from classes.player import player


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bomb_anim = [
            pygame.image.load('pic/bomb/b1.png'),
            pygame.image.load('pic/bomb/b2.png'),
            pygame.image.load('pic/bomb/b3.png'),
            pygame.image.load('pic/bomb/b4.png'),
            pygame.image.load('pic/bomb/b5.png'),
            pygame.image.load('pic/bomb/b6.png'),
            pygame.image.load('pic/bomb/b7.png'),
            pygame.image.load('pic/bomb/b8.png'),
            pygame.image.load('pic/bomb/b9.png'),
            pygame.image.load('pic/bomb/b10.png'),
            pygame.image.load('pic/bomb/b11.png'),
            pygame.image.load('pic/bomb/b12.png'),
            pygame.image.load('pic/bomb/b13.png'),
            pygame.image.load('pic/bomb/b14.png'),
        ]

        self.image = self.bomb_anim[0]
        self.rect = self.image.get_rect()
        self.anim_count = 0
        self.active = False
        self.explosions = pygame.sprite.Group()
        self.explosion_directions = []
        self.current_direction = None
        self.current_step = 0
        self.walls = walls  # Store the walls group
        self.enemies = enemies  # Store the enemies group
        self.player = player  # Store the player sprite
        self.steps_per_direction = []  # Random steps for each direction
        self.player_hit = False  # Track if the player has been hit

    def spawn(self, x, y):
        self.rect.topleft = (x, y)
        self.active = True  # Bomb is now active
        self.anim_count = 0  # Reset animation count
        self.explosion_directions = [(50, 0), (-50, 0), (0, 50), (0, -50)]  # Directions to check
        self.steps_per_direction = [random.randint(1, 5) for _ in self.explosion_directions]  # Random steps for each direction
        self.current_direction = 0
        self.current_step = 1
        self.player_hit = False  # Reset player hit status for new bomb

    def update(self):
        if self.active:
            self.anim_count += 1
            if self.anim_count == len(self.bomb_anim):
                self.anim_count = 0
                # if player.rect.colliderect(self.bomb_anim[13]):
                #     player.hp -= 1
                #     bomb.player_hit = True
                self.active = False  # Deactivate bomb after animation
            elif self.anim_count == 12:
                if player.rect.colliderect(self.rect):
                    player.hp -= 1
                    bomb.player_hit = True
            else:
                self.image = self.bomb_anim[self.anim_count]
        else:
            self.create_explosions()  # Create explosions sequentially

    def create_explosions(self):
        if self.current_direction is not None:
            direction = self.explosion_directions[self.current_direction]
            x, y = self.rect.topleft
            pos_x = x + direction[0] * self.current_step
            pos_y = y + direction[1] * self.current_step
            if 0 <= pos_x <= 1500 and 0 <= pos_y <= 790:  # Ensure within screen bounds
                explosion = Explosion(pos_x, pos_y)
                self.explosions.add(explosion)
                if pygame.sprite.spritecollideany(explosion, self.walls):  # Stop if a wall is hit
                    self.current_direction += 1
                    self.current_step = 0
                else:
                    # Check for collisions with enemies
                    collided_enemies = pygame.sprite.spritecollide(explosion, self.enemies, True)
                    if collided_enemies:
                        for enemy in collided_enemies:
                            self.enemies.remove(enemy)
                            enemy.kill()
                
                    # Check for collision with player
                    if not self.player_hit and pygame.sprite.collide_rect(explosion, self.player):
                        self.player.hp -= 1
                        self.player_hit = True  # Mark player as hit to prevent multiple deductions
                        if self.player.hp == 0:
                            global gaming
                            gaming = False

                    self.current_step += 1
                    if self.current_step > self.steps_per_direction[self.current_direction]:  # Use random steps per direction
                        self.current_direction += 1
                        self.current_step = 1
            else:
                self.current_direction += 1
                self.current_step = 1

            if self.current_direction >= len(self.explosion_directions):
                self.current_direction = None  # Stop creating explosions when done


    def draw_explosions(self, screen):
        self.explosions.update()
        self.explosions.draw(screen)



class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.explosion_anim = [
            pygame.image.load('pic/bomb/b11.png'),
            pygame.image.load('pic/bomb/b12.png'),
            pygame.image.load('pic/bomb/b13.png'),
            pygame.image.load('pic/bomb/b14.png'),
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




bomb = Bomb()