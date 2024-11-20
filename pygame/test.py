# # # # # # import pygame
# # # # # # import sys

# # # # # # # Initialize Pygame
# # # # # # pygame.init()

# # # # # # # Set up the screen
# # # # # # screen_width, screen_height = 800, 600
# # # # # # screen = pygame.display.set_mode((screen_width, screen_height))
# # # # # # pygame.display.set_caption('Game Home Page')

# # # # # # # Define colors
# # # # # # WHITE = (255, 255, 255)
# # # # # # BLACK = (0, 0, 0)
# # # # # # BUTTON_COLOR = (100, 200, 100)
# # # # # # BUTTON_HOVER_COLOR = (50, 150, 50)

# # # # # # # Load fonts
# # # # # # font = pygame.font.SysFont(None, 55)
# # # # # # button_font = pygame.font.SysFont(None, 45)

# # # # # # # Define functions
# # # # # # def draw_text(text, font, color, surface, x, y):
# # # # # #     text_obj = font.render(text, True, color)
# # # # # #     text_rect = text_obj.get_rect(center=(x, y))
# # # # # #     surface.blit(text_obj, text_rect)

# # # # # # def game_loop():
# # # # # #     screen.fill(WHITE)
# # # # # #     draw_text("Game Screen", font, BLACK, screen, screen_width//2, screen_height//2)
# # # # # #     pygame.display.flip()
# # # # # #     pygame.time.wait(2000)  # Placeholder for actual game logic

# # # # # # def main_menu():
# # # # # #     while True:
# # # # # #         screen.fill(WHITE)

# # # # # #         # Title Text
# # # # # #         draw_text('Game Home Page', font, BLACK, screen, screen_width // 2, 100)

# # # # # #         # Start Button
# # # # # #         mouse_pos = pygame.mouse.get_pos()
# # # # # #         start_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)

# # # # # #         # Check if mouse is hovering the button
# # # # # #         if start_button.collidepoint(mouse_pos):
# # # # # #             pygame.draw.rect(screen, BUTTON_HOVER_COLOR, start_button)
# # # # # #         else:
# # # # # #             pygame.draw.rect(screen, BUTTON_COLOR, start_button)

# # # # # #         draw_text('Start Game', button_font, WHITE, screen, screen_width // 2, screen_height // 2 + 25)

# # # # # #         # Event handling
# # # # # #         for event in pygame.event.get():
# # # # # #             if event.type == pygame.QUIT:
# # # # # #                 pygame.quit()
# # # # # #                 sys.exit()

# # # # # #             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
# # # # # #                 if start_button.collidepoint(event.pos):
# # # # # #                     game_loop()  # Start the game

# # # # # #         pygame.display.update()

# # # # # # # Run the main menu
# # # # # # main_menu()


# # # # # # import pygame
# # # # # # import sys

# # # # # # # Initialize Pygame
# # # # # # pygame.init()

# # # # # # # Set screen dimensions
# # # # # # SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# # # # # # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # # # # # # Load background image (make sure it's the same width as the screen)
# # # # # # background = pygame.image.load('img/testimg.jpg')
# # # # # # background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# # # # # # # Variables to keep track of background position
# # # # # # background_x1 = 0
# # # # # # background_x2 = SCREEN_WIDTH  # Second background starts where the first one ends
# # # # # # scroll_speed = 5  # Speed at which the background scrolls

# # # # # # # Main game loop
# # # # # # running = True
# # # # # # while running:
# # # # # #     for event in pygame.event.get():
# # # # # #         if event.type == pygame.QUIT:
# # # # # #             running = False

# # # # # #     # Move backgrounds to the left
# # # # # #     background_x1 -= scroll_speed
# # # # # #     background_x2 -= scroll_speed

# # # # # #     # If one of the backgrounds moves off the screen, reset its position
# # # # # #     if background_x1 <= -SCREEN_WIDTH:
# # # # # #         background_x1 = SCREEN_WIDTH
# # # # # #     if background_x2 <= -SCREEN_WIDTH:
# # # # # #         background_x2 = SCREEN_WIDTH

# # # # # #     # Draw the two backgrounds
# # # # # #     screen.blit(background, (background_x1, 0))
# # # # # #     screen.blit(background, (background_x2, 0))

# # # # # #     # Update the display
# # # # # #     pygame.display.update()

# # # # # #     # Frame rate
# # # # # #     pygame.time.Clock().tick(60)

# # # # # # # Quit Pygame
# # # # # # pygame.quit()
# # # # # # sys.exit()



# # # # # # import pygame
# # # # # # import random
# # # # # # import sys

# # # # # # # Initialize Pygame
# # # # # # pygame.init()

# # # # # # # Screen dimensions
# # # # # # SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# # # # # # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # # # # # # Colors
# # # # # # WHITE = (255, 255, 255)

# # # # # # # Player settings
# # # # # # player_x = SCREEN_WIDTH // 2
# # # # # # player_y = SCREEN_HEIGHT - 100
# # # # # # player_width, player_height = 50, 100
# # # # # # player_speed = 10
# # # # # # player_lane = 1  # 0 = left, 1 = middle, 2 = right

# # # # # # # Obstacles
# # # # # # obstacles = []

# # # # # # # Lane positions
# # # # # # lanes = [SCREEN_WIDTH // 4, SCREEN_WIDTH // 2, 3 * SCREEN_WIDTH // 4]

