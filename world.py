from player import Player
from enemy import Enemy
from game_attributes import Attributes
import pygame
class World:
    """
    game world class
    """
    def __init__(self):
        """
        initialize the class
        """
        self.reset()
        self.attrs = Attributes()
        
    def reset(self):
        """
        when game is over, the world will be reset for a new game

        """
        self.player = Player()
        self.enemies = []
        self.game_over = False
        self.score = 0
        self.enemy_counter = 0 # numbers of enemies recorded last time

        self.is_move_up = False
        self.is_move_down = False
        self.is_move_left = False
        self.is_move_right = False


    def is_gameover(self):
        """
        determine if the game is over
        """
        return self.game_over

    def update(self):
        """
        update the game
        """
        # every frame updates the player get a score  
        self.score += 1
        # control player movement
        if self.is_move_up:
            self.player.move(0, -self.attrs.player_speed)
        if self.is_move_down:
            self.player.move(0, self.attrs.player_speed)
        if self.is_move_left:
            self.player.move(-self.attrs.player_speed, 0)
        if self.is_move_right:
            self.player.move(self.attrs.player_speed, 0)


        for enemy in self.enemies:
            enemy.move()
            # check if player hit by enemy
            # if yes game over
            if self.player.did_collide(enemy.get_rect()):
                self.game_over = True

            if enemy.is_off_screen(): # remove enemy out of screen
                self.enemies.remove(enemy)

        self.enemy_counter += 1

        if self.enemy_counter > self.attrs.enemy_spawn_rate:
            self.enemy_counter = 0
            # append new Enemy
            self.enemies.append(Enemy())

    def draw(self, surface):
        """
        draw onto the surface
        """
        self.player.draw(surface)
        for enemy in self.enemies:
            enemy.draw(surface)

    def handle_keys(self, event):
        """
        handle event key --> control player movement
        
        INPUTS:
            event: event of the key strokes
        """
        # start moving if key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.is_move_up = True
            if event.key == pygame.K_DOWN:
                self.is_move_down = True
            if event.key == pygame.K_LEFT:
                self.is_move_left = True
            if event.key == pygame.K_RIGHT:
                self.is_move_right = True
        # stop moving if key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.is_move_up = False
            if event.key == pygame.K_DOWN:
                self.is_move_down = False
            if event.key == pygame.K_LEFT:
                self.is_move_left = False
            if event.key == pygame.K_RIGHT:
                self.is_move_right = False

