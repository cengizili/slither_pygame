import pygame

class Skin:
    def __init__(self, pattern):
        self.pattern = pygame.image.load(pattern)
    
    def getPattern(self):
        return self.pattern

