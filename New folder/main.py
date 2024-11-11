import pygame
import random
import sys

from setting import *
from object import *
from players import *

# Initialize Pygame
pygame.init()

player = Player()

# Main game loop
running = True
obsCount = 0




roadx = pygame.image.load('road.png').convert()
road =  pygame.transform.scale(roadx,(SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()

car_x=0
while running:
    screen.fill(WHITE)
    
    # Calculate delta time for smooth movement
    delta = clock.tick() / 1000 + 0.00001
    road_speed =1000
    road_speed += player.speed*2 # ใช้ความเร็วของผู้เล่นเป็นตัวกำหนดความเร็วของถนน
    
    car_x += delta * road_speed  # เคลื่อนที่ถนนตามความเร็วของผู้เล่น
    

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background color
    screen.fill((100, 150, 250))
    
    for i in range(800):
        scale = (800- i) /800
        x = car_x + i/scale
        road_slice = road.subsurface((0, x % 320,800, 1))  # Change to 800 width
        scaled_slice = pygame.transform.scale(road_slice, (800 * scale, 1))  # Scale to fit width of screen
        
    
        screen.blit(scaled_slice, (400 - 400 * scale, 600 - i))  # Center the road on the screen

   

    # Draw the player's car (player controls)
    player.Player_controller()

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

    # Handle obstacle movement and collision
    for obs in obstacles:
        obs.obstacle_move()
        if obs.get_rect().colliderect(player.get_rect()):
            if type(obs) == Obstacle:
                player.acceleration(obs.speedChanger)
                print(f'{obs.speedChanger} , {player.speed}')
            elif type(obs) == Barrier:
                if player.speed < obs.speedLimit:
                    print('Game Over')
                    running = False
                else:
                    player.acceleration(-1 * obs.speedLimit)

            obstacles.remove(obs)
            continue
        if obs.y > SCREEN_HEIGHT:
            obstacles.remove(obs)

    # Update the display
    pygame.display.update()

    # Set frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
