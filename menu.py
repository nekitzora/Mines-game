import pygame
import time
import math
import game

def main_menu(screen):
    pygame.mixer.init()

    screen_width, screen_height = 1550, 850
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bomberman")

    icon = pygame.image.load("data/pic/main_image.jpeg")
    pygame.display.set_icon(icon)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_COLOR = (50, 50, 50)
    BUTTON_HOVER_COLOR = (70, 70, 70)
    ARROW_COLOR = (255, 255, 255)

    background_menu = pygame.image.load("data/pic/background/mainmenu.png")
    background_menu = pygame.transform.scale(background_menu, (screen_width, screen_height))

    pygame.mixer.music.load("data/sound/menu.mp3")
    pygame.mixer.music.play(-1)

    pixel_font = pygame.font.Font("data/pic/fonts/joystix monospace.otf", 40)

    owner_image = pygame.image.load("data/pic/background/owners.png")
    owner_image = pygame.transform.scale(owner_image, (screen_width, screen_height))

    controls_image = pygame.image.load("data/pic/background/controls.png")
    controls_image = pygame.transform.scale(controls_image, (screen_width, screen_height))

    loading_image = pygame.image.load("data/pic/background/loading.png")
    loading_image = pygame.transform.scale(loading_image, (screen_width, screen_height))

    running = True
    show_owner_screen = False
    show_controls_screen = False
    show_loading_screen = False
    loading_start_time = None

    num_dots = 5
    dot_radius = 10
    dot_spacing = 30
    dot_brightness = 255
    dot_fade_speed = 0.5

    while running:
        screen.fill(WHITE)

        if show_owner_screen:
            screen.blit(owner_image, (0, 0))
            close_button = pygame.Rect(screen_width - 50, 10, 40, 40)
            pygame.draw.rect(screen, BUTTON_COLOR, close_button)
            pygame.draw.line(screen, WHITE, (screen_width - 45, 15), (screen_width - 15, 45), 3)
            pygame.draw.line(screen, WHITE, (screen_width - 45, 45), (screen_width - 15, 15), 3)
        elif show_controls_screen:
            screen.blit(controls_image, (0, 0))
            close_button = pygame.Rect(screen_width - 50, 10, 40, 40)
            pygame.draw.rect(screen, BUTTON_COLOR, close_button)
            pygame.draw.line(screen, WHITE, (screen_width - 45, 15), (screen_width - 15, 45), 3)
            pygame.draw.line(screen, WHITE, (screen_width - 45, 45), (screen_width - 15, 15), 3)
        elif show_loading_screen:
            screen.blit(loading_image, (0, 0))
            if not loading_start_time:
                loading_start_time = time.time()
                pygame.mixer.music.stop()

            elapsed_time = time.time() - loading_start_time
            if elapsed_time >= 8:
                game.game(screen)
                running = False
            else:
                time_per_dot = 0.5
                dot_index = int((elapsed_time % (num_dots * time_per_dot)) // time_per_dot)
                current_dot_time = elapsed_time % time_per_dot
                if current_dot_time > time_per_dot / 2:
                    dot_brightness = 255 - int(255 * ((current_dot_time - time_per_dot / 2) / (time_per_dot / 2)))
                else:
                    dot_brightness = int(255 * (current_dot_time / (time_per_dot / 2)))

                for i in range(num_dots):
                    brightness = dot_brightness if i == dot_index else 255
                    dot_color = (brightness, brightness, brightness)
                    pygame.draw.circle(screen, dot_color, (screen_width // 2 - ((num_dots - 1) * dot_spacing) // 2 + i * dot_spacing, screen_height - 50), dot_radius)
        else:
            screen.blit(background_menu, (0, 0))

            button_width, button_height = 365, 45
            button_padding = 65
            start_button = pygame.Rect((screen_width - button_width) // 2, 370, button_width, button_height)
            controls_button = pygame.Rect((screen_width - button_width) // 2, 370 + button_padding, button_width, button_height)
            owners_button = pygame.Rect((screen_width - button_width) // 2, 370 + 2 * button_padding, button_width, button_height)
            exit_button = pygame.Rect((screen_width - button_width) // 2, 370 + 3 * button_padding, button_width, button_height)

            buttons = [
                (start_button, "Start Game"),
                (controls_button, "Controls"),
                (owners_button, "Owners"),
                (exit_button, "Exit")
            ]

            mouse_pos = pygame.mouse.get_pos()

            for button, text in buttons:
                if button.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button)

                    left_arrow = [(button.left - 20, button.centery), (button.left - 10, button.centery - 10), (button.left - 10, button.centery + 10)]
                    right_arrow = [(button.right + 20, button.centery), (button.right + 10, button.centery - 10), (button.right + 10, button.centery + 10)]
                    pygame.draw.polygon(screen, ARROW_COLOR, left_arrow)
                    pygame.draw.polygon(screen, ARROW_COLOR, right_arrow)
                else:
                    pygame.draw.rect(screen, BUTTON_COLOR, button)

                text_surface = pixel_font.render(text, True, WHITE)
                text_rect = text_surface.get_rect(center=button.center)
                screen.blit(text_surface, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if show_owner_screen or show_controls_screen:
                    if close_button.collidepoint(mouse_pos):
                        show_owner_screen = False
                        show_controls_screen = False
                else:
                    for button, text in buttons:
                        if button.collidepoint(mouse_pos):
                            if text == "Exit":
                                pygame.quit()
                                running = False
                            elif text == "Owners":
                                show_owner_screen = True
                            elif text == "Controls":
                                show_controls_screen = True
                            elif text == "Start Game":
                                show_loading_screen = True

#if __name__ == "__main__":
 #   main_menu()

