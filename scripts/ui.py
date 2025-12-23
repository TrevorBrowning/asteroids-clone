import pygame

class UI:
    def __init__(self, screen, get_score, get_lives):
        self.screen = screen
        self.get_score = get_score  
        self.get_lives = get_lives
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        score_value = self.get_score()
        lives_value = self.get_lives()

        score_text = self.font.render(f"Score: {score_value}", True, "white")
        lives_text = self.font.render(f"Lives: {lives_value}", True, "white")

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 40))

