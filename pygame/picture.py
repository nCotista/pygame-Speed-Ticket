import pygame
import pygwidgets

# Initialize Pygame
pygame.init()

# Load the original image
original_image = pygame.image.load('pygame/img/startb.png')

# Resize the image
new_size = (200, 100)  # Replace width and height with the desired dimensions
resized_image = pygame.transform.scale(original_image, new_size)

# custom bt require path so it not work 