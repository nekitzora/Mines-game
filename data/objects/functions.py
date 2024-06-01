# from . import *
# from .objects import *
from .objects import not_destroying_walls, destroying_walls, destroying_walls_mass
from .objects import enemies
from .objects import all_sprites
from .objects import all_walls
from .objects import player
from .objects import enemies
from .objects import bomb
from .objects import key
from .objects import d as door
from .objects import health_plus, bomb_plus
from .explosion import Explosion
from .wall import Wall
from .enemy import Enemy
import pygame
import random

# forbiden_x = []
# forbiden_y = []

import logging

logging.basicConfig(level=logging.DEBUG)

forbiden_coords = set()


def set_door():
    # random.randrange(1050, 1450, 50)
    x = random.randrange(1050, 1450, 50)
    y = random.randrange(50, 750, 100)
    while (x, y) in forbiden_coords:
        logging.debug(f"Forbiden coordinate ({x}, {y}) to door, generating again...")
        x = random.randrange(1050, 1450, 50)
        y = random.randrange(50, 750, 100)
    logging.debug(f"Door added in ({x}, {y})")
    forbiden_coords.add((x,y))
    logging.debug(f"----------------------------------------------------------------")
    spawn_door(door, x, y)

def spawn_door(door, x, y):
    door.rect.topleft = (x, y)


def set_walls():
    # not destroying walls
    

    # вверх
    for i in range(0, 1550, 50):
        wall = Wall(i, 0, False)
        not_destroying_walls.add(wall)
        forbiden_coords.add((i, 0))
    #     forbiden_x.append(i)
    # forbiden_y.append(0)


    # лево
    for i in range (50, 850, 50):
        wall = Wall(0, i, False)
        not_destroying_walls.add(wall)
        forbiden_coords.add((0, i))
    #     forbiden_y.append(i)
    # forbiden_x.append(0)

    # право
    for i in range(50, 850, 50):
        wall = Wall(1500, i, False)
        not_destroying_walls.add(wall)
        forbiden_coords.add((1500, i))
    #     forbiden_y.append(i)
    # forbiden_x.append(1500)

    # низ
    for i in range(50, 1550, 50):
        wall = Wall(i, 800, False)
        not_destroying_walls.add(wall)
        forbiden_coords.add((i, 800))
    #     forbiden_x.append(i)
    # forbiden_y.append(800)

    for y in range(100, 800, 100):
        for x in range(100, 1500, 100):
            wall = Wall(x, y, False)
            not_destroying_walls.add(wall)
            forbiden_coords.add((x, y))
            # forbiden_x.append(x)
            # forbiden_x.append(y)

    set_door()

    #destroying walls

    maximum = 50
    teritoria = random.randrange(1,3)
    for i in range(1, maximum):
        if teritoria == 1:
            x = random.randrange(150, 1500, 50)
            y = random.randrange(50, 800, 50)
        else:
            x = random.randrange(50, 1500, 50)
            y = random.randrange(150, 800, 50)
        
        # while (x in forbiden_x) or (y in forbiden_y):  # Check if x and y are both in forbidden lists
        #     if teritoria == 1:
        #         x = random.randrange(150, 1500, 50)
        #         y = random.randrange(50, 800, 50)
        #     else:
        #         x = random.randrange(50, 1500, 50)
        #         y = random.randrange(150, 800, 50)

        while (x, y) in forbiden_coords:  # Проверка, если (x, y) уже в запрещенных координатах
            logging.debug(f"Forbiden coordinate ({x}, {y}) to wall, generating again...")
            if teritoria == 1:
                x = random.randrange(150, 1500, 50)
                y = random.randrange(50, 800, 50)
            else:
                x = random.randrange(50, 1500, 50)
                y = random.randrange(150, 800, 50)

        logging.debug(f"Wall added in ({x}, {y})")
        wall = Wall(x, y, True)
        destroying_walls.add(wall)
        # forbiden_x.append(x)
        # forbiden_y.append(y)
        forbiden_coords.add((x, y))
        teritoria = random.randrange(1, 3)

    logging.debug(f"----------------------------------------------------------------")

    all_walls.add(not_destroying_walls, destroying_walls)

    for wall in destroying_walls:
        destroying_walls_mass.append(wall)



