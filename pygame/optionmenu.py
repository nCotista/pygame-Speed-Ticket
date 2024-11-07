import pygame
import sys
from pygame.locals import *
from setting import *
from object import *

def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        scaled_uibg = pygame.transform.scale(uibg, (screen.get_width(), screen.get_height()))
        screen.blit(scaled_uibg, (0, 0))  # Draw the scaled background
        myDisplayText.setValue('Here is some new text to display')
        myDisplayText.draw()
       
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 