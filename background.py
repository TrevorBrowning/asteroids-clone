import pygame
import random

class Background:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        

        self.num_stars = random.randint(45, 90)
        self.stars_list = []
        self.star_color = [(255,255,255),(232,232,232),(195,190,200)]

        for _ in range(self.num_stars):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1,4)
            color = random.choice(self.star_color)
            self.stars_list.append((x, y, size, color))

    def draw(self):
        
        for x,y,size,color in self.stars_list:
            pygame.draw.circle(self.screen, color, (x,y), size)

