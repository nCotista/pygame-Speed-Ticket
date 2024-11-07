import pygame
import sys
from pygame.locals import *
from setting import *

class  button:
    def __init__(self,text):
        self.text = text
    
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

