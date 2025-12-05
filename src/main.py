import pygame #type: ignore
import sprite_sheet as ss
import settings

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.SIZE)
        pygame.display.set_caption('Waffles')

    def run(self):
        sheet = ss.SpriteSheet(pygame.image.load('assets/idle.png').convert_alpha())

        animation_list = []
        animation_steps = 10
        last_update = pygame.time.get_ticks()
        animation_cooldown = 75
        frame = 0

        for i in range(animation_steps):
            animation_list.append(sheet.get_image(i, 32, 32, 3, 'black'))

        running = True

        while running:
            self.screen.fill('white')

            current_time = pygame.time.get_ticks()

            if current_time - last_update >= animation_cooldown:
                frame += 1
                last_update = current_time

                if frame >= len(animation_list):
                    frame = 0

            self.screen.blit(animation_list[frame], (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()