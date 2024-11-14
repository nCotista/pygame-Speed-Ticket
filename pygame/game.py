import pygame
import sys
from setting import *
from object import *
from pygame.locals import * 
from players import *

pygame.init()
player = Player()

obsCount = 0
low_limit, high_limit = barrier_lowLimit, barrier_highLimit

# Main game loop
def game():
        running = True
        global screen
        global fullscreen
        global obsCount
        global low_limit
        global high_limit
        # Main game loop
        roadx = pygame.image.load('pygame/img/road.png').convert()
        road = pygame.transform.scale(roadx, (roadx.get_width(), roadx.get_height()))
        clock = pygame.time.Clock()
        car_x=0
        road_renderer = RoadRenderer(screen, road)
        while running:
            screen.fill(WHITE)
            # Calculate delta time for smooth movement
            delta = clock.tick() / 1000 + 0.00001
            road_speed =1000
            road_speed += player.speed*2 # ใช้ความเร็วของผู้เล่นเป็นตัวกำหนดความเร็วของถนน
            car_x += delta * road_speed  # เคลื่อนที่ถนนตามความเร็วของผู้เล่

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

            # screen.fill((100, 150, 250))
    
            # for i in range(800):
            #     scale = (800- i) /800
            #     x = car_x + i/scale
            #     road_slice = road.subsurface((0, x % 320,800, 1))  # Change to 800 width
            #     scaled_slice = pygame.transform.scale(road_slice, (800 * scale, 1))  # Scale to fit width of screen
        
    
            #     screen.blit(scaled_slice, (400 - 400 * scale, 600 - i))  # Center the road on the screen
            delta = clock.tick() / 1000.0
            road_speed = 1000 + player.speed * 2  # Use player's speed to determine road speed
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

        # Quit Pygame
        