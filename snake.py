from segment import Segment
from body import Body
import math
import pygame
import random


class Snake(Body):
    def __init__(self, x, y, radius, skin, speed, angle, distance, length, nickname):
        super().__init__(x, y, radius, skin, speed, angle, distance, length)
        self.nickname = nickname
        self.head = self.circles[0]
        self.lock = True
    
    def update_angle_list(self, to_add):
        self.angle_list.insert(0, to_add)
        self.angle_list.pop()
    
    def update_bot_path(self, spells):
        center_diffs = [math.sqrt((spell.x - self.head.x)**2 + (spell.y - self.head.y)**2) for spell in spells if spell.isAppear]
        self.spell = spells[center_diffs.index(min(center_diffs))]
        if self.alive:
            if self.lock:
                self.chase()
                self.lock = False
            else: 
                self.update_angle_list(self.angle_list[0])
        
    def chase(self):
        x1, y1 = self.head.x, self.head.y
        x2, y2 = self.spell.x, self.spell.y
        dx = x2 - x1
        dy = y2 - y1
        self.update_angle_list(math.atan2(dy, dx))
        
    def recede(self):
        x1, y1 = self.head.x, self.head.y
        x2, y2 = self.other_snake.head.x, self.other_snake.head.y
        dx = x1 - x2
        dy = y1 - y2
        self.update_angle_list(math.atan2(dy, dx))

    def check_collide(self, other_snake):
        if self.alive:
            for circle in other_snake.circles:
                if other_snake != self:
                    if self.head.rect.colliderect(circle.rect) and other_snake.alive:
                        return True
        return False

    def dissolve(self):
        self.alive = False
        self.nextActivationTime = pygame.time.get_ticks() + 10000
