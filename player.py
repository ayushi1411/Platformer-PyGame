import pygame
from pygame.locals import *

class Player():
    def __init__(self, x, y):
        img = pygame.image.load('img/guy1.png')
        self.image = pygame.transform.scale(img, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, screen):
        
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
        
        #check for collision

        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy
        
        #draw player onto the screen
        screen.screen.blit(self.image, self.rect)