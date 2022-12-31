import pygame
from pygame.locals import *

class Screen():
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tile_size = tile_size
        self.clock = pygame.time.Clock()
        self.fps = 60