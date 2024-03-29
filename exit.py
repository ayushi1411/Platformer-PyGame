import pygame
from pygame.locals import *
from screen import *

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(img, (screen.tile_size, screen.tile_size * 1.5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
