import pygame
from pygame.locals import *


class World():
    def __init__(self, data, screen):
        self.tile_list = []
        #load images 
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (screen.tile_size, screen.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * screen.tile_size
                    img_rect.y = row_count * screen.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 2:
                    img = pygame.transform.scale(grass_img, (screen.tile_size, screen.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * screen.tile_size
                    img_rect.y = row_count * screen.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self, screen):
        for tile in self.tile_list:
            screen.screen.blit(tile[0], tile[1])