# # # # # # # Obstacle settings
# # # # # # obstacle_width, obstacle_height = 50, 50
# # # # # # obstacle_speed = 5

# # # # # # # Function to add obstacles
# # # # # # def add_obstacle():
# # # # # #     lane = random.choice([0, 1, 2])
# # # # # #     size = random.randint(30, 50)
# # # # # #     new_obstacle = {
# # # # # #         "x": lanes[lane],
# # # # # #         "y": -size,
# # # # # #         "size": size,
# # # # # #         "lane": lane
# # # # # #     }
# # # # # #     obstacles.append(new_obstacle)

# # # # # # # Main game loop
# # # # # # running = True
# # # # # # while running:
# # # # # #     screen.fill(WHITE)
    
# # # # # #     # Event handling
# # # # # #     for event in pygame.event.get():
# # # # # #         if event.type == pygame.QUIT:
# # # # # #             running = False
    
# # # # # #     # Player controls (move between lanes)
# # # # # #     keys = pygame.key.get_pressed()
# # # # # #     if keys[pygame.K_LEFT] and player_lane > 0:
# # # # # #         player_lane -= 1
# # # # # #         player_x = lanes[player_lane] - player_width // 2
# # # # # #     if keys[pygame.K_RIGHT] and player_lane < 2:
# # # # # #         player_lane += 1
# # # # # #         player_x = lanes[player_lane] - player_width // 2

# # # # # #     # Draw player (fixed at the bottom of the screen)
# # # # # #     pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

# # # # # #     # Add obstacles
# # # # # #     if random.randint(0, 100) < 2:  # 2% chance per frame to generate obstacle
# # # # # #         add_obstacle()

# # # # # #     # Update obstacles and draw them
# # # # # #     for obstacle in obstacles[:]:
# # # # # #         obstacle["y"] += obstacle_speed
# # # # # #         # Scale the obstacle based on its y-position (depth effect)
# # # # # #         scale = 1 + (obstacle["y"] / SCREEN_HEIGHT)
# # # # # #         scaled_width = int(obstacle_width * scale)
# # # # # #         scaled_height = int(obstacle_height * scale)
# # # # # #         scaled_x = obstacle["x"] - (scaled_width // 2)  # Center the obstacle

# # # # # #         # Draw obstacle
# # # # # #         pygame.draw.rect(screen, (255, 0, 0), (scaled_x, obstacle["y"], scaled_width, scaled_height))

# # # # # #         # Remove obstacles that go off the screen
# # # # # #         if obstacle["y"] > SCREEN_HEIGHT:
# # # # # #             obstacles.remove(obstacle)

# # # # # #     # Update the display
# # # # # #     pygame.display.update()

# # # # # #     # Frame rate
# # # # # #     pygame.time.Clock().tick(60)

# # # # # # # Quit Pygame
# # # # # # pygame.quit()
# # # # # # sys.exit()





# # # # # # import pygame
# # # # # # import random
# # # # # # import sys

# # # # # # # Initialize Pygame
# # # # # # pygame.init()

# # # # # # # Screen dimensions
# # # # # # SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# # # # # # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # # # # # # Colors
# # # # # # WHITE = (255, 255, 255)
# # # # # # ROAD_COLOR = (50, 50, 50)

# # # # # # # Player settings
# # # # # # player_x = SCREEN_WIDTH // 2
# # # # # # player_y = SCREEN_HEIGHT - 100
# # # # # # player_width, player_height = 50, 100
# # # # # # player_speed = 10
# # # # # # player_lane = 1  # 0 = left, 1 = middle, 2 = right

# # # # # # # Obstacles
# # # # # # obstacles = []

# # # # # # # Lane positions
# # # # # # lanes = [SCREEN_WIDTH // 4, SCREEN_WIDTH // 2, 3 * SCREEN_WIDTH // 4]

# # # # # # # Obstacle settings
# # # # # # obstacle_width, obstacle_height = 50, 50
# # # # # # obstacle_speed = 5

# # # # # # # Function to add obstacles
# # # # # # def add_obstacle():
# # # # # #     lane = random.choice([0, 1, 2])
# # # # # #     size = random.randint(30, 50)
# # # # # #     new_obstacle = {
# # # # # #         "x": lanes[lane],
# # # # # #         "y": -size,
# # # # # #         "size": size,
# # # # # #         "lane": lane
# # # # # #     }
# # # # # #     obstacles.append(new_obstacle)

# # # # # # # Function to draw the road with perspective
# # # # # # def draw_perspective_road():
# # # # # #     # Bottom part of the road (close to player)
# # # # # #     road_bottom_width = SCREEN_WIDTH * 0.8  # 80% of the screen width
# # # # # #     road_top_width = SCREEN_WIDTH * 0.2     # 20% of the screen width (far distance)
# # # # # #     road_height = SCREEN_HEIGHT

# # # # # #     # Define the four points of the trapezoid (road)
# # # # # #     road_bottom_left = (SCREEN_WIDTH // 2 - road_bottom_width // 2, SCREEN_HEIGHT)
# # # # # #     road_bottom_right = (SCREEN_WIDTH // 2 + road_bottom_width // 2, SCREEN_HEIGHT)
# # # # # #     road_top_left = (SCREEN_WIDTH // 2 - road_top_width // 2, 0)
# # # # # #     road_top_right = (SCREEN_WIDTH // 2 + road_top_width // 2, 0)

