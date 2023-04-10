import pygame
from pygame.locals import *
from enemy import *
from lava import *
from exit import *
from coin import *


class World():
    def __init__(self, data, screen, blob_group, lava_group, exit_group, coin_group):
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
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (screen.tile_size, screen.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * screen.tile_size
                    img_rect.y = row_count * screen.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * screen.tile_size, row_count * screen.tile_size + 15)
                    blob_group.add(blob)
                if tile == 6:
                    lava = Lava(col_count * screen.tile_size, row_count * screen.tile_size + (screen.tile_size // 2), screen)
                    lava_group.add(lava)
                if tile == 7:
                    coin = Coin(col_count * screen.tile_size + (screen.tile_size // 2), row_count * screen.tile_size + (screen.tile_size // 2), screen)
                    coin_group.add(coin)
                if tile == 8:
                    exit = Exit(col_count * screen.tile_size, row_count * screen.tile_size - (screen.tile_size // 2), screen)
                    exit_group.add(exit)
                col_count += 1
            row_count += 1

    def draw(self, screen):
        for tile in self.tile_list:
            screen.screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen.screen, (255,255,255), tile[1], 2)