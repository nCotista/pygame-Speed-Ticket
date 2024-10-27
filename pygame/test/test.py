# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Game Home Page')

# # Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BUTTON_COLOR = (100, 200, 100)
# BUTTON_HOVER_COLOR = (50, 150, 50)

# # Load fonts
# font = pygame.font.SysFont(None, 55)
# button_font = pygame.font.SysFont(None, 45)

# # Define functions
# def draw_text(text, font, color, surface, x, y):
#     text_obj = font.render(text, True, color)
#     text_rect = text_obj.get_rect(center=(x, y))
#     surface.blit(text_obj, text_rect)

# def game_loop():
#     screen.fill(WHITE)
#     draw_text("Game Screen", font, BLACK, screen, screen_width//2, screen_height//2)
#     pygame.display.flip()
#     pygame.time.wait(2000)  # Placeholder for actual game logic

# def main_menu():
#     while True:
#         screen.fill(WHITE)

#         # Title Text
#         draw_text('Game Home Page', font, BLACK, screen, screen_width // 2, 100)

#         # Start Button
#         mouse_pos = pygame.mouse.get_pos()
#         start_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)

#         # Check if mouse is hovering the button
#         if start_button.collidepoint(mouse_pos):
#             pygame.draw.rect(screen, BUTTON_HOVER_COLOR, start_button)
#         else:
#             pygame.draw.rect(screen, BUTTON_COLOR, start_button)

#         draw_text('Start Game', button_font, WHITE, screen, screen_width // 2, screen_height // 2 + 25)

#         # Event handling
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if start_button.collidepoint(event.pos):
#                     game_loop()  # Start the game

#         pygame.display.update()

# # Run the main menu
# main_menu()


# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set screen dimensions
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # Load background image (make sure it's the same width as the screen)
# background = pygame.image.load('img/testimg.jpg')
# background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# # Variables to keep track of background position
# background_x1 = 0
# background_x2 = SCREEN_WIDTH  # Second background starts where the first one ends
# scroll_speed = 5  # Speed at which the background scrolls

# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Move backgrounds to the left
#     background_x1 -= scroll_speed
#     background_x2 -= scroll_speed

#     # If one of the backgrounds moves off the screen, reset its position
#     if background_x1 <= -SCREEN_WIDTH:
#         background_x1 = SCREEN_WIDTH
#     if background_x2 <= -SCREEN_WIDTH:
#         background_x2 = SCREEN_WIDTH

#     # Draw the two backgrounds
#     screen.blit(background, (background_x1, 0))
#     screen.blit(background, (background_x2, 0))

#     # Update the display
#     pygame.display.update()

#     # Frame rate
#     pygame.time.Clock().tick(60)

# # Quit Pygame
# pygame.quit()
# sys.exit()



# import pygame
# import random
# import sys

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # Colors
# WHITE = (255, 255, 255)

# # Player settings
# player_x = SCREEN_WIDTH // 2
# player_y = SCREEN_HEIGHT - 100
# player_width, player_height = 50, 100
# player_speed = 10
# player_lane = 1  # 0 = left, 1 = middle, 2 = right

# # Obstacles
# obstacles = []

# # Lane positions
# lanes = [SCREEN_WIDTH // 4, SCREEN_WIDTH // 2, 3 * SCREEN_WIDTH // 4]

# # Obstacle settings
# obstacle_width, obstacle_height = 50, 50
# obstacle_speed = 5

# # Function to add obstacles
# def add_obstacle():
#     lane = random.choice([0, 1, 2])
#     size = random.randint(30, 50)
#     new_obstacle = {
#         "x": lanes[lane],
#         "y": -size,
#         "size": size,
#         "lane": lane
#     }
#     obstacles.append(new_obstacle)

# # Main game loop
# running = True
# while running:
#     screen.fill(WHITE)
    
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     # Player controls (move between lanes)
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_lane > 0:
#         player_lane -= 1
#         player_x = lanes[player_lane] - player_width // 2
#     if keys[pygame.K_RIGHT] and player_lane < 2:
#         player_lane += 1
#         player_x = lanes[player_lane] - player_width // 2

#     # Draw player (fixed at the bottom of the screen)
#     pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

