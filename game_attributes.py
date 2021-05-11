import pygame
class Attributes:
    def __init__(self):
        
        self.screen_width = 600
        self.screen_height = 800
        self.fps = 40

        self.enemy_spawn_rate = 3
        self.enemy_size = 10 # in pixel
        self.enemy_speed= 8 # in pixel

        self.player_speed = 5
        self.player_size = 10
        self.player_max_up = 150

        # color setup
        self.background_color = pygame.Color("black")
        self.text_color = pygame.Color("white")
        self.enemy_color = pygame.Color("darkred")
        self.player_color = pygame.Color("darkgreen")