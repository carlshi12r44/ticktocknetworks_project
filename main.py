# pylint: disable=redefined-outer-name
import pygame
import random,sys
from world import World 
from game_attributes import Attributes

def run(attrs):
    """
    main driver program to run the game
    """
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((attrs.screen_width, attrs.screen_height))

    pygame.display.set_caption("Dodger game")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    is_running = True

    # world object
    world = World()
    font = pygame.font.SysFont("monospace", 25)

    # main loop
    while is_running:
        for event in pygame.event.get():
            if event == pygame.QUIT: # if the user click red button, the game needs to quit
                is_running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # if the user hits escape button, that means game needs to quit
                is_running = False
            elif event.type == pygame.KEYDOWN and event.key == ord("r"): # press r key to reset the game
                world.reset()
            else: # handle other events (moving the player, etc...)
                world.handle_keys(event)



        clock.tick(attrs.fps)

        if not world.is_gameover():
            world.update()

        surface.fill(attrs.background_color)
        world.draw(surface)
        
        screen.blit(surface, (0, 0)) # draw everything to the screen
        text = font.render("Score: {0}".format(world.score), 1, attrs.text_color)
        screen.blit(text, (5, 10))
        esc_text = font.render("press esc to quit", 1, attrs.text_color)
        screen.blit(esc_text, (5, 30))

        if world.is_gameover():
            over = font.render("Game Over", 1, attrs.text_color)
            screen.blit(over, (attrs.screen_width / 3, attrs.screen_width / 2))
            reset_text = font.render("Hit r to reset", 1, attrs.text_color)
            screen.blit(reset_text, (attrs.screen_width / 3, attrs.screen_height / 2 + 45))

        pygame.display.update()



if __name__ == "__main__":
    # want no global variables here since it's not really good for future development
    # import attributes from game_attributes.py
    attrs = Attributes()
    run(attrs)
    pygame.quit()