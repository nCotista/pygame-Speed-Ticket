import pygame
import sys
# pygame setup
pygame.init()
pygame.display.set_caption("My game") 

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height)) #ขนาดจอ
clock = pygame.time.Clock()
running = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (50, 150, 50)

#set blackground be 1 object
background = pygame.Surface(screen.get_size())
background = background.convert() 
background.fill((233, 62, 255)) # set bg color 


# bgimg = pygame.image.load("pygame\img\testimg.jpg") #load img
# bgimgpos = bgimg.get_rect() 
# bgimgpos.center = background.get_rect().center

#set font
font = pygame.font.Font(None, 36)
text = font.render("Hello There", 1, (10, 10, 10))

#textposition 
textpos = text.get_rect() 
textpos.centerx = background.get_rect().centerx 

# background.blit(text, textpos)  #blit = ขึ้นจอ

screen.blit(background, (0, 0))
pygame.display.flip()


def draw_text(text, font, color, screen, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    screen.blit(text_obj, text_rect)
    

def game_loop():
    screen.fill(WHITE)
    draw_text("Game Screen", font, BLACK, screen, screen_width//2, screen_height//2)
    pygame.display.flip()
    pygame.time.wait(2000)  # Placeholder for actual game logic


#main
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     #ออกเมื่อกดปิด
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    game_loop()  # Start the game
                    

    
    
    # Start Button
    mouse_pos = pygame.mouse.get_pos()
    start_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)

        # Check if mouse is hovering the button
    if start_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, start_button)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, start_button)


    draw_text('Start Game', font, WHITE, screen, screen_width // 2, screen_height // 2 + 25)
    pygame.display.update()


pygame.quit()