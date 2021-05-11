from game_attributes import Attributes
import random
import pygame
class Enemy:
    def __init__(self):
        """
        init for Enemy class
        """
        self.attrs = Attributes()
        self.size = self.attrs.enemy_size
        self.speed = self.attrs.enemy_speed
        self.color = self.attrs.enemy_color
        # draw to the right size of the pixel to avoid flushing on the top
        self.position = (random.randint(0, self.attrs.screen_width - self.size), 0 - self.size) 

    def move(self): 
        """simply let the enemy fall"""
        self.position = (self.position[0], self.position[1] + self.speed)

    def get_rect(self):
        """
        form the enemy as rectangle pygame object
        """
        return pygame.Rect(self.position, (self.size + self.size, self.size))

    def draw(self, surface):
        rectangle = self.get_rect()
        pygame.draw.rect(surface, self.color, rectangle)

    def is_off_screen(self):
        """check if the enemy is out of dimension"""
        # screen top is 0, bottom is height in pygame
        return self.position[1] > self.attrs.screen_height
