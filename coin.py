import pygame
from pygame.locals import *
from screen import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/coin.png')
        self.image = pygame.transform.scale(img, (screen.tile_size // 2, screen.tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)