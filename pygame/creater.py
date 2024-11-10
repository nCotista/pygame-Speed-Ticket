import pygame
from pygame.locals import *
from setting import *
import pygwidgets



class CustomButton:
    def __init__(self, screen, x, y, image_path):
        self.screen = screen
        self.button = pygwidgets.CustomButton(screen, (x, y),
                                               image_path,
                                               down=image_path,
                                               over=image_path,
                                               disabled=image_path)
        self.x = x
        self.y = y

    def update_position(self):
        screen_width = pygame.display.Info().current_w 
        screen_height = pygame.display.Info().current_h 
        button_x = screen_width // 2 - self.x
        button_y = screen_height // 2 - self.y #it too complicate to find the best equation na i will try another way then come back na 
        # button_x = screen_width * self.x 
        # button_y = screen_height * self.y 
        self.button.setLoc((button_x, button_y))

    def draw(self):
        self.button.draw()
    
    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if self.button.getRect().collidepoint(mouse_pos):
                    return True  # Button was clicked
        return False  # Button was not clicked



class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size
        self.hovered = False
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val  # <- percentage

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

        # Initialize DisplayText for displaying the value
        self.display_text = pygwidgets.DisplayText(screen, (self.pos[0], self.slider_top_pos - 20), textColor=(255, 255, 255))
        self.update_display_value()

    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos
        self.update_display_value()

    def hover(self):
        self.hovered = True

    def render(self):
        pygame.draw.rect(screen, "darkgray", self.container_rect)
        pygame.draw.rect(screen, "white" if self.hovered else "red", self.button_rect)
        self.display_text.draw()  # Draw the display text

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos
        return (button_val / val_range) * (self.max - self.min) + self.min

    def update_display_value(self):
        # Update the display text with the current value
        value = int(self.get_value())
        self.display_text.setText(f"Volume: {value}")
        
        # Set the mixer volume based on the slider value (normalize to 0.0 - 1.0)
        pygame.mixer.music.set_volume(value / 100.0)
