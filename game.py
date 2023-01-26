#PA token : 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

import pygame
from pygame.locals import *
from player import *
from world import *
from screen import *
from enemy import *
from button import *

pygame.init()
screen_width = 1000
screen_height = 1000

screen = Screen(screen_width, screen_width, 50)
pygame.display.set_caption('Platformer')

#define game variables
game_over = 0
main_menu = True

#load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')
restart_img = pygame.image.load('img/restart_btn.png')
start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')

def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen.screen, (255, 255, 255), (0, line * screen.tile_size), (screen.width, line * screen.tile_size))
        pygame.draw.line(screen.screen, (255, 255, 255), (line * screen.tile_size, 0), (line * screen.tile_size, screen.height))


world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player = Player(100, screen.height - 130)

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()

world = World(world_data, screen, blob_group, lava_group)

restart_button = Button(screen.width // 2 - 50, screen.height // 2 + 100, restart_img)
start_button = Button(screen.width // 2 - 350, screen_height //2, start_img)
exit_button = Button(screen.width // 2 + 150, screen_height //2, exit_img)

run = True
while run:
    screen.clock.tick(screen.fps)
    screen.screen.blit(bg_img, (0,0))
    screen.screen.blit(sun_img, (100,100))

    if main_menu == True:
        if exit_button.draw(screen):
            run = False
        if start_button.draw(screen):
            main_menu = False
    else : 
        world.draw(screen)

        if game_over == 0:
            blob_group.update()

        blob_group.draw(screen.screen)
        lava_group.draw(screen.screen)

        game_over = player.update(screen, world, blob_group, lava_group, game_over)

        #if player has died
        if game_over == -1:
            if restart_button.draw(screen):
                player.reset(100, screen.height - 130)
                game_over = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
