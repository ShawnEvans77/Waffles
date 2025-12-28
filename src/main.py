import pygame
import window_settings
import spritesheet as ss
import player as p
import stage as s

class Game:
    '''
    A class responsible for executing the game. 
    '''

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(window_settings.SIZE)
        pygame.display.set_caption('waffles')
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        stage = s.Stage(self.screen)
        player = p.Player(self.screen, 'frog', stage)

        while running:

            key = pygame.key.get_pressed()
            self.screen.fill('white')

            stage.draw()

            player.update(key)
            self.clock.tick(300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()