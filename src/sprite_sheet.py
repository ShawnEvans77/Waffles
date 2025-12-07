import pygame 
import sprite_sheet as ss

class SpriteSheet():

    HEIGHT = 32
    WIDTH = 32
    SCALE = 3
    BACKGROUND = 'black'

    def __init__(self, image_path: str):
        self.sheet = pygame.image.load(image_path).convert_alpha()
        self.frames = []
        self.fill_frames()
        self.i = 0

    def fill_frames(self):
        num_frames = self.get_num_frames()

        for i in range(num_frames):
            self.frames.append(self.get_image(i, ss.SpriteSheet.WIDTH, ss.SpriteSheet.HEIGHT, ss.SpriteSheet.SCALE, ss.SpriteSheet.BACKGROUND))

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
    def get_num_frames(self) -> int:
        return self.sheet.get_width() // 32
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= len(self.frames):
            raise StopIteration
        
        current_img = self.frames[self.i]
        self.i += 1
        return current_img
    
    def __len__(self):
        return len(self.frames)