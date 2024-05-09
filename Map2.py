import pygame

def build_map(screen):
    # Ініціалізація Pygame
    pygame.init()

    # Розміри вікна
    screen_width, screen_height = 1500, 790
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mines 2D")

    # Початкові значення камери
    camera_x = 0
    map_right_boundary = 1900

    # Завантаження зображення фону
    background_image = pygame.image.load("MAP BUILDING/PLATE1.png")
    background_width, background_height = background_image.get_rect().size

    # Завантаження зображення стіни
    wall_image = pygame.image.load("MAP BUILDING/Wall.png")
    wall_width, wall_height = wall_image.get_rect().size

    # Флаги для визначення стану натискання клавіш
    moving_left = False
    moving_right = False

    # Список стін з координатами
    walls = [(3, 3), (5, 5), (7, 7)]  # Додайте потрібні координати стін

    # Головний цикл гри
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                elif event.key == pygame.K_d:
                    moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                elif event.key == pygame.K_d:
                    moving_right = False

        # Переміщення камери
        if moving_left:
            if camera_x > 0:
                camera_x -= 50
        elif moving_right:
            if camera_x < map_right_boundary - screen_width:
                camera_x += 50

        # Рендеринг фону
        num_tiles_x = screen.get_width() // background_width + 8
        num_tiles_y = screen.get_height() // background_height + 1

        for i in range(num_tiles_x):
            for j in range(num_tiles_y):
                tile_x = camera_x // background_width + i
                tile_y = j
                screen.blit(background_image, (i * background_width - camera_x, j * background_height))

                # Розміщення стін на краях арени
                if (i == 0 or i == num_tiles_x - 1 or j == 0 or j == num_tiles_y - 1) and (tile_x, tile_y) not in walls:
                    screen.blit(wall_image, (i * background_width - camera_x, j * background_height))
                elif i == num_tiles_x - 1 and j == num_tiles_y - 1 and (tile_x, tile_y) not in walls:
                    screen.blit(wall_image, (i * background_width - camera_x, j * background_height))

        # Оновлення екрану
        pygame.display.flip()

    # Завершення Pygame
    pygame.quit()

