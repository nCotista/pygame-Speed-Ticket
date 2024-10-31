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
    if len(obstacles) < 2:  # 2% chance per frame to generate obstacle สุ่ม 0 - 100 เอาเฉพาะที่น้อยกว่า 2 เลยเป็น 2%
        create_obstacle()

    # Ping: สร้าง obstacle ขึ้นมาเป็น class แล้วให้ขยับ
    for obs in obstacles:
        obs.obstacle_move()
        if obs.get_rect().colliderect(player): # Ping: check ว่า obstacle ชน player มั้ย
            player.acceleration(obs.speedChanger)
            print(f'{obs.speedChanger} , {player.speed}')
            obstacles.remove(obs)
        if obs.y > SCREEN_HEIGHT:
            obstacles.remove(obs)

    # Update the display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
