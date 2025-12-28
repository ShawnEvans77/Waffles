import spritesheet as ss
import player_settings as ps
import window_settings as ws
import vector as v
import pygame
import stage as s

class Player:

    def __init__(self, screen, skin, stage):
        self.screen = screen
        self.sheet = ss.SpriteSheet(skin).get()
        self.last_update = pygame.time.get_ticks()

        self.x, self.y = 0, 0
        self.vel = v.Vector(0,1)
        self.frame = 0

        self.stage = stage
        self.falling = True
        self.jumping = False
        self.grounded = False
        self.walking = False
        self.face_right = True

        # self.jump_velocity = ((2.0 * ps.JUMP_HEIGHT) / ps.JUMP_PEAKTIME) * -1.0
        # self.jump_gravity = ((-2.0 * ps.JUMP_HEIGHT) / (ps.JUMP_PEAKTIME * ps.JUMP_PEAKTIME))  * -1.0
        # self.fall_gravity = ((-2.0 * ps.JUMP_HEIGHT) / (ps.JUMP_DESCENTTIME * ps.JUMP_DESCENTTIME)) * -1.0

        self.state = self.check_state()

        self.rect = self.sheet[self.state][self.frame].get_rect()

    def update(self, key):
        self.physics(key)
        self.display()

    def physics(self, key):

        if not self.on_floor() and not self.jumping and not self.touching_obstacle():
            self.vel.y += ps.GRAVITY
            self.falling = True
        elif self.on_floor() or self.touching_obstacle():
            self.vel.y = 0
            self.falling = False
            self.grounded = True

        if key[pygame.K_SPACE] and (self.on_floor() or self.touching_obstacle()):
            self.jumping = True

        if self.jumping:
            self.jump()

        self.vel.x = self.get_input_velocity(key) * ps.SPEED

    def on_floor(self):
        return self.y > ws.BOTTOM_BORDER
    
    def touching_obstacle(self):

        for obstacle in self.stage.platforms:
            if self.rect.colliderect(obstacle):
                return True
                        
        return False
 
    def jump(self):
        if self.vel.y > ps.JUMP_HEIGHT:
            self.vel.y -= ps.JUMP_STRENGTH
        else:
            self.falling = True
            self.jumping = False

    def get_gravity(self):
        return self.jump_gravity if self.vel.y < 0 else self.fall_gravity

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
            return ps.FALLING if self.vel.y > 0 else ps.JUMPING
        
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

        self.rect = image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.x += self.vel.x
        self.y += self.vel.y

        self.screen.blit(image, (self.x, self.y))