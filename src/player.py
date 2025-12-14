import pygame
import sprite_sheet as ss
import game_settings
import player_settings

class Player():

    def __init__(self, screen):
        self.frames = {}

        self.x, self.y = 0, 0

        self.add_frames(f'assets/{player_settings.SKIN}/idle.png')
        self.add_frames(f'assets/{player_settings.SKIN}/run.png')
        self.add_frames(f'assets/{player_settings.SKIN}/jump.png')
        self.add_frames(f'assets/{player_settings.SKIN}/fall.png')

        self.screen = screen
        self.state = player_settings.IDLE

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

    def gravity(self, platforms):

        if self.y < game_settings.BOTTOM_BORDER and not self.collision(platforms):

            self.vertical_velocity = player_settings.GRAVITY
            self.y += self.vertical_velocity
            self.grounded = False

        else:
            self.grounded = True
            self.vertical_velocity = 0

    def collision(self, platforms) -> bool:

        for platform in platforms:
            if pygame.Rect.colliderect(self.rect, platform):
                return True
            
        return False

    def move(self, key):

        self.horizontal_velocity = 0

        if key[pygame.K_LEFT] and self.x > game_settings.LEFT_BORDER:

            self.horizontal_velocity = -player_settings.SPEED
            self.x += self.horizontal_velocity
            self.face_right = False

        if key[pygame.K_RIGHT] and self.x < game_settings.RIGHT_BORDER:

            self.horizontal_velocity = player_settings.SPEED
            self.x += self.horizontal_velocity 
            self.face_right = True

        if key[pygame.K_SPACE] and self.grounded == True:

            self.jump = True
            self.is_grounded = False
            self.vertical_velocity = player_settings.JUMP_STRENGTH

        if key[pygame.K_r]:
            self.x = 0
            self.y = 0

        if self.jump:

            if self.jump_length >= player_settings.JUMP_HEIGHT:
                self.vertical_velocity = -player_settings.JUMP_STRENGTH
                self.y += self.vertical_velocity       
                self.jump_length += self.vertical_velocity
            else:
                self.jump = False
                self.jump_length = 0
                
    def check_state(self):
        if self.grounded: 
            return player_settings.IDLE if self.horizontal_velocity == 0 else player_settings.RUN
        
        if not self.grounded: 
            return player_settings.FALL if not self.jump else player_settings.JUMP
 
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

        print(self.x, self.y)

        self.rect.x = self.x
        self.rect.y = self.y