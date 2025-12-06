import pygame #type: ignore
import sprite_sheet as ss
import settings

class Player():

    def __init__(self, screen):

        self.frames = []
        self.screen = screen

        self.frames.append(Player.fetch_frames('assets/idle.png', 10))
        self.frames.append(Player.fetch_frames('assets/run.png', 10))
        self.idle = True
        # self.rect = self.image.get_rect()

        self.x = 0
        self.y = 0

        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 75
        self.frame = 0

    @staticmethod
    def fetch_frames(file_path: str, total_frames):
        list = []

        # state = file_path[file_path.index('/')+1:file_path.index('.')]

        sheet = ss.SpriteSheet(pygame.image.load(file_path).convert_alpha())

        for i in range(total_frames):
            list.append(sheet.get_image(i, 32, 32, 3, 'black'))

        return list

    def process_keys(self):
        key = pygame.key.get_pressed()

        dx = 0
        dy = 0

        self.idle = True

        mv = 5

        if key[pygame.K_LEFT] and self.x > 0:
            dx = -mv
            self.x += dx
            self.idle = False
        if key[pygame.K_RIGHT] and self.x < settings.WINDOW_WIDTH - 100:
            dx = mv
            self.x += dx
            self.idle = False
        if key[pygame.K_UP] and self.y > 0:
            dy = -mv
            self.y += dy
        if key[pygame.K_DOWN] and self.y < settings.WINDOW_HEIGHT - 100:
            dy = mv
            self.y += dy

    def display(self):

        if self.idle == False:
            sprite_set = 1
        else:
            sprite_set = 0

        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1

            self.last_update = self.current_time

            if self.frame >= len(self.frames[0]):
                self.frame = 0

        self.screen.blit(self.frames[sprite_set][self.frame], (self.x, self.y))