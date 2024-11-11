from setting import *
import pygame
from object import *

class Player:
    def __init__(self):
        self.width = player_width
        self.height = player_height
        self.lane = player_lane
        self.x = get_lane_x_position(self.lane, player_y) - self.width // 2
        self.y = player_y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 0

        #เปลียน player เป็น car
        self.image = pygame.image.load('car-removebg-preview.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Initial size

        # Speed display
        self.font = pygame.font.Font(None, 72)
        self.text = self.font.render(str(self.speed), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y - 50))

    def Player_controller(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.lane > 0:
            self.lane -= 1
        if keys[pygame.K_RIGHT] and self.lane < 1:
            self.lane += 1
        # TODO: Add a delay to the movement

        # Update player position
        self.x = get_lane_x_position(self.lane, player_y) - self.width // 2
        player_scale = 1 + (self.y / SCREEN_HEIGHT)  # Scale the player based on Y position
        scaled_player_width = int(self.width * player_scale)
        scaled_player_height = int(self.height * player_scale)
        self.rect = pygame.Rect(self.x, self.y, scaled_player_width, scaled_player_height)

        # Update scaled image for depth effect
        scaled_image = pygame.transform.scale(self.image, (scaled_player_width, scaled_player_height))

        # Draw player image
        screen.blit(scaled_image, (self.x, self.y))

        # Update and draw speed text
        self.text = self.font.render(str(self.speed), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x + 25, self.y - 50))
        screen.blit(self.text, self.text_rect)

    def get_rect(self):
        return self.rect

    def acceleration(self, increasing):
        self.speed += increasing