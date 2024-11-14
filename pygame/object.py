import random
from setting import *
import pygame
from creater import *
# from pygame_widgets.slider import Slider
# from pygame_widgets.textbox import TextBox


#picture
background = pygame.image.load('pygame/img/Pixellance.png')
uibg = pygame.image.load('pygame/img/uibg.jpg')

#button from creater
start_button = CustomButton(screen, 200, -150, 'pygame/img/startb.png') #note the same value !!!!!!!!11
meun_button = CustomButton(screen, 0, -150, 'pygame/img/menu.png') 

#pygwidgets object
musicSound = pygwidgets.BackgroundSound('pygame/sound/bgm.mp3')
myDisplayText = pygwidgets.DisplayText(screen, (100, 200),textColor=(255, 255, 255))

# test = random.randint(1, 800)
#pygame_widgets
#slider = Slider(Surface x, y, w, h, )
# slider = Slider(screen, test, 100, 800, 40, min=0, max=99, step=1)
# output = TextBox(screen, 475, 200, 50, 50, fontSize=30)


slider = Slider(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), size=(300, 20), initial_val=0.5, min=0, max=100)











class Obstacle:
    def __init__(self, lane):
        self.lane = lane

        # Basic + Co-ordinate Setting
        self.size = random.randint(30,50)
        self.y = -self.size
        self.x = get_lane_x_position(self.lane, self.y)
        # Load obstacle image
        
        self.image = pygame.image.load('pygame\img\ham.PNG').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        # Speed Addition/Subtraction + text Setting
        self.speedChanger = random.randint(obstacle_low_value, obstacle_high_value)
        self.font = pygame.font.Font(None, 72)
        self.text = self.font.render(str(self.speedChanger), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y -50))

    def obstacle_move(self):
            self.y += obstacle_speed
            scale = 1 + (self.y / SCREEN_HEIGHT)
            scaled_width = int(obstacle_width * scale)  # obstacle_width in setting.py
            scaled_height = int(obstacle_height * scale)
            self.x = get_lane_x_position(self.lane, self.y)
            # Update image size and position
            scaled_image = pygame.transform.scale(self.image, (scaled_width, scaled_height))
            screen.blit(scaled_image, (self.x, self.y))

            # Draw Text on Rect
            self.text_rect = self.text.get_rect(center=(self.x +25, self.y -50 ))
            screen.blit(self.text, self.text_rect)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

class MuDi_Obstacle(Obstacle):
    def __init__(self, lane):
        super().__init__(lane)

        self.operator = random.choice(['X', '%'])
        self.muDiNum = random.randint(obstacle_low_multiplier, obstacle_high_multiplier)
        self.speedChanger = self.muDiNum if self.operator == 'X' else 1/self.muDiNum
        self.text = self.font.render(str(f'{self.operator} {self.muDiNum}'), True, (255, 255, 255))

    def get_total(self, player_speed):
        return int(player_speed * self.speedChanger)

class Barrier(Obstacle):
    def __init__(self, lane, low, high):
        super().__init__(lane)

        # Load barrier image
        self.image = pygame.image.load('pygame/img/car.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        
        # Barrier-specific speed limit
        self.color = (0, 0, 255)
        self.speedLimit = random.randint(barrier_lowLimit, barrier_highLimit)
        self.text = self.font.render(str(self.speedLimit), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y - 50))


# Function Section

def create_obstacle():
    for i in range(0, 2):
        if random.randint(0, 100) < MuDi_spawn_rate: # 20% to spawn a Multiplication Obstacle(MuDi_Obstacle)
            obstacles.append(MuDi_Obstacle(i))
        else:
            obstacles.append(Obstacle(i))

def create_barrier(low, high):
    obstacles.append(Barrier(0, low, high))
    obstacles.append(Barrier(1, low, high))

# Function to draw the road with perspective
def draw_perspective_road():
    # Bottom part of the road (close to player)
    SCREEN_WIDTH = pygame.display.Info().current_w 
    SCREEN_HEIGHT =  pygame.display.Info().current_h 
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
    SCREEN_WIDTH = pygame.display.Info().current_w 
    SCREEN_HEIGHT =  pygame.display.Info().current_h 
    road_bottom_width = SCREEN_WIDTH * 0.8
    road_top_width = SCREEN_WIDTH * 0.2

    # Linear interpolation between top and bottom lane positions based on Y
    road_width_at_y = road_top_width + (road_bottom_width - road_top_width) * (y / SCREEN_HEIGHT) #come from chat gpt

    if lane == 0:  # Left lane
        return SCREEN_WIDTH // 2 - road_width_at_y // 4
    elif lane == 1:  # Right lane
        return SCREEN_WIDTH // 2 + road_width_at_y // 4


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


class RoadRenderer:
    def __init__(self, screen, road_image):
        self.screen = screen
        self.road_image = road_image
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
    def render(self, car_x=0):
        # Update screen dimensions
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        
        # Render road slices with perspective effect
        for i in range(self.screen_height):
            # Calculate scale based on distance from viewer
            scale = (self.screen_height - i) / self.screen_height
            
            # Calculate position of the road slice
            y = int(car_x % self.road_image.get_height())
            road_slice = self.road_image.subsurface((0, y, self.road_image.get_width(), 1))
            
            # Scale the slice to create perspective effect
            scaled_slice = pygame.transform.scale(
                road_slice, 
                (int(self.screen_width * scale), 1)
            )
            
            # Position the slice to create vanishing point
            self.screen.blit(
                scaled_slice, 
                (int((self.screen_width / 2) * (1 - scale)), self.screen_height - i)
            )