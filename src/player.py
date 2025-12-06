import pygame #type: ignore
import sprite_sheet as ss
import settings

class Player():

    IDLE = 'idle'
    RUN = 'run'
    VEL = 2

    def __init__(self, screen, skin: str):
        self.frames = {}

        self.add_frames(f'assets/{skin}/idle.png')
        self.add_frames(f'assets/{skin}/run.png')

        self.screen = screen
        self.state = Player.IDLE
        self.face_right = True

        self.x = 0
        self.y = 0

        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 75
        self.frame = 0

    def add_frames(self, file_path: str):
        state = file_path[file_path.rfind('/')+1:file_path.index('.')]

        sheet = ss.SpriteSheet(file_path)

        list = []

        for frame in sheet:
            list.append(frame)

        self.frames[state] = list

    def process_keys(self):
        key = pygame.key.get_pressed()
        dx, dy = 0, 0

        if key[pygame.K_LEFT] and self.x > 0:
            dx = -Player.VEL
            self.x += dx
            self.face_right = False
        if key[pygame.K_RIGHT] and self.x < settings.WINDOW_WIDTH - 100:
            dx = Player.VEL
            self.x += dx
            self.face_right = True
        if key[pygame.K_UP] and self.y > 0:
            dy = -Player.VEL
            self.y += dy
        if key[pygame.K_DOWN] and self.y < settings.WINDOW_HEIGHT - 100:
            dy = Player.VEL
            self.y += dy
        
        match dx:
            case 0: self.state = Player.IDLE
            case _: self.state = Player.RUN

    def display(self):
        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.current_time
                
            if self.frame >= len(self.frames[self.state]):
                self.frame = 0

        # print(self.frame)

        image = self.frames[self.state][self.frame]

        # match self.face_right:
        #     case False: out_frame = pygame.transform.flip(image, True, False)
        #     case True: out_frame = image
                
        self.screen.blit(image, (self.x, self.y))