# # # # # #     # Draw the road as a trapezoid
# # # # # #     pygame.draw.polygon(screen, ROAD_COLOR, [road_bottom_left, road_bottom_right, road_top_right, road_top_left])

# # # # # # # Main game loop
# # # # # # running = True
# # # # # # while running:
# # # # # #     screen.fill(WHITE)

# # # # # #     # Event handling
# # # # # #     for event in pygame.event.get():
# # # # # #         if event.type == pygame.QUIT:
# # # # # #             running = False

# # # # # #     # Draw the road with perspective
# # # # # #     draw_perspective_road()

# # # # # #     # Player controls (move between lanes)
# # # # # #     keys = pygame.key.get_pressed()
# # # # # #     if keys[pygame.K_LEFT] and player_lane > 0:
# # # # # #         player_lane -= 1
# # # # # #         player_x = lanes[player_lane] - player_width // 2
# # # # # #     if keys[pygame.K_RIGHT] and player_lane < 2:
# # # # # #         player_lane += 1
# # # # # #         player_x = lanes[player_lane] - player_width // 2

# # # # # #     # Draw player (fixed at the bottom of the screen)
# # # # # #     pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

# # # # # #     # Add obstacles
# # # # # #     if random.randint(0, 100) < 2:  # 2% chance per frame to generate obstacle
# # # # # #         add_obstacle()

# # # # # #     # Update obstacles and draw them
# # # # # #     for obstacle in obstacles[:]:
# # # # # #         obstacle["y"] += obstacle_speed
# # # # # #         # Scale the obstacle based on its y-position (depth effect)
# # # # # #         scale = 1 + (obstacle["y"] / SCREEN_HEIGHT)
# # # # # #         scaled_width = int(obstacle_width * scale)
# # # # # #         scaled_height = int(obstacle_height * scale)
# # # # # #         scaled_x = obstacle["x"] - (scaled_width // 2)  # Center the obstacle

# # # # # #         # Draw obstacle
# # # # # #         pygame.draw.rect(screen, (255, 0, 0), (scaled_x, obstacle["y"], scaled_width, scaled_height))

# # # # # #         # Remove obstacles that go off the screen
# # # # # #         if obstacle["y"] > SCREEN_HEIGHT:
# # # # # #             obstacles.remove(obstacle)

# # # # # #     # Update the display
# # # # # #     pygame.display.update()

# # # # # #     # Frame rate
# # # # # #     pygame.time.Clock().tick(60)

# # # # # # # Quit Pygame
# # # # # # pygame.quit()
# # # # # # sys.exit()



# # # # # import pygame
# # # # # import random
# # # # # import sys

# # # # # # Initialize Pygame
# # # # # pygame.init()

# # # # # # Screen dimensions
# # # # # SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# # # # # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # # # # # Colors
# # # # # WHITE = (255, 255, 255)
# # # # # ROAD_COLOR = (50, 50, 50)

# # # # # # Player settings
# # # # # player_y = SCREEN_HEIGHT - 120  # Fixed Y position for the player (close to bottom)
# # # # # player_width, player_height = 50, 100
# # # # # player_lane = 1  # 0 = left, 1 = middle, 2 = right
# # # # # lanes = [0, 1, 2]  # Lane IDs (left, middle, right)

# # # # # # Obstacles
# # # # # obstacles = []

# # # # # # Obstacle settings
# # # # # obstacle_width, obstacle_height = 50, 50
# # # # # obstacle_speed = 5

# # # # # # Function to add obstacles
# # # # # def add_obstacle():
# # # # #     lane = random.choice([0, 1, 2])
# # # # #     size = random.randint(30, 50)
# # # # #     new_obstacle = {
# # # # #         "lane": lane,
# # # # #         "y": -size,  # Start off-screen
# # # # #         "size": size
# # # # #     }
# # # # #     obstacles.append(new_obstacle)

# # # # # # Function to draw the road with perspective
# # # # # def draw_perspective_road():
# # # # #     # Bottom part of the road (close to player)
# # # # #     road_bottom_width = SCREEN_WIDTH * 0.8  # 80% of the screen width
# # # # #     road_top_width = SCREEN_WIDTH * 0.2     # 20% of the screen width (far distance)

# # # # #     # Define the four points of the trapezoid (road)
# # # # #     road_bottom_left = (SCREEN_WIDTH // 2 - road_bottom_width // 2, SCREEN_HEIGHT)
# # # # #     road_bottom_right = (SCREEN_WIDTH // 2 + road_bottom_width // 2, SCREEN_HEIGHT)
# # # # #     road_top_left = (SCREEN_WIDTH // 2 - road_top_width // 2, 0)
# # # # #     road_top_right = (SCREEN_WIDTH // 2 + road_top_width // 2, 0)

# # # # #     # Draw the road as a trapezoid
# # # # #     pygame.draw.polygon(screen, ROAD_COLOR, [road_bottom_left, road_bottom_right, road_top_right, road_top_left])

# # # # # # Function to calculate lane X position based on Y (depth effect)
# # # # # def get_lane_x_position(lane, y):
# # # # #     road_bottom_width = SCREEN_WIDTH * 0.8
# # # # #     road_top_width = SCREEN_WIDTH * 0.2

