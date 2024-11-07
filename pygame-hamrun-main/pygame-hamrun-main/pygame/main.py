import pygame
import random
import sys

from sqlalchemy import false

from setting import *
from object import *
from players import *
# Initialize Pygame
pygame.init()

player = Player()
# Main game loop
running = True
obsCount = 0
low_limit, high_limit = barrier_lowLimit, barrier_highLimit

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the road with perspective
    draw_perspective_road()

    player.Player_controller()

    # Add obstacles
    if len(obstacles) < 2:
        if obsCount > 5:
            create_barrier(low_limit, high_limit)
            high_limit += barrier_addConstant
            low_limit += barrier_addConstant
            obsCount = 0
        else:
            create_obstacle()
            obsCount += 1

    for obs in obstacles:
        obs.obstacle_move()
        if obs.get_rect().colliderect(player):
            if type(obs) == Obstacle:
                player.acceleration(obs.speedChanger)
                #print(f'{obs.speedChanger} , {player.speed}')
            elif type(obs) == MuDi_Obstacle:
                player.speed = obs.get_total(player.speed)
            elif type(obs) == Barrier:
                if player.speed < obs.speedLimit:
                    print('Game Over')
                    running = False
                else:
                    player.acceleration(-1*obs.speedLimit)

            obstacles.remove(obs)
            continue
        if obs.y > SCREEN_HEIGHT:
            obstacles.remove(obs)

    # Update the display
    pygame.display.update()

    # Frame rate
    fr = 60 + player.speed/player_speed_ratio
    pygame.time.Clock().tick(fr)

# Quit Pygame
pygame.quit()
sys.exit()
