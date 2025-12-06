import pygame #type: ignore

class SpriteSheet():

    HEIGHT = 32
    WIDTH = 32
    SCALE = 3
    BACKGROUND = 'black'

    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    
    def get_num_frames(self) -> int:
        return self.sheet.get_width() // 32