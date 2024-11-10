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











# Function to add obstacles by random
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
    SCREEN_WIDTH = pygame.display.Info().current_w 
    SCREEN_HEIGHT =  pygame.display.Info().current_h 
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


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# newGameButton = pygwidgets.TextButton(screen, (20, 230),'New Game', width=100, height=45)


# startButton = pygwidgets.CustomButton(screen, (button_x, button_y),
#            'pygame/img/startb.png',
#             down='pygame/img/startb.png',
#             over='pygame/img/startb.png',
#             disabled='pygame/img/startb.png')

# def update_button_position():
#     screen_width = pygame.display.Info().current_w 
#     screen_height = pygame.display.Info().current_h 
#     button_x = screen_width // 2 - x
#     button_y = screen_height // 2 - y
#     startButton.setLoc((button_x, button_y))

