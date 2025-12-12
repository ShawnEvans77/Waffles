import pygame 
import sprite_sheet as ss
import settings
import player as p

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SIZE)
        pygame.display.set_caption('Waffles')

    def run(self):
        plyr = p.Player(self.screen, 'frog')
        running = True
        clock = pygame.time.Clock()

        while running:
            self.screen.fill('white')
            clock.tick(300)

            key = pygame.key.get_pressed()
            pygame.draw.rect(self.screen, 'darkgreen', pygame.Rect(200, 350, 870, 100))

            # plyr.gravity()
            plyr.move(key)
            plyr.display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()