# # # # #     # Linear interpolation between top and bottom lane positions based on Y
# # # # #     road_width_at_y = road_top_width + (road_bottom_width - road_top_width) * (y / SCREEN_HEIGHT)

# # # # #     if lane == 0:  # Left lane
# # # # #         return SCREEN_WIDTH // 2 - road_width_at_y // 3
# # # # #     elif lane == 1:  # Middle lane
# # # # #         return SCREEN_WIDTH // 2
# # # # #     elif lane == 2:  # Right lane
# # # # #         return SCREEN_WIDTH // 2 + road_width_at_y // 3

# # # # # # Main game loop
# # # # # running = True
# # # # # while running:
# # # # #     screen.fill(WHITE)

# # # # #     # Event handling
# # # # #     for event in pygame.event.get():
# # # # #         if event.type == pygame.QUIT:
# # # # #             running = False

# # # # #     # Draw the road with perspective
# # # # #     draw_perspective_road()

# # # # #     # Player controls (move between lanes)
# # # # #     keys = pygame.key.get_pressed()
# # # # #     if keys[pygame.K_LEFT] and player_lane > 0:
# # # # #         player_lane -= 1
# # # # #     if keys[pygame.K_RIGHT] and player_lane < 2:
# # # # #         player_lane += 1

# # # # #     # Draw player
# # # # #     player_x = get_lane_x_position(player_lane, player_y) - player_width // 2
# # # # #     player_scale = 1 + (player_y / SCREEN_HEIGHT)  # Scale the player based on Y position
# # # # #     scaled_player_width = int(player_width * player_scale)
# # # # #     scaled_player_height = int(player_height * player_scale)

# # # # #     pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, scaled_player_width, scaled_player_height))

# # # # #     # Add obstacles
# # # # #     if random.randint(0, 100) < 2:  # 2% chance per frame to generate obstacle
# # # # #         add_obstacle()

# # # # #     # Update obstacles and draw them
# # # # #     for obstacle in obstacles[:]:
# # # # #         obstacle["y"] += obstacle_speed

# # # # #         # Scale the obstacle based on its y-position (depth effect)
# # # # #         scale = 1 + (obstacle["y"] / SCREEN_HEIGHT)
# # # # #         scaled_width = int(obstacle_width * scale)
# # # # #         scaled_height = int(obstacle_height * scale)
# # # # #         obstacle_x = get_lane_x_position(obstacle["lane"], obstacle["y"]) - scaled_width // 2

# # # # #         # Draw obstacle
# # # # #         pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle["y"], scaled_width, scaled_height))

# # # # #         # Remove obstacles that go off the screen
# # # # #         if obstacle["y"] > SCREEN_HEIGHT:
# # # # #             obstacles.remove(obstacle)

# # # # #     # Update the display
# # # # #     pygame.display.update()

# # # # #     # Frame rate
# # # # #     pygame.time.Clock().tick(60)

# # # # # # Quit Pygame
# # # # # pygame.quit()
# # # # # sys.exit()



# # # # import pygame
# # # # import pygwidgets

# # # # # Initialize Pygame
# # # # pygame.init()

# # # # # Set initial screen dimensions
# # # # screen_width, screen_height = 800, 600
# # # # screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# # # # # Create the button with initial position
# # # # button_x = screen_width / 2 - 50  # Center the button horizontally
# # # # button_y = screen_height / 2 - 25  # Center the button vertically
# # # # myButton = pygwidgets.CustomButton(screen, (button_x, button_y),
# # # #                                     'pygame/img/start.png',
# # # #                                     down='pygame/img/start.png',
# # # #                                     over='pygame/img/start.png',
# # # #                                     disabled='pygame/img/start.png')

# # # # # Main loop
# # # # running = True
# # # # while running:
# # # #     for event in pygame.event.get():
# # # #         if event.type == pygame.QUIT:
# # # #             running = False
            
# # # #         # Handle window resize
# # # #         if event.type == pygame.VIDEORESIZE:
# # # #             screen_width, screen_height = event.w, event.h
# # # #             screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            
# # # #             # Update the button's position
# # # #             button_x = screen_width / 2 - 50  # Recalculate new x position
# # # #             button_y = screen_height / 2 - 25  # Recalculate new y position
            
# # # #             # Recreate the button with the updated position
# # # #             myButton = pygwidgets.CustomButton(screen, (button_x, button_y),
# # # #                                                 'pygame/img/start.png',
# # # #                                                 down='pygame/img/start.png',
# # # #                                                 over='pygame/img/start.png',
# # # #                                                 disabled='pygame/img/start.png')

# # # #     # Clear the screen
# # # #     screen.fill((255, 255, 255))
    
# # # #     # Draw the button
# # # #     myButton.draw()

# # # #     # Update the display
# # # #     pygame.display.flip()

# # # # # Quit Pygame
# # # # pygame.quit()


# # # import pygame
# # # import pygwidgets

# # # class CustomButton:
# # #     def __init__(self, screen, image_path, position):
# # #         self.screen = screen
# # #         self.image_path = image_path
# # #         self.button = pygwidgets.CustomButton(screen, position,
# # #                                                image_path,
# # #                                                down=image_path,
# # #                                                over=image_path,
# # #                                                disabled=image_path)
# # #         self.position = position

# # #     def update_position(self, new_x, new_y):
# # #         """Update the button's position to the specified coordinates."""
# # #         self.position = (new_x, new_y)
# # #         self.button.setLoc(self.position)

