import pygame #type: ignore
import sprite_sheet as ss

class Player():

    def __init__(self, screen):
        self.sheet = ss.SpriteSheet(pygame.image.load('assets/idle.png').convert_alpha())
        self.image = self.sheet.get_image(0, 32, 32, 3, 'black')
        self.rect = self.image.get_rect()
        self.screen = screen

    def prepare_ani(self):
        self.animation_list = []
        self.animation_steps = 10
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 75
        self.frame = 0

    def draw(self):
        # self.screen.blit(self.image, (0, 0))

        for i in range(self.animation_steps):
            self.animation_list.append(self.sheet.get_image(i, 32, 32, 3, 'black'))

        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.current_time

            if self.frame >= len(self.animation_list):
                frame = 0

        self.screen.blit(self.animation_list[self.frame], (0, 0))


    