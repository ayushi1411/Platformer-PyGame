import pygame
from pygame.locals import *

class Player():
    def __init__(self, x, y):
        self.reset(x,y)

    def update(self, screen, world, blob_group, lava_group, game_over, exit_group):
        
        dx = 0
        dy = 0
        walk_cooldown = 5

        if game_over == 0:
            #get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.dir = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.dir = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.dir == 1:
                    self.image = self.images_right[self.index]
                if self.dir == -1:
                    self.image = self.images_left[self.index]
            
            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.dir == 1:
                    self.image = self.images_right[self.index]
                if self.dir == -1:
                    self.image = self.images_left[self.index]

            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            self.in_air = True
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground i.e jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #check if above the ground i.e falling
                    elif self.vel_y >= 0:
                        dy = self.rect.bottom - tile[1].top
                        self.in_air = False

            #check for collision with enemies
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1

            #check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1

            #check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy
            
        elif game_over == -1 : 
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5
        #draw player onto the screen
        screen.screen.blit(self.image, self.rect)
        pygame.draw.rect(screen.screen, (255,255,255), self.rect, 2 )

        return game_over

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False )
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load('img/ghost.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.dir = 0
        self.in_air = True