#     # Add obstacles
#     if random.randint(0, 100) < 2:  # 2% chance per frame to generate obstacle
#         add_obstacle()

#     # Update obstacles and draw them
#     for obstacle in obstacles[:]:
#         obstacle["y"] += obstacle_speed
#         # Scale the obstacle based on its y-position (depth effect)
#         scale = 1 + (obstacle["y"] / SCREEN_HEIGHT)
#         scaled_width = int(obstacle_width * scale)
#         scaled_height = int(obstacle_height * scale)
#         scaled_x = obstacle["x"] - (scaled_width // 2)  # Center the obstacle

#         # Draw obstacle
#         pygame.draw.rect(screen, (255, 0, 0), (scaled_x, obstacle["y"], scaled_width, scaled_height))

#         # Remove obstacles that go off the screen
#         if obstacle["y"] > SCREEN_HEIGHT:
#             obstacles.remove(obstacle)

#     # Update the display
#     pygame.display.update()

#     # Frame rate
#     pygame.time.Clock().tick(60)

# # Quit Pygame
# pygame.quit()
# sys.exit()





# import pygame
# import random
# import sys

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # Colors
# WHITE = (255, 255, 255)
# ROAD_COLOR = (50, 50, 50)

# # Player settings
# player_x = SCREEN_WIDTH // 2
# player_y = SCREEN_HEIGHT - 100
# player_width, player_height = 50, 100
# player_speed = 10
# player_lane = 1  # 0 = left, 1 = middle, 2 = right

# # Obstacles
# obstacles = []

# # Lane positions
# lanes = [SCREEN_WIDTH // 4, SCREEN_WIDTH // 2, 3 * SCREEN_WIDTH // 4]

# # Obstacle settings
# obstacle_width, obstacle_height = 50, 50
# obstacle_speed = 5

# # Function to add obstacles
# def add_obstacle():
#     lane = random.choice([0, 1, 2])
#     size = random.randint(30, 50)
#     new_obstacle = {
#         "x": lanes[lane],
#         "y": -size,
#         "size": size,
#         "lane": lane
#     }
#     obstacles.append(new_obstacle)

# # Function to draw the road with perspective
# def draw_perspective_road():
#     # Bottom part of the road (close to player)
#     road_bottom_width = SCREEN_WIDTH * 0.8  # 80% of the screen width
#     road_top_width = SCREEN_WIDTH * 0.2     # 20% of the screen width (far distance)
#     road_height = SCREEN_HEIGHT

#     # Define the four points of the trapezoid (road)
#     road_bottom_left = (SCREEN_WIDTH // 2 - road_bottom_width // 2, SCREEN_HEIGHT)
#     road_bottom_right = (SCREEN_WIDTH // 2 + road_bottom_width // 2, SCREEN_HEIGHT)
#     road_top_left = (SCREEN_WIDTH // 2 - road_top_width // 2, 0)
#     road_top_right = (SCREEN_WIDTH // 2 + road_top_width // 2, 0)

#     # Draw the road as a trapezoid
#     pygame.draw.polygon(screen, ROAD_COLOR, [road_bottom_left, road_bottom_right, road_top_right, road_top_left])

# # Main game loop
# running = True
# while running:
#     screen.fill(WHITE)

#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Draw the road with perspective
#     draw_perspective_road()

#     # Player controls (move between lanes)
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_lane > 0:
#         player_lane -= 1
#         player_x = lanes[player_lane] - player_width // 2
#     if keys[pygame.K_RIGHT] and player_lane < 2:
#         player_lane += 1
#         player_x = lanes[player_lane] - player_width // 2

#     # Draw player (fixed at the bottom of the screen)
#     pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

#     # Add obstacles
#     if random.randint(0, 100) < 2:  # 2% chance per frame to generate obstacle
#         add_obstacle()

#     # Update obstacles and draw them
#     for obstacle in obstacles[:]:
#         obstacle["y"] += obstacle_speed
#         # Scale the obstacle based on its y-position (depth effect)
#         scale = 1 + (obstacle["y"] / SCREEN_HEIGHT)
#         scaled_width = int(obstacle_width * scale)
#         scaled_height = int(obstacle_height * scale)
#         scaled_x = obstacle["x"] - (scaled_width // 2)  # Center the obstacle