def set_enemy():
    maximum = 10
    have_key = random.randrange(1, maximum + 1)
    teritoria = random.randrange(1,3)
    for i in range(1, maximum + 1):
        if teritoria == 1:
            x = random.randrange(350, 1500, 50)
            y = random.randrange(50, 800, 50)
        else:
            x = random.randrange(50, 1500, 50)
            y = random.randrange(350, 800, 50)
        
        # while (x in forbiden_x) or (y in forbiden_y):  # Check if x and y are both in forbidden lists
        #     if teritoria == 1:
        #         x = random.randrange(150, 1500, 50)
        #         y = random.randrange(50, 800, 50)
        #     else:
        #         x = random.randrange(50, 1500, 50)
        #         y = random.randrange(150, 800, 50)

        while (x, y) in forbiden_coords:  # Проверка, если (x, y) уже в запрещенных координатах
            logging.debug(f"Forbiden coordinate ({x}, {y}) to enemy, generating again...")
            if teritoria == 1:
                x = random.randrange(350, 1500, 50)
                y = random.randrange(50, 800, 50)
            else:
                x = random.randrange(50, 1500, 50)
                y = random.randrange(350, 800, 50)

        logging.debug(f"Enemy added in ({x}, {y})")

        if i == have_key:
            enemy = Enemy(x, y, 5, True)
        else:
            enemy = Enemy(x, y, 5, False)
        enemies.add(enemy)
        forbiden_coords.add((x,y))
        # forbiden_x.append(x)
        # forbiden_y.append(y)  # Add enemy coordinates to forbidden lists to prevent other enemies from spawning here
        teritoria = random.randrange(1, 3)

    all_sprites.add(enemies)






def spawn_bomb(bomb, x, y):
    bomb.rect.topleft = (x, y)
    bomb.active = True  # Bomb is now active
    bomb.anim_count = 0  # Reset animation count
    bomb.explosion_directions = [(50, 0), (-50, 0), (0, 50), (0, -50)]  # Directions to check
    # bomb.steps_per_direction = [random.randint(1, 5) for _ in bomb.explosion_directions]  # Random steps for each direction
    bomb.current_direction = 0
    bomb.current_step = 1
    bomb.player_hit = False  # Reset player hit status for new bomb
    bomb.placed = True

def bomb_update(bomb):
    if bomb.active:
        bomb.anim_count += 1
        if bomb.anim_count == len(bomb.bomb_anim):
            bomb.anim_count = 0
            # if player.rect.colliderect(self.bomb_anim[13]):
            #     player.hp -= 1
            #     bomb.player_hit = True
            bomb.active = False  # Deactivate bomb after animation
        elif bomb.anim_count == 12:
            if player.rect.colliderect(bomb.rect):
                player.hp -= 1
                bomb.player_hit = True
        else:
            bomb.image = bomb.bomb_anim[bomb.anim_count]
    else:
        create_explosions(bomb)  # Create explosions sequentially

def create_explosions(bomb):
    if bomb.current_direction is not None:
        direction = bomb.explosion_directions[bomb.current_direction]
        x, y = bomb.rect.topleft
        pos_x = x + direction[0] * bomb.current_step
        pos_y = y + direction[1] * bomb.current_step
        if 0 <= pos_x <= 1500 and 0 <= pos_y <= 790:
            explosion = Explosion(pos_x, pos_y)
            bomb.explosions.add(explosion)
            if pygame.sprite.spritecollideany(explosion, all_walls):
                bomb.current_direction += 1
                bomb.current_step = 0
            else:
                collided_enemies = pygame.sprite.spritecollide(explosion, enemies, True)
                if collided_enemies:
                        for enemy in collided_enemies:
                            if enemy.have_key:
                                spawn_key(key, enemy.rect.x, enemy.rect.y)
                            luck = try_lucky()
                            if luck != 'nothing':
                                spawn_upgrate(luck, enemy.rect.x, enemy.rect.y)

                            enemies.remove(enemy)
                            enemy.kill()

                if not bomb.player_hit and pygame.sprite.collide_rect(explosion, player):
                    player.hp -= 1
                    bomb.player_hit = True  # Mark player as hit to prevent multiple deductions
                    if player.hp == 0:
                        player.dead = True

                bomb.current_step += 1
                if bomb.current_step > bomb.steps_per_direction:  # Use random steps per direction
                    bomb.current_direction += 1
                    bomb.current_step = 1
        else:
            bomb.current_direction += 1
            bomb.current_step = 1
        
        if bomb.current_direction >= len(bomb.explosion_directions):
            bomb.current_direction = None  # Stop creating explosions when done
            bomb.placed = False


def spawn_key(key, x, y):
    key.rect.topleft = (x, y)


def try_lucky():
    if random.randint(0, 100) < 25:  # 25% chance
        item_type = random.choice(['health', 'bomb'])
        return item_type
    else:
        return 'nothing'

def spawn_upgrate(what, x, y):
    if what == 'health':
        health_plus.rect.topleft = (x, y)
    else:
        bomb_plus.rect.topleft = (x, y)

def despawn_upgrate(what):
    what.rect.topleft = (-50, -50)
    if what.name == 'bomb':
        bomb.steps_per_direction += 1
    else:
        if player.hp < 4:
            player.hp += 1