# # #     def draw(self):
# # #         """Draw the button on the screen."""
# # #         self.button.draw()

# # # # Example usage:
# # # # Initialize Pygame and create a screen object
# # # pygame.init()
# # # screen = pygame.display.set_mode((800, 600))

# # # # Create an instance of CustomButton
# # # my_button = CustomButton(screen, 'pygame/img/start.png', (100, 100))

# # # # Main loop
# # # running = True
# # # while running:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # #     # Example of updating the button position to the center of the screen
# # #     screen_width = pygame.display.Info().current_w
# # #     screen_height = pygame.display.Info().current_h
# # #     my_button.update_position(screen_width // 2, screen_height // 2)

# # #     # Clear the screen and draw the button
# # #     screen.fill((255, 255, 255))  # Fill the screen with white
# # #     my_button.draw()

# # #     pygame.display.flip()

# # # pygame.quit()

# # import pygame
# # import pygwidgets

# # class CustomButton:
# #     def __init__(self, screen, image_path, position):
# #         self.screen = screen
# #         self.image_path = image_path
# #         self.button = pygwidgets.CustomButton(screen, position,
# #                                                image_path,
# #                                                down=image_path,
# #                                                over=image_path,
# #                                                disabled=image_path)
# #         self.position = position

# #     def update_position(self, new_x, new_y):
# #         """Update the button's position to the specified coordinates."""
# #         self.position = (new_x, new_y)
# #         self.button.setLoc(self.position)

# #     def draw(self):
# #         """Draw the button on the screen."""
# #         self.button.draw()

# # # Example usage:
# # # Initialize Pygame and create a screen object
# # pygame.init()
# # screen = pygame.display.set_mode((800, 600))

# # # Create an instance of CustomButton
# # my_button = CustomButton(screen, 'pygame/img/start.png', (100, 100))

# # # Get initial screen dimensions
# # previous_width, previous_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# # # Main loop
# # running = True
# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #     # Get current screen dimensions
# #     current_width, current_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# #     # Check if the screen size has changed
# #     if (current_width, current_height) != (previous_width, previous_height):
# #         # Update the button position to the center of the new screen size
# #         my_button.update_position(current_width // 2, current_height // 2)
# #         # Update previous dimensions
# #         previous_width, previous_height = current_width, current_height

# #     # Clear the screen and draw the button
# #     screen.fill((255, 255, 255))  # Fill the screen with white
# #     my_button.draw()

# #     pygame.display.flip()

# # pygame.quit()



# # import pygame
# # import pygwidgets

# # class CustomButton:
# #     def __init__(self, screen, x, y, image_path):
# #         self.screen = screen
# #         self.button = pygwidgets.CustomButton(screen, (x, y),
# #                                                image_path,
# #                                                down=image_path,
# #                                                over=image_path,
# #                                                disabled=image_path)
# #         self.x = x
# #         self.y = y

# #     def update_position(self):
# #         screen_width = pygame.display.Info().current_w 
# #         screen_height = pygame.display.Info().current_h 
# #         button_x = screen_width // 2 - self.x
# #         button_y = screen_height // 2 - self.y
# #         self.button.setLoc((button_x, button_y))

# #     def draw(self):
# #         self.button.draw()

# # # Example usage:
# # # Initialize Pygame and create a screen
# # pygame.init()
# # screen = pygame.display.set_mode((800, 600))

# # # Create an instance of CustomButton
# # start_button = CustomButton(screen, 100, 100, 'pygame/img/startb.png')

# # # Main loop
# # running = True
# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #     # Update button position if necessary
# #     start_button.update_position()

# #     # Draw the button
# #     screen.fill((255, 255, 255))  # Clear screen with white
# #     start_button.draw()
    
# #     pygame.display.flip()

# # pygame.quit()


# # import pygame
# # import pygwidgets

# # class CustomButton:
# #     def __init__(self, screen, x, y, image_path):
# #         self.screen = screen
# #         self.button = pygwidgets.CustomButton(screen, (x, y),
# #                                                image_path,
# #                                                down=image_path,
# #                                                over=image_path,
# #                                                disabled=image_path)
# #         self.x = x
# #         self.y = y

# #     def update_position(self):
# #         screen_width = pygame.display.Info().current_w 
# #         screen_height = pygame.display.Info().current_h 
# #         self.x = screen_width // 2 - self.button.getWidth() // 2
# #         self.y = screen_height // 2 - self.button.getHeight() // 2
# #         self.button.setLoc((self.x, self.y))

# #     def draw(self):
# #         self.button.draw()

# #     def handleEvent(self, event):
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             if event.button == 1:  # Left mouse button
# #                 mouse_pos = pygame.mouse.get_pos()
# #                 if self.button.getRect().collidepoint(mouse_pos):
# #                     return True  # Button was clicked
# #         return False  # Button was not clicked

# # # Example usage:
# # # Initialize Pygame and create a screen
# # pygame.init()
# # screen = pygame.display.set_mode((800, 600))

# # # Create an instance of CustomButton
# # start_button = CustomButton(screen, 100, 100, 'pygame/img/startb.png')

# # # Main loop
# # running = True
# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
        
# #         # Check if the button was clicked
# #         if start_button.handleEvent(event):
# #             print("Button clicked!")

