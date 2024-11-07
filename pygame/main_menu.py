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
    # musicSound.play()
    mixer.music.load('pygame/sound/bgm.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    while True:

        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        scaled_background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(scaled_background, (0, 0))  # Draw the scaled background
        # startButton.draw()
        # update_button_position()
        start_button.draw()
        start_button.update_position()
        meun_button.draw()
        meun_button.update_position()


        # mx, my = pygame.mouse.get_pos()
 
        # button_1 = pygame.Rect(50, 100, 200, 50)
        # button_2 = pygame.Rect(50, 200, 200, 50)
        # if button_1.collidepoint((mx, my)):
        #     if click:
        #         game()
        # if button_2.collidepoint((mx, my)):
        #     if click:
        #         options()
        # pygame.draw.rect(screen, (255, 0, 0), button_1)
        # pygame.draw.rect(screen, (255, 0, 0), button_2)
       
 
        # click = False
        
        # musicSound.set_volume(1)
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
            # if event.type == MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         click = True
            if start_button.handleEvent(event):
                game()
            if meun_button.handleEvent(event):
                options()
            if mixer.music.get_busy():
                print("playing")
    
            
        pygame.display.update()
        mainClock.tick(60)

main_menu()
