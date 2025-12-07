import pygame 
import sprite_sheet as ss
import settings
import player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SIZE)
        pygame.display.set_caption('Waffles')

    def run(self):
        plyr = player.Player(self.screen, 'amogus')
        
        running = True
        clock = pygame.time.Clock()

        while running:

            self.screen.fill('white')
            clock.tick(150)

            plyr.process_keys()
            plyr.display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
