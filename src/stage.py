import pygame

class Stage:
    
    def __init__(self, screen):
        self.screen = screen
        self.platforms = []
        self.rect = pygame.Rect(100, 400, 300, 50)
        self.rect2 = pygame.Rect(600, 200, 300, 50)

        self.platforms.append(self.rect)
        self.platforms.append(self.rect2)

    def draw(self):
        pygame.draw.rect(self.screen, 'blue', self.rect)
        pygame.draw.rect(self.screen, 'blue', self.rect2)