# #     # Update button position if necessary
# #     start_button.update_position()

# #     # Draw the button
# #     screen.fill((255, 255, 255))  # Clear screen with white
# #     start_button.draw()
    
# #     pygame.display.flip()

# # pygame.quit()


# # import pygame_widgets
# # import pygame
# # from pygame_widgets.slider import Slider
# # from pygame_widgets.textbox import TextBox

# # pygame.init()
# # win = pygame.display.set_mode((1000, 600))

# # #slider = Slider(Surface x, y, w, h, )
# # slider = Slider(win, 100, 100, 800, 40, min=0, max=99, step=1)
# # output = TextBox(win, 475, 200, 50, 50, fontSize=30)

# # output.disable()  # Act as label instead of textbox

# # run = True
# # while run:
# #     events = pygame.event.get()
# #     for event in events:
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             run = False
# #             quit()

# #     win.fill((255, 255, 255))

# #     output.setText(slider.getValue())

# #     pygame_widgets.update(events)
# #     pygame.display.update()

# # import pygame
# # from pygame.locals import *

# # pygame.init()

# # # Screen dimensions
# # SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# # monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
# # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
# # mainClock = pygame.time.Clock()
# # fullscreen = False

# # # Dropdown settings
# # dropdown_active = False
# # dropdown_options = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]
# # selected_size = dropdown_options[0]

# # # Colors
# # WHITE = (255, 255, 255)
# # BLACK = (0, 0, 0)
# # BUTTON_COLOR = (100, 200, 100)
# # BUTTON_HOVER_COLOR = (50, 150, 50)

# # font = pygame.font.SysFont(None, 30)

# # def draw_dropdown():
# #     global dropdown_active
# #     # Draw the main dropdown button
# #     button_rect = pygame.Rect(50, 50, 200, 40)
# #     pygame.draw.rect(screen, BUTTON_COLOR if not dropdown_active else BUTTON_HOVER_COLOR, button_rect)
# #     button_text = font.render(f"Screen Size: {selected_size[0]}x{selected_size[1]}", True, WHITE)
# #     screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

# #     # Draw the dropdown options if active
# #     if dropdown_active:
# #         for i, (width, height) in enumerate(dropdown_options):
# #             option_rect = pygame.Rect(50, 50 + (i + 1) * 40, 200, 40)
# #             pygame.draw.rect(screen, BUTTON_COLOR, option_rect)
# #             option_text = font.render(f"{width}x{height}", True, WHITE)
# #             screen.blit(option_text, (option_rect.x + 10, option_rect.y + 10))

# # def main():
# #     global dropdown_active, selected_size
# #     running = True
# #     while running:
# #         for event in pygame.event.get():
# #             if event.type == QUIT:
# #                 running = False

# #             # Handle mouse events for dropdown
# #             if event.type == MOUSEBUTTONDOWN:
# #                 mouse_pos = event.pos
# #                 if button_rect.collidepoint(mouse_pos):
# #                     dropdown_active = not dropdown_active  # Toggle dropdown on button click

# #                 # Check if an option is selected
# #                 if dropdown_active:
# #                     for i, (width, height) in enumerate(dropdown_options):
# #                         option_rect = pygame.Rect(50, 50 + (i + 1) * 40, 200, 40)
# #                         if option_rect.collidepoint(mouse_pos):
# #                             selected_size = (width, height)
# #                             screen = pygame.display.set_mode(selected_size, pygame.RESIZABLE)
# #                             dropdown_active = False  # Close dropdown after selection

# #             # Close the dropdown if clicked outside
# #             if event.type == MOUSEBUTTONDOWN and dropdown_active:
# #                 dropdown_active = False

# #         screen.fill(BLACK)  # Clear screen
# #         draw_dropdown()  # Draw the dropdown menu
# #         pygame.display.flip()  # Update the display
# #         mainClock.tick(30)  # Control the frame rate

# #     pygame.quit()

# # if __name__ == "__main__":
# #     main()



# import pygame
# import sys
# from pygame.locals import *
# from setting import *
# from object import *
# import pygame_widgets
# from pygame_widgets.dropdown import Dropdown

# # Define available screen sizes
# screen_sizes = [
#     ("800x600", (800, 600)),
#     ("1024x768", (1024, 768)),
#     ("1280x720", (1280, 720)),
#     ("1920x1080", (1920, 1080))
# ]

# def options():
#     running = True
    
#     # Create a dropdown for screen sizes
#     dropdown = Dropdown(
#         screen,
#         50,  # x position
#         50,  # y position
#         200,  # width
#         30,  # height
#         options=[size[0] for size in screen_sizes],  # Display names
#         default='Choose Screen Size',  # Default text
#         fontSize=20,
#         borderColour=(255, 255, 255),
#         colour=(0, 0, 0),
#         hoverColour=(100, 100, 100),
#         textColour=(255, 255, 255),
#         inactiveColour=(50, 50, 50),
#         activeColour=(100, 100, 100)
#     )

#     while running:
#         screen.fill((0, 0, 0))

#         draw_text('Options', font, (255, 255, 255), screen, 20, 20)
#         scaled_uibg = pygame.transform.scale(uibg, (screen.get_width(), screen.get_height()))
#         screen.blit(scaled_uibg, (0, 0))  # Draw the scaled background
#         myDisplayText.setValue('Here is some new text to display')
#         myDisplayText.draw()

