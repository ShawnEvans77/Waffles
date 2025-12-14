import pygame 
import sprite_sheet as ss
import game_settings
import player as p

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(game_settings.SIZE)
        pygame.display.set_caption('Waffles')

    def run(self):
        plyr = p.Player(self.screen)
        running = True
        clock = pygame.time.Clock()

        platforms = []

        while running:
            self.screen.fill('white')
            clock.tick(300)

            key = pygame.key.get_pressed()

            platforms.append(pygame.draw.rect(self.screen, 'darkgreen', pygame.Rect(100, 350, 520, 35)))
            platforms.append(pygame.draw.rect(self.screen, 'blue', pygame.Rect(900, 350, 350, 35)))

            plyr.gravity(platforms)

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
