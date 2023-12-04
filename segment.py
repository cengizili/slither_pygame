import pygame
import time
import math
import random

class Segment:
    def __init__(self, x, y, radius, skin, speed, angle):
        self.x = x
        self.y = y
        self.radius = radius
        self.skin = skin
        self.speed = speed
        self.angle = angle
    
    def move(self):
        self.x += math.cos(self.angle)*self.speed
        self.y += math.sin(self.angle)*self.speed
    
    def chase(self, other_segment):
        x1, y1 = self.x, self.y
        x2, y2 = other_segment.x, other_segment.y
        dx = x2 - x1
        dy = y2 - y1
        self.angle = math.atan2(dy, dx)
        
    def recede(self, other_segment):
        x1, y1 = self.x, self.y
        x2, y2 = other_segment.x, other_segment.y
        dx = x1 - x2
        dy = y1 - y2
        self.angle = math.atan2(dy, dx)
            
    def get(self):
        return Segment(self.x, self.y, self.radius, self.skin, self.speed, self.angle)
    
    def draw(self, screen):
        self.rect = pygame.draw.circle(screen, self.skin, (self.x, self.y), self.radius)


            
            

            



