#PA token : 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

import pygame
from pygame.locals import *
from player import *
from world import *
from screen import *
from enemy import *
from button import *
import pickle
from os import path

pygame.init()
screen_width = 1000
screen_height = 1000

screen = Screen(screen_width, screen_width, 50)
pygame.display.set_caption('Platformer')


#define font
font_score = pygame.font.SysFont('Bauhaus 93', 30)

#define game variables
game_over = 0
main_menu = True
level = 0
max_levels = 7
score = 0


#define colours
white = (255, 255, 255)


#load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')
restart_img = pygame.image.load('img/restart_btn.png')
start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.screen.blit(img, (x,y))

#function to reset level
def reset_level(level):
    player.reset(100, screen.height - 130)
    blob_group.empty()
    lava_group.empty()
    exit_group.empty()
    #load in level data and create world
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data, screen, blob_group, lava_group, exit_group, coin_group)

    return world


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen.screen, (255, 255, 255), (0, line * screen.tile_size), (screen.width, line * screen.tile_size))
        pygame.draw.line(screen.screen, (255, 255, 255), (line * screen.tile_size, 0), (line * screen.tile_size, screen.height))


player = Player(100, screen.height - 130)

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

#create dummy coin for showing the score
score_coin = Coin(screen.tile_size // 2, screen.tile_size // 2, screen)
coin_group.add(score_coin)
#load in level data and create world
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
world = World(world_data, screen, blob_group, lava_group, exit_group, coin_group)

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
            #update score
            #check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
            draw_text('X ' + str(score), font_score, white, screen.tile_size - 10, 10)

        blob_group.draw(screen.screen)
        lava_group.draw(screen.screen)
        coin_group.draw(screen.screen)
        exit_group.draw(screen.screen)

        game_over = player.update(screen, world, blob_group, lava_group, game_over, exit_group)

        #if player has died
        if game_over == -1:
            if restart_button.draw(screen):
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0
        
        #if player has completed the level
        if game_over == 1:
            #reset game and go to next level
            level += 1
            if level <= max_levels:
                #reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                #restart game
                if restart_button.draw(screen):
                    level = 1
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0
                    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
