import pygame
from pygame.locals import *

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self, screen):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            #check left button click
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #draw button
        screen.screen.blit(self.image, self.rect)

        return action