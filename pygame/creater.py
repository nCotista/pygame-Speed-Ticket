import pygame
import sys
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
        # button_x = screen_width // 2 - self.x
        # button_y = screen_height // 2 - self.y it too complicate to find the best equation na i will try another way then come back na 
        button_x = screen_width * self.x + 100
        button_y = screen_height * self.y + 87/2
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