#         # Draw the dropdown
#         dropdown.draw()

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
            
#             # Check if an option is selected
#             selected_size = dropdown.getSelected()
#             if selected_size and selected_size != 'Choose Screen Size':
#                 # Change the screen size based on the selected option
#                 new_size = next(size[1] for size in screen_sizes if size[0] == selected_size)
#                 screen = pygame.display.set_mode(new_size)
        
#         pygame_widgets.update(pygame.event.get())
#         pygame.display.update()
#         mainClock.tick(60)
# options()


# import pygame
# import sys
# from pygame.locals import *
# from pygame_widgets import *
# from pygame_widgets.dropdown import Dropdown

# # Initialize Pygame
# pygame.init()

# # Define the initial screen size
# initial_size = (800, 600)
# screen = pygame.display.set_mode(initial_size)
# pygame.display.set_caption("Options Menu")

# # Define available screen sizes
# screen_sizes = [
#     ("800x600", (800, 600)),
#     ("1024x768", (1024, 768)),
#     ("1280x720", (1280, 720)),
#     ("1920x1080", (1920, 1080))
# ]

# def options(screen):
#     running = True
    
#     # Create a dropdown for screen sizes
#     dropdown = Dropdown(
#         screen,
#         50,  # x position
#         50,  # y position
#         200,  # width
#         30,  # height
#         name='Choose Screen Size',
#         # options=[size[0] for size in screen_sizes],  # Display names
#         choices= [
#                 ("800x600", (800, 600)),
#                 ("1024x768", (1024, 768)),
#                 ("1280x720", (1280, 720)),
#                 ("1920x1080", (1920, 1080))
#             ],
#         default='Choose Screen Size',  # Default text
#         fontSize=20,
#         borderColour=(255, 255, 255),
#         colour=(0, 0, 0),
#         hoverColour=(100, 100, 100),
#         textColour=(255, 255, 255),
#         inactiveColour=(50, 50, 50),
#         activeColour=(100, 100, 100)
#     )

#     while running:
#         screen.fill((0, 0, 0))

#         # Draw the dropdown
#         dropdown.draw()

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
            
#             # Check if an option is selected
#             selected_size = dropdown.getSelected()
#             if selected_size and selected_size != 'Choose Screen Size':
#                 # Change the screen size based on the selected option
#                 new_size = next(size[1] for size in screen_sizes if size[0] == selected_size)
#                 screen = pygame.display.set_mode(new_size)
        
#         # update(pygame.event.get())
#         pygame.display.update()
#         pygame.time.Clock().tick(60)

# # Call the options function
# options(screen)


# import pygame
# import sys
# from pygame.locals import *

# # Initialize Pygame
# pygame.init()

# # Define the initial screen size
# initial_size = (800, 600)
# screen = pygame.display.set_mode(initial_size)
# pygame.display.set_caption("Options Menu")

# # Define available screen sizes
# screen_sizes = [
#     ("800x600", (800, 600)),
#     ("1024x768", (1024, 768)),
#     ("1280x720", (1280, 720)),
#     ("1920x1080", (1920, 1080))
# ]

# # Function to draw text on the screen
# def draw_text(text, font, color, surface, x, y):
#     textobj = font.render(text, True, color)
#     textrect = textobj.get_rect()
#     textrect.topleft = (x, y)
#     surface.blit(textobj, textrect)

# def options():
#     running = True
#     font = pygame.font.Font(None, 36)
#     selected_index = -1  # No selection initially

#     while running:
#         screen.fill((0, 0, 0))
#         draw_text('Options', font, (255, 255, 255), screen, 20, 20)

#         # Draw the screen size options
#         for index, (size_text, _) in enumerate(screen_sizes):
#             color = (255, 255, 255) if index != selected_index else (0, 255, 0)  # Highlight selected option
#             draw_text(size_text, font, color, screen, 50, 60 + index * 40)  # Adjust y position for each option

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
#                 if event.key == K_DOWN:
#                     selected_index = (selected_index + 1) % len(screen_sizes)  # Move down in the list
#                 if event.key == K_UP:
#                     selected_index = (selected_index - 1) % len(screen_sizes)  # Move up in the list
#                 if event.key == K_RETURN and selected_index != -1:
#                     # Change the screen size based on the selected option
#                     new_size = screen_sizes[selected_index][1]
#                     screen = pygame.display.set_mode(new_size)
#                     pygame.display.set_caption(f"Options Menu - {screen_sizes[selected_index][0]}")

#         pygame.display.update()
#         pygame.time.Clock().tick(60)

# # Call the options function
# options(
# import pygame
# import pygame_gui


# pygame.init()

# pygame.display.set_caption('Quick Start')
# window_surface = pygame.display.set_mode((800, 600))

# background = pygame.Surface((800, 600))
# background.fill(pygame.Color('#000000'))

# manager = pygame_gui.UIManager((800, 600))

# hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                              text='Say Hello',
#                                              manager=manager)

# clock = pygame.time.Clock()
# is_running = True

# while is_running:
#     time_delta = clock.tick(60)/1000.0
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#              is_running = False

#         if event.type == pygame_gui.UI_BUTTON_PRESSED:
#               if event.ui_element == hello_button:
#                   print('Hello World!')

#         manager.process_events(event)

#     manager.update(time_delta)

