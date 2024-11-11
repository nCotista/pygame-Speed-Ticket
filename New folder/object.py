import random

from pygame import font
from pygame.time import delay

from setting import *
import pygame


import random
from setting import *
import pygame


class Obstacle:
    def __init__(self, lane):
        self.lane = lane

        # Set initial position and size
        self.size = random.randint(30, 50)
        self.y = -self.size
        self.x = get_lane_x_position(self.lane, self.y)
        
        # Load obstacle image
        
        self.image = pygame.image.load('ham.PNG').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Speed addition/subtraction settings
        self.speedChanger = random.randint(-250, 400)
        self.font = pygame.font.Font(None, 72)
        self.text = self.font.render(str(self.speedChanger), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y - 50))

    def obstacle_move(self):
        # Move down the screen
        self.y += obstacle_speed
        
        # Scale for depth effect
        scale = 1 + (self.y / SCREEN_HEIGHT)
        scaled_width = int(obstacle_width * scale)
        scaled_height = int(obstacle_height * scale)
        self.x = get_lane_x_position(self.lane, self.y)

        # Update image size and position
        scaled_image = pygame.transform.scale(self.image, (scaled_width, scaled_height))
        screen.blit(scaled_image, (self.x, self.y))

        # Draw text on the obstacle
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y - 50))
        screen.blit(self.text, self.text_rect)

    def get_rect(self):
        # Return rect for collision
        return pygame.Rect(self.x, self.y, self.size, self.size)


class Barrier(Obstacle):
    def __init__(self, lane):
        super().__init__(lane)

        # Load barrier image
        self.image = pygame.image.load('tree.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        
        # Barrier-specific speed limit
        self.color = (0, 0, 255)
        self.speedLimit = random.randint(barrier_lowLimit, barrier_highLimit)
        self.text = self.font.render(str(self.speedLimit), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y - 50))


def create_obstacle():
    obstacles.append(Obstacle(0))
    obstacles.append(Obstacle(1))

# Function to create barriers
def create_barrier():
    obstacles.append(Barrier(0))
    obstacles.append(Barrier(1))

# Function to draw the road with perspective
# Function to draw the road with perspective and a center line
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
ROAD_COLOR = (50, 50, 50)  # Dark gray for the road
CENTER_LINE_COLOR = (255, 255, 0)  # Yellow for center line

# Define road properties
road_bottom_width = SCREEN_WIDTH * 0.8  # 80% of the screen width
road_top_width = SCREEN_WIDTH * 0.2     # 20% of the screen width (far distance)
num_dashes = 20  # Number of dashes in the center line

# Initialize variables for dash movement



def draw_perspective_road(dash_offset):
    # Define the four points of the trapezoid (road)
    road_bottom_left = (SCREEN_WIDTH // 2 - road_bottom_width // 2, SCREEN_HEIGHT)
    road_bottom_right = (SCREEN_WIDTH // 2 + road_bottom_width // 2, SCREEN_HEIGHT)
    road_top_left = (SCREEN_WIDTH // 2 - road_top_width // 2, 0)
    road_top_right = (SCREEN_WIDTH // 2 + road_top_width // 2, 0)

    # Draw the road as a trapezoid
    pygame.draw.polygon(screen, ROAD_COLOR, [road_bottom_left, road_bottom_right, road_top_right, road_top_left])

    # Define center line positions (narrower at top for perspective)
    center_bottom_left = (SCREEN_WIDTH // 2 - 5, SCREEN_HEIGHT)
    center_bottom_right = (SCREEN_WIDTH // 2 + 5, SCREEN_HEIGHT)
    center_top_left = (SCREEN_WIDTH // 2 - 2, 0)
    center_top_right = (SCREEN_WIDTH // 2 + 2, 0)

    # Draw dashed center line with perspective effect
    for i in range(num_dashes):
        # Interpolate positions for each dash segment
        t = (i + dash_offset) / num_dashes  # การใช้ dash_offset เพื่อเคลื่อนที่
        dash_bottom_left = (
            center_bottom_left[0] + t * (center_top_left[0] - center_bottom_left[0]),
            center_bottom_left[1] + t * (center_top_left[1] - center_bottom_left[1])
        )
        dash_bottom_right = (
            center_bottom_right[0] + t * (center_top_right[0] - center_bottom_right[0]),
            center_bottom_right[1] + t * (center_top_right[1] - center_bottom_right[1])
        )

        t_next = (i + 1 + dash_offset) / num_dashes
        dash_top_left = (
            center_bottom_left[0] + t_next * (center_top_left[0] - center_bottom_left[0]),
            center_bottom_left[1] + t_next * (center_top_left[1] - center_bottom_left[1])
        )
        dash_top_right = (
            center_bottom_right[0] + t_next * (center_top_right[0] - center_bottom_right[0]),
            center_bottom_right[1] + t_next * (center_top_right[1] - center_bottom_right[1])
        )

        # Draw every other segment to create dashed effect
        if i % 2 == 0:
            pygame.draw.polygon(screen, CENTER_LINE_COLOR, [dash_bottom_left, dash_bottom_right, dash_top_right, dash_top_left])
# Function to calculate lane X position based on Y (depth effect)
def get_lane_x_position(lane, y):
    road_bottom_width = SCREEN_WIDTH * 0.8
    road_top_width = SCREEN_WIDTH * 0.2

    # Linear interpolation between top and bottom lane positions based on Y
    road_width_at_y = road_top_width + (road_bottom_width - road_top_width) * (y / SCREEN_HEIGHT) #come from chat gpt

    if lane == 0:  # Left lane
        return SCREEN_WIDTH // 2 - road_width_at_y // 4  
    elif lane == 1:  # Right lane
        return SCREEN_WIDTH // 2 + road_width_at_y // 4  
    


