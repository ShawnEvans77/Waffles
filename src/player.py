import pygame
import sprite_sheet as ss
import settings

class Player():

    IDLE = 'idle'
    RUN = 'run'
    JUMP = 'jump'
    FALL = 'fall'

    SPEED = 1
    JUMP_STRENGTH = 5

    JUMP_HEIGHT = -400
    GRAVITY = 1.5

    def __init__(self, screen, skin: str):
        self.frames = {}

        self.x, self.y = 0, 0

        self.add_frames(f'assets/{skin}/idle.png')
        self.add_frames(f'assets/{skin}/run.png')
        self.add_frames(f'assets/{skin}/jump.png')
        self.add_frames(f'assets/{skin}/fall.png')

        self.screen = screen

        self.state = Player.IDLE
        self.jump = False

        self.face_right = True
        self.grounded = False

        self.last_update = pygame.time.get_ticks()

        self.animation_cooldown = 50

        self.frame = 0

        self.rect = self.frames[self.state][self.frame].get_rect()

        self.horizontal_velocity = 0
        self.vertical_velocity = 0


        self.jump_length = 0

    def add_frames(self, file_path: str):

        state = file_path[file_path.rfind('/')+1:file_path.index('.')]

        sheet = ss.SpriteSheet(file_path)
        list = [frame for frame in sheet]

        self.frames[state] = list

    def gravity(self):

        if self.y < settings.BOTTOM_BORDER:
            self.y += Player.GRAVITY
            self.grounded = False
        else:
            self.grounded = True

    def move(self, key):

        self.horizontal_velocity = 0
        self.vertical_velocity = 0

        if key[pygame.K_LEFT] and self.x > settings.LEFT_BORDER:

            self.horizontal_velocity = -Player.SPEED
            self.x += self.horizontal_velocity
            self.face_right = False

        if key[pygame.K_RIGHT] and self.x < settings.RIGHT_BORDER:

            self.horizontal_velocity = Player.SPEED
            self.x += self.horizontal_velocity 
            self.face_right = True

        if key[pygame.K_SPACE]:

            self.jump = True
            self.is_grounded = False
            self.vertical_velocity = Player.JUMP_STRENGTH

        if self.jump:

            if self.jump_length >= Player.JUMP_HEIGHT:

                self.vertical_velocity = -Player.JUMP_STRENGTH
                self.y += self.vertical_velocity       
                self.jump_length += self.vertical_velocity

            else:

                self.jump = False
                self.jump_length = 0
                

       


        # if self.jump:

        #     if self.velocity >= Player.JUMP_HEIGHT:

        #         self.jump_power = -4
        #         self.y += self.jump_power
        #         self.velocity += self.jump_power

        #     else:
        #         self.grounded = True

        # if key[pygame.K_UP] and self.y > 0:
        #     dy = -Player.VEL
        #     self.y += dy

        # if key[pygame.K_DOWN] and self.y < settings.WINDOW_HEIGHT - 100:
        #     dy = Player.VEL
        #     self.y += dy

        # match dx:
        #     case 0: self.state = Player.IDLE
        #     case _: self.state = Player.RUN

    def check_state(self):
        if self.grounded: 
            return Player.IDLE if self.horizontal_velocity == 0 else Player.RUN
        
        elif not self.grounded and not self.jump:
            return Player.FALL
        elif not self.grounded and self.jump:
            return Player.JUMP
        

    def display(self):
        self.current_time = pygame.time.get_ticks()

        self.state = self.check_state()

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