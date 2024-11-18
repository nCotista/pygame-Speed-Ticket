import pygame
import sys
from pygame.locals import *
from setting import *
from object import *
from game import *
from optionmenu import *
from pygame import mixer



# Initialize Pygame
pygame.init()
pygame.display.set_caption("My game") 



click = False
def main_menu():
    global screen
    global fullscreen
    mixer.music.load('pygame/sound/bgm.mp3')
    mixer.music.play(-1)

    while True:

        screen.fill((0,0,0))
        # draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        scaled_background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(scaled_background, (0, 0))  # Draw the scaled background
        
        start_button.draw()
        start_button.update_position()
        meun_button.draw()
        meun_button.update_position()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    slider.update_size_and_position()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                        slider.update_size_and_position()
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                        slider.update_size_and_position()

            if start_button.handleEvent(event):
                game()
            if meun_button.handleEvent(event):
                options()
            #if mixer.music.get_busy():
                # print("playing")
                #print(slider.get_value())
    
            
        pygame.display.update()
        mainClock.tick(60)

main_menu()
