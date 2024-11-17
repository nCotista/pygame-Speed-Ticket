import pygame
import sys
from setting import *
from object import *
from pygame.locals import * 
from players import *
from optionmenu import *
pygame.init()
player = Player()

def Gameover():
    global screen
    global fullscreen
    running = True
    scaled_died = pygame.transform.scale(died1, (screen.get_width(), screen.get_height()))
    screen.blit(scaled_died, (0, 0))  # Draw the scaled background
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Handle mouse clicks on buttons
            if start_button.handleEvent(event):
                game()
            if meun_button.handleEvent(event):
                options()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            
            if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_f:
                        fullscreen = not fullscreen
                        if fullscreen:
                            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
            if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_f:
                        fullscreen = not fullscreen
                        if fullscreen:
                            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
        
        # Drawing
        
        start_button.draw()
        start_button.update_position()
        meun_button.draw()
        meun_button.update_position()
        
        pygame.display.update()
        clock.tick(60)
        

# Main game loop
def game():
        running = True
        global screen
        global fullscreen
        global obsCount
        global low_limit
        global high_limit
        global car_x
        # Main game loop
        
        while running:
            screen.fill((66, 182, 245))
            # Calculate delta time for smooth movement
            delta = mainClock.tick() / 1000 + 0.00001
            road_speed =0
            road_speed += player.speed*2 # ใช้ความเร็วของผู้เล่นเป็นตัวกำหนดความเร็วของถนน
            car_x += delta * road_speed  # เคลื่อนที่ถนนตามความเร็วของผู้เล่
            turn_sound.set_volume(slider.get_value())

            # Event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == VIDEORESIZE:
                    if not fullscreen:
                        screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                        road_renderer.screen = screen
                    
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_f:
                        fullscreen = not fullscreen
                        if fullscreen:
                            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)

            
            delta = clock.tick() / 1000 + 0.00001
            road_speed =  player.speed * 2  # Use player's speed to determine road speed
            car_x += delta * road_speed  # Move the road based on player's speed
            road_renderer.render(car_x)
            

            player.Player_controller()
            
            # Add obstacles
            if len(obstacles) < 2:
                if obsCount > 5:
                    create_barrier(low_limit, high_limit)
                    high_limit += barrier_addConstant
                    low_limit += barrier_addConstant
                    obsCount = 0
                else:
                    create_obstacle()
                    obsCount += 1

            for obs in obstacles:
                obs.obstacle_move()
                if obs.get_rect().colliderect(player):
                    if type(obs) == Obstacle:
                        player.acceleration(obs.speedChanger)
                        #print(f'{obs.speedChanger} , {player.speed}')
                    elif type(obs) == MuDi_Obstacle:
                        player.speed = obs.get_total(player.speed)
                    elif type(obs) == Barrier:
                        if player.speed < obs.speedLimit:
                            print('Game Over')
                            obs.speedLimit = player.speed 
                            Gameover()
                            running = False
                        else:
                            player.acceleration(-1*obs.speedLimit)

                    obstacles.remove(obs)
                    continue
                if obs.y > SCREEN_HEIGHT:
                    obstacles.remove(obs)

            # Update the display
            pygame.display.update()

            # Frame rate
            fr = 60 + player.speed/player_speed_ratio
            pygame.time.Clock().tick(fr)

        
    