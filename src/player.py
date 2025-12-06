import pygame #type: ignore
import sprite_sheet as ss
import settings

class Player():

    IDLE = 'idle'
    RUN = 'run'
    VEL = 2

    def __init__(self, screen):
        self.frames = {}
        self.add_frames('assets/idle.png')
        self.add_frames('assets/run.png')
        self.screen = screen
        self.state = Player.IDLE
        self.face_right = True

        # self.rect = self.image.get_rect()

        self.x = 0
        self.y = 0

        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 75
        self.frame = 0

    def add_frames(self, file_path: str):
        list = []

        state = file_path[file_path.index('/')+1:file_path.index('.')]

        sheet = ss.SpriteSheet(pygame.image.load(file_path).convert_alpha())
        num_frames = sheet.get_num_frames()

        for i in range(num_frames):
            list.append(sheet.get_image(i, ss.SpriteSheet.WIDTH, ss.SpriteSheet.HEIGHT, ss.SpriteSheet.SCALE, ss.SpriteSheet.BACKGROUND))

        self.frames[state] = list

    def process_keys(self):
        key = pygame.key.get_pressed()
        dx, dy = 0, 0

        if key[pygame.K_LEFT] and self.x > 0:
            dx = -Player.VEL
            self.x += dx
        if key[pygame.K_RIGHT] and self.x < settings.WINDOW_WIDTH - 100:
            dx = Player.VEL
            self.x += dx
        if key[pygame.K_UP] and self.y > 0:
            dy = -Player.VEL
            self.y += dy
        if key[pygame.K_DOWN] and self.y < settings.WINDOW_HEIGHT - 100:
            dy = Player.VEL
            self.y += dy

        match dx:
            case 0:
                self.state = Player.IDLE
            case _:
                self.state = Player.RUN

    def display(self):
        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.current_time
                
            if self.frame >= len(self.frames[self.state]):
                self.frame = 0

        self.screen.blit(self.frames[self.state][self.frame], (self.x, self.y))