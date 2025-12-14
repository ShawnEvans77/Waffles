import pygame
import sprite_sheet as ss
import settings

class Player():

    IDLE = 'idle'
    RUN = 'run'
    JUMP = 'jump'
    FALL = 'fall'

    VEL = 1

    JUMP_HEIGHT = -20

    GRAVITY = 1

    def __init__(self, screen, skin: str):
        self.frames = {}

        self.add_frames(f'assets/{skin}/idle.png')
        self.add_frames(f'assets/{skin}/run.png')
        self.add_frames(f'assets/{skin}/jump.png')
        self.add_frames(f'assets/{skin}/fall.png')

        self.screen = screen
        self.state = Player.IDLE
        self.face_right = True

        self.x, self.y = 0, 0

        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 50

        self.frame = 0

        self.rect = self.frames[self.state][self.frame].get_rect()

        self.jump = False

        self.velocity = 0

    def add_frames(self, file_path: str):
        state = file_path[file_path.rfind('/')+1:file_path.index('.')]

        sheet = ss.SpriteSheet(file_path)
        list = [frame for frame in sheet]

        self.frames[state] = list

    def gravity(self):

        if self.y < settings.BOTTOM_BORDER:
            self.y += Player.GRAVITY

    def move(self, key):
        dx, dy = 0, 0

        self.state = Player.IDLE
    
        if key[pygame.K_LEFT] and self.x > settings.LEFT_BORDER:

            dx = -Player.VEL
            self.x += dx
            self.face_right = False
            self.state = Player.RUN

        if key[pygame.K_RIGHT] and self.x < settings.RIGHT_BORDER:
            dx = Player.VEL
            self.x += dx
            self.face_right = True
            self.state = Player.RUN

        if key[pygame.K_SPACE]:
            self.jump = True
            self.state = Player.JUMP

        if self.jump:

            if self.velocity >= Player.JUMP_HEIGHT:

                self.jump_power = -2
                self.y += self.jump_power
                self.velocity += self.jump_power

                self.state = Player.JUMP

            else:

                self.jump = False
                self.state = Player.FALL
                self.velocity = 0


        # if key[pygame.K_UP] and self.y > 0:
        #     dy = -Player.VEL
        #     self.y += dy

        # if key[pygame.K_DOWN] and self.y < settings.WINDOW_HEIGHT - 100:
        #     dy = Player.VEL
        #     self.y += dy

        # match dx:
        #     case 0: self.state = Player.IDLE
        #     case _: self.state = Player.RUN

    def display(self):
        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.current_time

        if self.frame >= len(self.frames[self.state]):
            self.frame = 0

        image = self.frames[self.state][self.frame]

        match self.face_right:
            case False: out_frame = pygame.transform.flip(image, True, False)
            case True: out_frame = image
                
        self.screen.blit(out_frame, (self.x, self.y))

        self.rect.x = self.x
        self.rect.y = self.y