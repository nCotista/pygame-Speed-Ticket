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

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the road with perspective
    draw_perspective_road()

    player.Player_controller() # Ping: รวมคำสั่ง ขยับ player กับ วาด player เอาไว้ใน class Player ที่ object.py

    # Add obstacles
    if len(obstacles) < 2:
        if obsCount > 5:
            create_barrier()
            barrier_highLimit += barrier_addConstant
            barrier_lowLimit += barrier_addConstant
            obsCount = 0
        else:
            create_obstacle()
            obsCount += 1

    # Ping: สร้าง obstacle ขึ้นมาเป็น class แล้วให้ขยับ
    for obs in obstacles:
        obs.obstacle_move()
        # TODO: Clean Up -> update detection
        if obs.get_rect().colliderect(player): # Ping: check ว่า obstacle ชน player มั้ย
            if type(obs) == Obstacle:
                player.acceleration(obs.speedChanger)
                print(f'{obs.speedChanger} , {player.speed}')
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
    # TODO: Speed Up the car

    # Update the display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
