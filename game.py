import pygame
import sys
import random

from pygame.time import delay

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPEED = 30
framerate = SPEED * 1/4

RED = [255, 0, 0]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

player_size = 50
player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT-player_size*3/2]

enemy_size = 50
enemy_pos = [random.randint(0,SCREEN_WIDTH - enemy_size), 0]
enemy_list = []
enemy_number = 8

game_over = False

font = pygame.font.SysFont('arial', 20)



score = 0

score_text = "Score: " + str(score)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list :
        pygame.draw.rect(screen, WHITE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
            
def enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < enemy_number and delay <0.2:
        enemy_pos[0] = random.randint(0,SCREEN_WIDTH - enemy_size)
        enemy_list.append([enemy_pos[0], 0])

def enemy_fall(enemy_list,score):
    for enemy_pos in enemy_list:
        if enemy_pos[1] < SCREEN_HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_pos[0] = random.randint(0,SCREEN_WIDTH - enemy_size)
            enemy_pos[1] = 0
        score += 1
    
def collision(player_pos, enemy_list):
    for enemy_pos in enemy_list:
        if (enemy_pos[1] >= player_pos[1]) and (enemy_pos[1] <= player_pos[1] + player_size*3/2):
            if (enemy_pos[0] + player_size > player_pos[0]) and (enemy_pos[0] < player_pos[0] + player_size):
                return True

while not game_over:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if x < SCREEN_WIDTH - player_size:
                if event.key == pygame.K_RIGHT:
                    x += player_size
            if x > 0 : 
                if event.key == pygame.K_LEFT:
                    x -= player_size

            player_pos = [x, y]        

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    

    enemy_fall(enemy_list, score)

    enemies(enemy_list)

    draw_enemies(enemy_list)

    if collision(player_pos, enemy_list):
        game_over = True
        break

    time_passed = str(pygame.time.get_ticks())

    text = font.render(time_passed, 1, (255, 255, 255))


    clock.tick(framerate)

    screen.blit(text, [100, 100])

    pygame.display.update()

