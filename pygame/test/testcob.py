import pygame, sys
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()



# import pygame
# import pygwidgets

# # Initialize Pygame
# pygame.init()

# # Set up the screen dimensions
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Slider Example")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Slider class definition (as provided previously)
# class Slider:
#     def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
#         self.pos = pos
#         self.size = size
#         self.hovered = False
#         self.grabbed = False

#         self.slider_left_pos = self.pos[0] - (size[0] // 2)
#         self.slider_right_pos = self.pos[0] + (size[0] // 2)
#         self.slider_top_pos = self.pos[1] - (size[1] // 2)

#         self.min = min
#         self.max = max
#         self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val  # <- percentage

#         self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
#         self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

#         # Initialize DisplayText for displaying the value
#         self.display_text = pygwidgets.DisplayText(screen, (self.pos[0], self.slider_top_pos - 20), textColor=(255, 255, 255))
#         self.update_display_value()

#     def move_slider(self, mouse_pos):
#         pos = mouse_pos[0]
#         if pos < self.slider_left_pos:
#             pos = self.slider_left_pos
#         if pos > self.slider_right_pos:
#             pos = self.slider_right_pos
#         self.button_rect.centerx = pos
#         self.update_display_value()

#     def hover(self):
#         self.hovered = True

#     def render(self):
#         pygame.draw.rect(screen, "darkgray", self.container_rect)
#         pygame.draw.rect(screen, "white" if self.hovered else "red", self.button_rect)
#         self.display_text.draw()  # Draw the display text

#     def get_value(self):
#         val_range = self.slider_right_pos - self.slider_left_pos - 1
#         button_val = self.button_rect.centerx - self.slider_left_pos
#         return (button_val / val_range) * (self.max - self.min) + self.min

#     def update_display_value(self):
#         # Update the display text with the current value
#         self.display_text.setText(f"Value: {int(self.get_value())}")

# # Main loop
# def main():
#     clock = pygame.time.Clock()
#     running = True

#     # Create a slider instance
#     slider = Slider(pos=(screen_width // 2, screen_height // 2), size=(300, 20), initial_val=0.5, min=0, max=100)

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
            
#             # Check for mouse button down to grab the slider
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:  # Left mouse button
#                     if slider.button_rect.collidepoint(event.pos):
#                         slider.grabbed = True
            
#             # Check for mouse button up to release the slider
#             if event.type == pygame.MOUSEBUTTONUP:
#                 if event.button == 1:  # Left mouse button
#                     slider.grabbed = False

#         # Move the slider if it is being grabbed
#         if slider.grabbed:
#             mouse_pos = pygame.mouse.get_pos()
#             slider.move_slider(mouse_pos)

#         # Render everything
#         screen.fill(BLACK)
#         slider.render()
#         pygame.display.flip()

#         # Limit the frame rate
#         clock.tick(60)

#     pygame.quit()

# # Run the main function
# if __name__ == "__main__":
#     main()



import pygame
import pygwidgets

UNSELECTED = "red"
SELECTED = "white"
BUTTONSTATES = {
    True: SELECTED,
    False: UNSELECTED
}

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size
        self.hovered = False
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val  # <- percentage

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

        # Initialize DisplayText for displaying the value
        self.display_text = pygwidgets.DisplayText(screen, (self.pos[0], self.slider_top_pos - 20), textColor=(255, 255, 255))
        self.update_display_value()

    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos
        self.update_display_value()

    def hover(self):
        self.hovered = True

    def render(self):
        pygame.draw.rect(screen, "darkgray", self.container_rect)
        pygame.draw.rect(screen, BUTTONSTATES[self.hovered], self.button_rect)
        self.display_text.draw()  # Draw the display text

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos
        return (button_val / val_range) * (self.max - self.min) + self.min

    def update_display_value(self):
        # Update the display text with the current value
        value = int(self.get_value())
        self.display_text.setText(f"Volume: {value}")
        
        # Set the mixer volume based on the slider value (normalize to 0.0 - 1.0)
        pygame.mixer.music.set_volume(value / 100.0)

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('pygame/sound/bgm.mp3')  # Load your music file here
    pygame.mixer.music.play(-1)  # Play the music in a loop

    clock = pygame.time.Clock()
    running = True

    # Create a slider instance
    slider = Slider(pos=(screen_width // 2, screen_height // 2), size=(300, 20), initial_val=0.5, min=0, max=100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Check for mouse button down to grab the slider
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

        # Render everything
        screen.fill(BLACK)
        slider.render()
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()