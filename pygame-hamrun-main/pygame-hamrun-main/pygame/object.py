import random

from pygame import font
from pygame.time import delay

from setting import *
import pygame


class Obstacle:
    def __init__(self, lane):
        self.lane = lane

        # Basic + Co-ordinate Setting
        self.size = random.randint(30,50)
        self.y = -self.size
        self.x = get_lane_x_position(self.lane, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.color = (225, 0, 0)

        # Speed Addition/Subtraction + text Setting
        self.speedChanger = random.randint(-250, 400)
        self.font = pygame.font.Font(None, 72)
        self.text = self.font.render(str(self.speedChanger), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y -50))

    def obstacle_move(self):
            self.y += obstacle_speed
            scale = 1 + (self.y / SCREEN_HEIGHT)
            scaled_width = int(obstacle_width * scale)  # obstacle_width in setting.py
            scaled_height = int(obstacle_height * scale)
            self.x = get_lane_x_position(self.lane, self.y)
            self.rect = pygame.Rect(self.x, self.y, scaled_width, scaled_height)

            pygame.draw.rect(screen, self.color, self.rect) # Draw Rect
            # Draw Text on Rect
            self.text_rect = self.text.get_rect(center=(self.x +25, self.y -50 ))
            screen.blit(self.text, self.text_rect)

    def get_rect(self):
        return self.rect

# TODO: Create a "Multiplication-Increase/Decrease" Obstacle

class Barrier(Obstacle):
    def __init__(self, lane):
        super().__init__(lane)

        self.color = (0, 0, 255)
        self.speedLimit = random.randint(barrier_lowLimit, barrier_highLimit)
        self.text = self.font.render(str(self.speedLimit), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y - 50))


# Function Section

def create_obstacle():
    obstacles.append(Obstacle(0))
    obstacles.append(Obstacle(1))

def create_barrier():
    obstacles.append(Barrier(0))
    obstacles.append(Barrier(1))

# Jay's Legacy
def add_obstacle():
    lane = random.choice([0, 1])
    size = random.randint(30, 50)
    new_obstacle = {
        "lane": lane,
        "y": -size,  # - เพื่อให้มันมาจากสุดจอ
        "size": size
    }
    obstacles.append(new_obstacle)

# Function to draw the road with perspective
def draw_perspective_road():
    # Bottom part of the road (close to player)
    road_bottom_width = SCREEN_WIDTH * 0.8  # 80% of the screen width
    road_top_width = SCREEN_WIDTH * 0.2     # 20% of the screen width (far distance)

    # Define the four points of the trapezoid (road) เพื่อเอามาวาดคางหมูกลางจอ
    road_bottom_left = (SCREEN_WIDTH // 2 - road_bottom_width // 2, SCREEN_HEIGHT) #(x,y)  x จับหารสองจะได้กลางจอ อยากได้ความกว้าง80 จับหารสองอีกฝั่งนึงเอาไปบวก อีกฝั่งเอาไปลบจากกลางจอจะรวมกันได้ % ที่ต้องการ
    road_bottom_right = (SCREEN_WIDTH // 2 + road_bottom_width // 2, SCREEN_HEIGHT) # y  SCREEN_HEIGHT ให้พิกัดล่างสุด 0 ให้บนสุด
    road_top_left = (SCREEN_WIDTH // 2 - road_top_width // 2, 0)
    road_top_right = (SCREEN_WIDTH // 2 + road_top_width // 2, 0)

    # Draw the road as a trapezoid
    pygame.draw.polygon(screen, ROAD_COLOR, [road_bottom_left, road_bottom_right, road_top_right, road_top_left])

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

