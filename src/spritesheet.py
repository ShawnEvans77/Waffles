import pygame
import os
import player_settings as ps

class SpriteSheet:
    
    def __init__(self, folder: str):
        '''Instantiates a sprite sheet based on the contents of a given folder.'''

        self.frames = {}
        self.folder = f"assets/{folder}"
        self.images = self.__parse()

    def get(self):
        return self.frames

    def __parse(self):
        assets = os.listdir(self.folder)

        for asset in assets:
            self.__add_frames(f"{self.folder}/{asset}")

    def __add_frames(self, asset_path):

        asset_frames = pygame.image.load(asset_path).convert_alpha()
        asset_num_frames = asset_frames.get_width() // ps.HEIGHT

        asset_name = self.__get_file_name(asset_path)

        self.frames[asset_name] = []
            
        for i in range(asset_num_frames):
            image = pygame.Surface((ps.WIDTH, ps.HEIGHT)).convert_alpha()
            image.blit(asset_frames, (0, 0), ((i*ps.WIDTH), 0, ps.WIDTH, ps.HEIGHT))
            image = pygame.transform.scale(image, (ps.WIDTH * ps.SCALE, ps.HEIGHT * ps.SCALE))
            image.set_colorkey(ps.COLOR)
            self.frames[asset_name].append(image)

    def __get_file_name(self, asset_path) -> str:
        return asset_path[asset_path.rfind('/')+1:asset_path.index('.')]