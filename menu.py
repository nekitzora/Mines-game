import pygame

def main_menu():
    pygame.init()
    pygame.mixer.init()

    screen_width, screen_height = 1500, 790
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bomberman")

    icon = pygame.image.load("Mines-game/pic/background/mainmenu.png")
    pygame.display.set_icon(icon)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_COLOR = (50, 50, 50)
    BUTTON_HOVER_COLOR = (70, 70, 70)
    ARROW_COLOR = (255, 255, 255) 

    background_menu = pygame.image.load("Mines-game/pic/background/mainmenu.png")
    background_menu = pygame.transform.scale(background_menu, (screen_width, screen_height))

    pygame.mixer.music.load("Mines-game/pic/music/titlescreen_sound.mp3") 
    pygame.mixer.music.play(-1)  

    pixel_font = pygame.font.Font("Mines-game/pic/fonts/joystix monospace.otf", 40) 

    owner_image = pygame.image.load("Mines-game/pic/background/owners.png")  
    owner_image = pygame.transform.scale(owner_image, (screen_width, screen_height))

    running = True
    show_owner_screen = False
     
    while running:   
        screen.fill(WHITE)  

        if show_owner_screen:
            screen.blit(owner_image, (0, 0)) 
            close_button = pygame.Rect(screen_width - 50, 10, 40, 40)
            pygame.draw.rect(screen, BUTTON_COLOR, close_button)
            pygame.draw.line(screen, WHITE, (screen_width - 45, 15), (screen_width - 15, 45), 3)
            pygame.draw.line(screen, WHITE, (screen_width - 45, 45), (screen_width - 15, 15), 3)
        else:
            screen.blit(background_menu, (0, 0)) 

            button_width, button_height = 365, 45
            button_padding = 65
            start_button = pygame.Rect((screen_width - button_width) // 2, 370, button_width, button_height)
            controls_button = pygame.Rect((screen_width - button_width) // 2, 370 + button_padding, button_width, button_height)
            how_to_play_button = pygame.Rect((screen_width - button_width) // 2, 370 + 2 * button_padding, button_width, button_height)
            owners_button = pygame.Rect((screen_width - button_width) // 2, 370 + 3 * button_padding, button_width, button_height)
            exit_button = pygame.Rect((screen_width - button_width) // 2, 370 + 4 * button_padding, button_width, button_height)

            buttons = [
                (start_button, "Start Game"),
                (controls_button, "Controls"),
                (how_to_play_button, "How to play"),
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
                if show_owner_screen:
                    if close_button.collidepoint(mouse_pos):
                        show_owner_screen = False
                else:
                    for button, text in buttons:
                        if button.collidepoint(mouse_pos) and text == "Exit":
                            pygame.quit()
                            running = False
                        elif button.collidepoint(mouse_pos):
                            if text == "Owners":
                                show_owner_screen = True
                            elif text: 
                                print(f"Clicked {text}")

if __name__ == "__main__":
    main_menu() 