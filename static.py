import pygame

class Static:
    def __init__(self, x, y, width, height, skin):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.skin = skin
    
    def update(self):
        # update the object's state
        pass
    
    def draw(self, surface):
        # draw the object on the surface using the skin
        pygame.draw.rect(surface, self.skin, (self.x, self.y, self.width, self.height))
