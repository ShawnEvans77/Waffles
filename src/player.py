import spritesheet as ss
import player_settings as ps
import window_settings as ws
import vector as v
import pygame

class Player:

    def __init__(self, screen, skin):
        self.screen = screen
        self.sheet = ss.SpriteSheet(skin).get()
        self.last_update = pygame.time.get_ticks()

        self.x, self.y = 0, 0
        self.vel = v.Vector(0,0)
        self.frame = 0

        self.falling = True
        self.jumping = False
        self.grounded = False
        self.walking = False
        self.face_right = True

        self.jump_velocity = ((2.0 * ps.JUMP_HEIGHT) / ps.JUMP_PEAKTIME) * -1
        self.jump_gravity = ((-2.0 * ps.JUMP_HEIGHT) / (ps.JUMP_PEAKTIME * ps.JUMP_PEAKTIME)) 
        self.fall_gravity = ((-2.0 * ps.JUMP_HEIGHT) / (ps.JUMP_DESCENTTIME * ps.JUMP_DESCENTTIME)) 
        
        self.state = self.check_state()

    def update(self, key):
        self.physics(key)
        self.display()

    def physics(self, key):
        self.vel.y = self.get_gravity()
        self.vel.x = self.get_input_velocity(key) * ps.SPEED

        if key[pygame.K_SPACE] and self.grounded and not self.jumping:
            self.jump()

    def jump(self):
        self.vel.y = self.jump_velocity

    def get_gravity(self):
        if self.y > ws.BOTTOM_BORDER:
            return 0

        if self.vel.y < 0:
            return self.vel.y + self.jump_gravity

        return self.vel.y + self.fall_gravity
                    
    def get_input_velocity(self, key):
        horizontal_vel = 0

        if key[pygame.K_LEFT] and self.x > ws.LEFT_BORDER:
            horizontal_vel -= 1
            self.face_right = False

        if key[pygame.K_RIGHT] and self.x < ws.RIGHT_BORDER:
            horizontal_vel += 1
            self.face_right = True

        self.walking = True if horizontal_vel != 0 else False

        return horizontal_vel
    
    def check_state(self):

        if self.vel.y == 0:
            return ps.IDLE if self.vel.x == 0 else ps.RUNNING
        
        if self.vel.y != 0:
            return ps.FALLING if not self.vel.y < 0 else ps.JUMPING
        
    def correct_direction(self, image):

        return image if self.face_right else pygame.transform.flip(image, True, False)

    def display(self):
        self.current_time = pygame.time.get_ticks()

        self.state = self.check_state()

        if self.current_time - self.last_update >= ps.ANIMATION_COOLDOWN:
            self.frame += 1
            self.last_update = self.current_time

        if self.frame >= len(self.sheet[self.state]):
            self.frame = 0

        image = self.correct_direction(self.sheet[self.state][self.frame])

        self.x += self.vel.x
        self.y += self.vel.y


        print(self.x, self.y)

        self.screen.blit(image, (self.x, self.y))