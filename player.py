from game_attributes import Attributes
import pygame
class Player:
    def __init__(self):
        """
        Player class initialization
        """
        self.attrs = Attributes()
        self.size = self.attrs.player_size
        self.color = self.attrs.player_color
        self.speed = self.attrs.player_speed
        self.radius = 4
        # (screen mid point, screen 5% up from the bottom)
        self.position = (self.attrs.screen_width / 2, (self.attrs.screen_height - (self.attrs.screen_height / 20)))


    def draw(self, surface):
        """
        draw the player to the screen
        """
        pygame.draw.circle(surface, self.color, self.position, self.radius)

    
    def move(self, delta_x, delta_y):
        """
        move the player with delta_x (x speed in 1 frame) and delta_y (y speed in 1 frame)
        """
        new_x = self.position[0] + delta_x
        new_y = self.position[1] + delta_y

        # bound-check
        if new_x < 0 or new_x > self.attrs.screen_width - self.radius:
            new_x = self.position[0]
        
        if new_y < self.attrs.screen_height - self.attrs.player_max_up or new_y > self.attrs.screen_height - self.radius:
            newY = self.position[1]

        self.position = (new_x, new_y)
    
    def did_collide(self, rect):
        """
        check if the player (circle) got hit by the enemy (rectangle), if it got hit, return True
        using intersection rules between circle and rectangles
        INPUTS:
            rect: enemy rectangle
        """
        circle_distance_x = abs(self.position[0] - rect.centerx)
        circle_distance_y = abs(self.position[1] - rect.centery)
        # no collision
        if circle_distance_x > rect.w / 2.0 + self.radius or circle_distance_y > rect.h / 2.0 + self.radius:
            return False 
        # has collision
        if circle_distance_x <= rect.w / 2.0 + self.radius or circle_distance_y <= rect.h / 2.0: 
            return True

        corner_x = circle_distance_x-rect.w/2.0
        corner_y = circle_distance_y-rect.h/2.0
        corner_distance_sq = corner_x**2.0 +corner_y**2.0
        return corner_distance_sq <= self.radius**2.0

