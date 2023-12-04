import pygame

class ScoreBoard:
    def __init__(self, snake):
        self.score = snake.length
        self.snake = snake
        self.font = pygame.font.SysFont(None, 36)
        self.text = self.font.render("Score: {}".format(self.score), True, (0, 255, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (100, 50)
    
    def draw(self, surface):
        self.text = self.font.render("Score: {}".format(len(self.snake.circles)), True, (0, 255, 0))
        surface.blit(self.text, self.textRect)