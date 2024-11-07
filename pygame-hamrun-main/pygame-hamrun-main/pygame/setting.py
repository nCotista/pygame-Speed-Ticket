from typing import List, Any

import pygame
# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



#Colors
WHITE = (255, 255, 255)
ROAD_COLOR = (50, 50, 50)

# Player settings
player_y = SCREEN_HEIGHT - 120  # Fixed Y position for the player (close to bottom)
player_width, player_height = 50, 100
player_lane = 0  # 0 = left 1 right
lanes = [0, 1]  # Lane IDs (left, right)
player_speed_ratio = 50 # ratio between player.speed value and player actual speed in game

# Obstacles
obstacles: list[Any] = []

# Obstacle settings
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 5
obstacle_low_value, obstacle_high_value = -500, 500 # # Set the highest-lowest addition number for Obstacle
obstacle_low_multiplier, obstacle_high_multiplier = 2, 5 # Set the highest-lowest Multiplication number for MuDi_Obstacle
MuDi_spawn_rate = 20 # chance of a MuDi_obstacle to spawn (%)


# Barrier settings
barrier_lowLimit = 100
barrier_highLimit = 500
barrier_addConstant = 500