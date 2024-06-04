import pygame

class GameSound():
    def __init__(self, direction):
        self.sound = pygame.mixer.Sound(direction)
        self.played = False

    def change_played(self):
        self.played = not self.played