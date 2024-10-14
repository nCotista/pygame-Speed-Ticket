
from setting import *
import pygame
from object import *

def Draw_player():
    player_x = get_lane_x_position(player_lane, player_y) - player_width // 2
    player_scale = 1 + (player_y / SCREEN_HEIGHT)  # Scale the player based on Y position
    scaled_player_width = int(player_width * player_scale)
    scaled_player_height = int(player_height * player_scale)

    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, scaled_player_width, scaled_player_height))