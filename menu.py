import pygame



# Функція для відображення головного меню
def main_menu():

    # Ініціалізація Pygame
    pygame.init()

    # Розміри вікна
    screen_width, screen_height = 1500, 790
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main menu")

    icon = pygame.image.load("Main_Image.jpeg")
    pygame.display.set_icon(icon)

    # Кольори
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Завантаження фонового зображення
    background_menu = pygame.image.load("MENU/BACKROUND_MENU.jpeg")
    background_menu = pygame.transform.scale(background_menu, (screen_width, screen_height))
    running = True
    
    while running:
        screen.blit(background_menu, (0, 0))  # Відображення фонового зображення

        # Текст "Головне меню"
        font = pygame.font.SysFont(None, 60)
        text = font.render("Main menu", True, BLACK)
        text_rect = text.get_rect(center=(screen_width // 2, 100))
        screen.blit(text, text_rect)

        # Створення кнопок
        button_width, button_height = 250, 50
        start_button = pygame.Rect((screen_width - button_width) // 2, 200, button_width, button_height)
        about_button = pygame.Rect((screen_width - button_width) // 2, 270, button_width, button_height)
        controls_button = pygame.Rect((screen_width - button_width) // 2, 340, button_width, button_height)
        how_to_play_button = pygame.Rect((screen_width - button_width) // 2, 410, button_width, button_height)
        owner_button = pygame.Rect((screen_width - button_width) // 2, 480, button_width, button_height)

        # Кнопка "Почати гру"
        pygame.draw.rect(screen, BLACK, start_button)
        text = font.render("Почати гру", True, WHITE)
        text_rect = text.get_rect(center=start_button.center)
        screen.blit(text, text_rect)

        # Кнопка "About us"
        pygame.draw.rect(screen, BLACK, about_button)
        text = font.render("About us", True, WHITE)
        text_rect = text.get_rect(center=about_button.center)
        screen.blit(text, text_rect)

        # Кнопка "Controls"
        pygame.draw.rect(screen, BLACK, controls_button)
        text = font.render("Controls", True, WHITE)
        text_rect = text.get_rect(center=controls_button.center)
        screen.blit(text, text_rect)

        # Кнопка "How to play"
        pygame.draw.rect(screen, BLACK, how_to_play_button)
        text = font.render("How to play", True, WHITE)
        text_rect = text.get_rect(center=how_to_play_button.center)
        screen.blit(text, text_rect)

        # Кнопка "Owner"
        pygame.draw.rect(screen, BLACK, owner_button)
        text = font.render("Owner", True, WHITE)
        text_rect = text.get_rect(center=owner_button.center)
        screen.blit(text, text_rect)

        # Оновлення екрану
        pygame.display.flip()

        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if about_button.collidepoint(mouse_pos):
                    # Оновлення екрану з текстом "Ми студенти ТУКЕ"
                    screen.fill(WHITE)
                    about_text = font.render("Ми студенти ТУКЕ", True, BLACK)
                    text_rect = about_text.get_rect(center=(screen_width // 2, screen_height // 2))
                    screen.blit(about_text, text_rect)
                    pygame.display.flip()

                    # Цикл для очікування натискання кнопки Enter
                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                waiting = False

# Виклик функції для відображення головного меню
#main_menu()
