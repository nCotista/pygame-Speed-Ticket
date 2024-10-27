import pygame
from pygame.locals import *
pygame.init()
# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
mainClock = pygame.time.Clock()
fullscreen = False

font = pygame.font.SysFont(None, 20)

#Colors
WHITE = (255, 255, 255)
ROAD_COLOR = (50, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (50, 150, 50)


# Player settings
# player_y = SCREEN_HEIGHT - 120 /ไปเขียนในลูปดพราะมันต้องเปลีี่ยนค่าตามขนาดจอ
player_width, player_height = 50, 100
player_lane = 0  # 0 = left 1 right
lanes = [0, 1]  # Lane IDs (left, right)

# Obstacles
obstacles = []

# Obstacle settings
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 5