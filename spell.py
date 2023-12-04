import pygame
import random

from static import Static

class Spell(Static):
    def __init__(self, x, y, width, height, skin, duration, isPermenant):
        super().__init__(x, y, width, height, skin)
        self.duration = duration
        self.skin = skin
        self.x = x
        self.y = y
        self.isPermenant = isPermenant
        self.isAppear = True
        self.nextActivationTime = 0
        self.snake = None
        self.rect = None
    
    def disappear(self):
        self.nextActivationTime = pygame.time.get_ticks() + self.duration*1000
        if self.isAppear:
            self.activate()
        self.isAppear = False
        
    
    def activate(self):
        pass

    def deactivate(self):
        pass
    
    def draw(self, screen):
        if pygame.time.get_ticks() >= self.nextActivationTime:
            self.deactivate()
            if self.isPermenant:
                self.isAppear = True
            if self.isAppear:
                self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height) 
                scaled_image = pygame.transform.scale(self.skin, (self.width, self.height))
                screen.blit(scaled_image, self.rect)
   
class SpeedChanger(Spell):
    def __init__(self, x, y, width, height, skin, duration, isPermenant, speed_change):
        super().__init__(x, y, width, height, skin, duration, isPermenant)
        self.speed_change = speed_change
    
    def activate(self):
        self.snake.head.speed += self.speed_change
    
    def deactivate(self):
        if self.snake:
            self.snake.head.speed -= self.speed_change
            self.snake = None

class LengthChanger(Spell):
    def __init__(self, x, y, width, height, skin, duration, isPermenant):
        super().__init__(x, y, width, height, skin, duration, isPermenant)
    
    def activate(self):
        self.snake.circles.append(self.snake.get())
    
    