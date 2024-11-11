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

# Obstacles
obstacles = []

# Obstacle settings
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 5