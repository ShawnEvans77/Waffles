import pygame #type: ignore
import sprite_sheet as ss
import settings

class Player():

    HEIGHT = 32
    WIDTH = 32
    SCALE = 3
    BACKGROUND = 'black'

    def __init__(self, screen):
        self.sheet = ss.SpriteSheet(pygame.image.load('assets/idle.png').convert_alpha())
        self.image = self.sheet.get_image(0, Player.HEIGHT, Player.WIDTH, Player.SCALE, Player.BACKGROUND)
        # self.rect = self.image.get_rect()
        self.screen = screen
        self.idle = True
        self.dx = 0
        self.dy = 0

    def prepare_ani(self):
        self.frame_list = []
        self.frames = [10, 10]
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 75
        self.frame = 0

    def process_keys(self):
        key = pygame.key.get_pressed()

        mv = 1

        if key[pygame.K_LEFT] and self.dx > 0:
            self.dx -= mv
        if key[pygame.K_RIGHT] and self.dx < settings.WINDOW_WIDTH - 100:
            self.dx += mv
        if key[pygame.K_UP] and self.dy > 0:
            self.dy -= mv
        if key[pygame.K_DOWN] and self.dy < settings.WINDOW_HEIGHT - 100:
            self.dy += mv
   
    def display(self, state):

        self.screen.blit(self.image, (self.dx, self.dy))

        # for i in range(self.frames):
        #     self.frame_list.append(self.sheet.get_image(i, 32, 32, 3, 'black'))

        # self.current_time = pygame.time.get_ticks()

        # if self.current_time - self.last_update >= self.animation_cooldown:
        #     self.frame += 1
        #     self.last_update = self.current_time

        #     if self.frame >= len(self.frame_list):
        #         frame = 0