#     window_surface.blit(background, (0, 0))
#     manager.draw_ui(window_surface)

#     pygame.display.update()


# import pygame_widgets
# import pygame
# from pygame_widgets.button import Button
# from pygame_widgets.dropdown import Dropdown
# x = 400
# y = 800
# pygame.init()
# win = pygame.display.set_mode((x, y))

# dropdown = Dropdown(
#     win, 120, 10, 100, 50, name='Select Color',
#     choices=[
#         "500x500",
#         'Blue',
#         'Yellow',
#     ],
#     borderRadius=3, colour=pygame.Color('green'), values=[1, 2, 'true'], direction='down', textHAlign='left'
# )


# def print_value():
#     print(dropdown.getSelected())


# button = Button(
#     win, 10, 10, 100, 50, text='Print Value', fontSize=30,
#     margin=20, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0),
#     radius=5, onClick=print_value, font=pygame.font.SysFont('calibri', 10),
#     textVAlign='bottom'
# )

# run = True
# while run:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             run = False
#             quit()

#     win.fill((255, 255, 255))

#     pygame_widgets.update(events)
#     pygame.display.update()


# import pygame
# import sys
# from pygame.locals import *
# from setting import *
# from object import *
# import pygame_widgets as pw
# from pygame_widgets.dropdown import Dropdown

# def options():
#     running = True
    
#     # Define screen sizes
#     screen_sizes = [
#         "800x600",
#         "1024x768",
#         "1280x720",
#         "1920x1080"
#     ]
    
#     # Create a dropdown for screen sizes
#     screen_size_dropdown = Dropdown(
#         window=screen,
#         options=screen_sizes,
#         fontSize=30,
#         position=(20, 60),
#         color=(255, 255, 255),
#         borderColor=(255, 255, 255),
#         textColor=(0, 0, 0),
#         selectedTextColor=(255, 0, 0),
#         rounded=5,
#         width=200,
#         dropDownHeight=200
#     )

#     while running:
#         screen.fill((0, 0, 0))

#         draw_text('Options', font, (255, 255, 255), screen, 20, 20)
#         scaled_uibg = pygame.transform.scale(uibg, (screen.get_width(), screen.get_height()))
#         screen.blit(scaled_uibg, (0, 0))  # Draw the scaled background

#         # Draw the dropdown
#         screen_size_dropdown.draw()

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
            
#             # Update widgets
#             pw.update(event)
        
#         pygame.display.update()
#         mainClock.tick(60)


# import pygame
# import pygame_menu

# pygame.init()
# surface = pygame.display.set_mode((600, 400))

# def set_difficulty(value, difficulty):
#     # Do the job here !
#     pass

# def start_the_game():
#     # Do the job here !
#     pass

# menu = pygame_menu.Menu('Welcome', 600, 400,
#                        theme=pygame_menu.themes.THEME_BLUE)

# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
# menu.add.button('Play', start_the_game)
# slider = menu.add.range_slider(title="test", default=50, range_values=(0, 100), increment=1, range_box_enabled=False)
# menu.mainloop(surface)


# import pygame
# import sys
# from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# class OptionsMenu:
#     def __init__(self, screen, font, uibg, mainClock):
#         self.screen = screen
#         self.font = font
#         self.uibg = uibg
#         self.mainClock = mainClock
#         self.running = True
#         self.myDisplayText = None  # You would need to initialize this properly based on your context

#     def draw_text(self, text, font, color, surface, x, y):
#         text_surface = font.render(text, True, color)
#         surface.blit(text_surface, (x, y))

#     def run(self):
#         while self.running:
#             self.screen.fill((0, 0, 0))

#             self.draw_text('options', self.font, (255, 255, 255), self.screen, 20, 20)
#             scaled_uibg = pygame.transform.scale(self.uibg, (self.screen.get_width(), self.screen.get_height()))
#             self.screen.blit(scaled_uibg, (0, 0))  # Draw the scaled background
            
#             if self.myDisplayText:  # Assuming myDisplayText is a class with setValue and draw methods
#                 self.myDisplayText.setValue('Here is some new text to display')
#                 self.myDisplayText.draw()

#             for event in pygame.event.get():
#                 if event.type == QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == KEYDOWN:
#                     if event.key == K_ESCAPE:
#                         self.running = False

#             pygame.display.update()
#             self.mainClock.tick(60)

# Usage example (assuming pygame is initialized and other necessary components are set up):
# options_menu = OptionsMenu(screen, font, uibg, mainClock)
# options_menu.run()

import pygame
UNSELECTED = "red"
SELECTED = "white"
BUTTONSTATES = {
    True:SELECTED,
    False:UNSELECTED
}

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size
        self.hovered = False
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- percentage

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

        # label
        # self.text = UI.fonts['m'].render(str(int(self.get_value())), True, "white", None)
        # self.label_rect = self.text.get_rect(center = (self.pos[0], self.slider_top_pos - 15))
        
    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos
    def hover(self):
        self.hovered = True
    def render(self, app):
        pygame.draw.rect(app.screen, "darkgray", self.container_rect)
        pygame.draw.rect(app.screen, BUTTONSTATES[self.hovered], self.button_rect)
    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val/val_range)*(self.max-self.min)+self.min
    def update_display_value(self):
        # Update the display text with the current value
        self.display_text.setText(f"Value: {int(self.get_value())}")
        
