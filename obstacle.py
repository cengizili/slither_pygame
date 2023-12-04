import pygame
from snake import Snake

from static import Static

class Obstacle(Static):
    def __init__(self, x, y, width, height, skin):
        super().__init__(x, y, width, height, skin)
    
    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, self.skin, (self.x, self.y, self.width, self.height))
    
    def collision(self, snake:Snake):
        if self.rect.colliderect(snake.rect):
            snake.dissolve()