#         # Draw obstacle
#         pygame.draw.rect(screen, (255, 0, 0), (scaled_x, obstacle["y"], scaled_width, scaled_height))

#         # Remove obstacles that go off the screen
#         if obstacle["y"] > SCREEN_HEIGHT:
#             obstacles.remove(obstacle)

#     # Update the display
#     pygame.display.update()

#     # Frame rate
#     pygame.time.Clock().tick(60)

# # Quit Pygame
# pygame.quit()
# sys.exit()



import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
ROAD_COLOR = (50, 50, 50)

# Player settings
player_y = SCREEN_HEIGHT - 120  # Fixed Y position for the player (close to bottom)
player_width, player_height = 50, 100
player_lane = 1  # 0 = left, 1 = middle, 2 = right
lanes = [0, 1, 2]  # Lane IDs (left, middle, right)

# Obstacles
obstacles = []

# Obstacle settings
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 5

# Function to add obstacles
def add_obstacle():
    lane = random.choice([0, 1, 2])
    size = random.randint(30, 50)
    new_obstacle = {
        "lane": lane,
        "y": -size,  # Start off-screen
        "size": size
    }
    obstacles.append(new_obstacle)

# Function to draw the road with perspective
def draw_perspective_road():
    # Bottom part of the road (close to player)
    road_bottom_width = SCREEN_WIDTH * 0.8  # 80% of the screen width
    road_top_width = SCREEN_WIDTH * 0.2     # 20% of the screen width (far distance)

    # Define the four points of the trapezoid (road)
    road_bottom_left = (SCREEN_WIDTH // 2 - road_bottom_width // 2, SCREEN_HEIGHT)
    road_bottom_right = (SCREEN_WIDTH // 2 + road_bottom_width // 2, SCREEN_HEIGHT)
    road_top_left = (SCREEN_WIDTH // 2 - road_top_width // 2, 0)
    road_top_right = (SCREEN_WIDTH // 2 + road_top_width // 2, 0)

    # Draw the road as a trapezoid
    pygame.draw.polygon(screen, ROAD_COLOR, [road_bottom_left, road_bottom_right, road_top_right, road_top_left])

# Function to calculate lane X position based on Y (depth effect)
def get_lane_x_position(lane, y):
    road_bottom_width = SCREEN_WIDTH * 0.8
    road_top_width = SCREEN_WIDTH * 0.2

    # Linear interpolation between top and bottom lane positions based on Y
    road_width_at_y = road_top_width + (road_bottom_width - road_top_width) * (y / SCREEN_HEIGHT)

    if lane == 0:  # Left lane
        return SCREEN_WIDTH // 2 - road_width_at_y // 3
    elif lane == 1:  # Middle lane
        return SCREEN_WIDTH // 2
    elif lane == 2:  # Right lane
        return SCREEN_WIDTH // 2 + road_width_at_y // 3

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

    # Player controls (move between lanes)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_lane > 0:
        player_lane -= 1
    if keys[pygame.K_RIGHT] and player_lane < 2:
        player_lane += 1

    # Draw player
    player_x = get_lane_x_position(player_lane, player_y) - player_width // 2
    player_scale = 1 + (player_y / SCREEN_HEIGHT)  # Scale the player based on Y position
    scaled_player_width = int(player_width * player_scale)
    scaled_player_height = int(player_height * player_scale)

    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, scaled_player_width, scaled_player_height))

    # Add obstacles
    if random.randint(0, 100) < 2:  # 2% chance per frame to generate obstacle
        add_obstacle()

    # Update obstacles and draw them
    for obstacle in obstacles[:]:
        obstacle["y"] += obstacle_speed

        # Scale the obstacle based on its y-position (depth effect)
        scale = 1 + (obstacle["y"] / SCREEN_HEIGHT)
        scaled_width = int(obstacle_width * scale)
        scaled_height = int(obstacle_height * scale)
        obstacle_x = get_lane_x_position(obstacle["lane"], obstacle["y"]) - scaled_width // 2

        # Draw obstacle
        pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle["y"], scaled_width, scaled_height))

        # Remove obstacles that go off the screen
        if obstacle["y"] > SCREEN_HEIGHT:
            obstacles.remove(obstacle)

    # Update the display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
