# import pygame
# from pygame.locals import *
# from setting import *
# import pygwidgets



# class CustomButton:
#     def __init__(self, screen, x, y, image_path):
#         self.screen = screen
#         self.button = pygwidgets.CustomButton(screen, (x, y),
#                                                image_path,
#                                                down=image_path,
#                                                over=image_path,
#                                                disabled=image_path)
#         self.x = x
#         self.y = y

#     def update_position(self):
#         screen_width = pygame.display.Info().current_w 
#         screen_height = pygame.display.Info().current_h 
#         button_x = screen_width // 2 - self.x
#         button_y = screen_height // 2 - self.y #it too complicate to find the best equation na i will try another way then come back na 
#         # button_x = screen_width * self.x 
#         # button_y = screen_height * self.y 
#         self.button.setLoc((button_x, button_y))

#     def draw(self):
#         self.button.draw()
    
#     def handleEvent(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:  # Left mouse button
#                 mouse_pos = pygame.mouse.get_pos()
#                 if self.button.getRect().collidepoint(mouse_pos):
#                     return True  # Button was clicked
#         return False  # Button was not clicked



# class Slider:
#     def __init__(self, screen: pygame.Surface, initial_val: float, min: int, max: int) -> None:
#         self.screen = screen
#         self.min = min
#         self.max = max
#         self.initial_val = initial_val

#         self.hovered = False
#         self.grabbed = False

#         # Dynamic sizing based on screen width
#         self.update_size_and_position()

#     def update_size_and_position(self):
#         # Dynamic slider width (80% of screen width)
#         screen_width = self.screen.get_width()
#         screen_height = self.screen.get_height()
        
#         # Scale slider width and height based on screen size
#         self.size = (int(screen_width * 0.8), int(screen_height * 0.04))
        
#         # Center the slider
#         self.pos = (screen_width // 2, screen_height // 2)
        
#         # Calculate slider boundaries
#         self.slider_left_pos = self.pos[0] - (self.size[0] // 2)
#         self.slider_right_pos = self.pos[0] + (self.size[0] // 2)
#         self.slider_top_pos = self.pos[1] - (self.size[1] // 2)

#         # Create container and button rects with dynamic sizing
#         self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        
#         # Calculate button width proportional to slider width
#         button_width = max(10, int(self.size[0] * 0.05))
        
#         # Position the button based on initial value
#         button_x = (self.slider_left_pos + 
#                     (self.size[0] * self.initial_val) - 
#                     (button_width // 2))
        
#         self.button_rect = pygame.Rect(button_x, 
#                                         self.slider_top_pos, 
#                                         button_width, 
#                                         self.size[1])

#         # Update display text position
#         self.display_text = pygwidgets.DisplayText(
#             self.screen, 
#             (self.pos[0], self.slider_top_pos - int(screen_height * 0.05)), 
#             textColor=(255, 255, 255),
#             fontSize=int(screen_height * 0.03)  # Dynamic font size
#         )
        
#         # Update the display value
#         self.update_display_value()

#     def move_slider(self, mouse_pos):
#         pos = mouse_pos[0]
#         if pos < self.slider_left_pos:
#             pos = self.slider_left_pos
#         if pos > self.slider_right_pos:
#             pos = self.slider_right_pos
#         self.button_rect.centerx = pos
#         self.update_display_value()

#     def hover(self):
#         self.hovered = True

#     def render(self):
#         # Dynamic colors and rendering based on screen size
#         container_color = (100, 100, 100)  # Dark gray
#         button_color = (255, 255, 255) if self.hovered else (200, 0, 0)
        
#         pygame.draw.rect(self.screen, container_color, self.container_rect)
#         pygame.draw.rect(self.screen, button_color, self.button_rect)
#         self.display_text.draw()

#     def get_value(self):
#         val_range = self.slider_right_pos - self.slider_left_pos
#         button_val = self.button_rect.centerx - self.slider_left_pos
#         return (button_val / val_range) * (self.max - self.min) + self.min

#     def update_display_value(self):
#         # Update the display text with the current value
#         value = int(self.get_value())
#         self.display_text.setText(f"Volume: {value}")
        
#         # Set the mixer volume based on the slider value (normalize to 0.0 - 1.0)
#         pygame.mixer.music.set_volume(value / 100.0)

