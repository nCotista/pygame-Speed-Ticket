import pygame
import sys
from pygame.locals import *
from setting import *
from object import *
# import pygame_widgets


def options():
    running = True
    while running:
        screen.fill((0,0,0))

        # draw_text('options', font, (255, 255, 255), screen, 20, 20)
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        if slider.button_rect.collidepoint(event.pos):
                            slider.grabbed = True
                
                # Check for mouse button up to release the slider
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    slider.grabbed = False

        # Move the slider if it is being grabbed
        if slider.grabbed:
            mouse_pos = pygame.mouse.get_pos()
            slider.move_slider(mouse_pos)
        # pygame_widgets.update(pygame.event.get())
        slider.render()
        pygame.display.update()
        mainClock.tick(60)
 