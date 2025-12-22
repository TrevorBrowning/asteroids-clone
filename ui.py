import pygame

class UI:
    def __init__(self, screen, get_score):
        self.screen = screen
        self.get_score = get_score  
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        score_value = self.get_score()  
        text = self.font.render(f"Score: {score_value}", True, "white")
        self.screen.blit(text, (10, 10))
