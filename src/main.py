import pygame #type: ignore
import sprite_sheet as ss
import settings
import player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SIZE)
        pygame.display.set_caption('Waffles')

    def run(self):
        frog = player.Player(self.screen)
        
        running = True

        clock = pygame.time.Clock()

        while running:

            self.screen.fill('white')

            frog.process_keys()
            frog.display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()