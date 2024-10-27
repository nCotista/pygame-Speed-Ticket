import pygame
import random
import sys
from setting import *
from object import *
from pygame.locals import *


# Main game loop
def game():
    global player_lane
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        # Draw the road with perspective
        draw_perspective_road()

        # Player controls (move between lanes)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_lane > 0:
            player_lane -= 1
        if keys[pygame.K_RIGHT] and player_lane < 1:  
            player_lane += 1

        # Draw player ต้องเขียนในนี้ เพราะต้อวรับค่า player lanes ที่เปลี่ยนตลอด มั้ง ลองเขียนแยกตอนแรกขยับไม่ได้
        SCREEN_HEIGHT =  pygame.display.Info().current_h 
        player_y  = SCREEN_HEIGHT - 120 #ต้องลบเพราะนับมุมเป็น  0,0 จากบนซ้าย
        player_x = get_lane_x_position(player_lane, player_y) - player_width // 2
        player_scale = 1 + (player_y / SCREEN_HEIGHT)  # Scale the player based on Y position
        scaled_player_width = int(player_width * player_scale)
        scaled_player_height = int(player_height * player_scale)

        pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, scaled_player_width, scaled_player_height))

        # Add obstacles
        if random.randint(0, 100) < 2:  # 2% chance per frame to generate obstacle สุ่ม 0 - 100 เอาเฉพาะที่น้อยกว่า 2 เลยเป็น 2%
            add_obstacle() #in object.py

        # Update obstacles and draw them
        for obstacle in obstacles[:]:
            obstacle["y"] += obstacle_speed #position

            # Scale the obstacle based on its y-position (depth effect)
            scale = 1 + (obstacle["y"] / SCREEN_HEIGHT)
            scaled_width = int(obstacle_width * scale) #obstacle_width in setting.py
            scaled_height = int(obstacle_height * scale)
            obstacle_x = get_lane_x_position(obstacle["lane"], obstacle["y"]) - scaled_width // 2

            # Draw obstacle
            pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle["y"], scaled_width, scaled_height))

            # Remove obstacles that go off the screen
            if obstacle["y"] > SCREEN_HEIGHT:
                obstacles.remove(obstacle)

        pygame.display.update()
        mainClock.tick(60)