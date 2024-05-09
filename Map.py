import pygame
import os

def build_map(screen, walls=[]):
    # Завантаження зображення фону
    background_image = pygame.image.load("MAP BUILDING/PLATE1.png")

    # Завантаження зображення стіни
    wall_image = pygame.image.load("MAP BUILDING/Wall.png")

    # Завантаження анімації бомби
    bomb_animation = load_bomb_animation()

    # Розмір зображення фону
    background_width, background_height = background_image.get_rect().size

    # Розмір зображення стіни
    wall_width, wall_height = wall_image.get_rect().size

    # Кількість зображень фону по горизонталі і вертикалі
    num_tiles_x = screen.get_width() // background_width + 1
    num_tiles_y = screen.get_height() // background_height + 1

    # Рендеринг фону
    for i in range(num_tiles_x):
        for j in range(num_tiles_y):
            screen.blit(background_image, (i * background_width, j * background_height))

            # Розміщення стін на краях арени
            if i == 0 or j == 0 or i == num_tiles_x - 1 or j == num_tiles_y - 1:
                screen.blit(wall_image, (i * background_width, j * background_height))

    # Рендеринг власних стін
    for wall_pos in walls:
        screen.blit(wall_image, (wall_pos[0] * background_width, wall_pos[1] * background_height))

    # Відображення анімації бомби
    for frame in bomb_animation:
        screen.blit(background_image, (4 * background_width, 4 * background_height))  # Очистка попереднього кадру
        screen.blit(frame, (4 * background_width, 4 * background_height))
        pygame.display.flip()  # Оновлення екрану після кожного кадру
        pygame.time.delay(100)  # Затримка між кадрами для анімації

    # Очищення анімації після завершення
    screen.blit(background_image, (4 * background_width, 4 * background_height))
    pygame.display.flip()

# Функція для завантаження анімації бомби
def load_bomb_animation():
    bomb_animation = []
    for i in range(1, 15):
        image_path = os.path.join("THINGS AND PARTICLESS", f"b{i}.png")
        bomb_animation.append(pygame.image.load(image_path))
    return bomb_animation
