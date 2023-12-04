from segment import Segment
import math
import random


class Body(Segment):

    def __init__(self, x, y, radius, skin, speed, angle, distance, length):
        super().__init__(x, y, radius, skin, speed, angle)
        self.head = self.get()
        self.circles = [self.head]
        self.length = length
        self.distance = distance
        self.angle_list = [0]*2000
        self.init_circles()
        self.alive = True

    def init_circles(self):
        random_angle = random.uniform(math.pi/2, math.pi)*random.choice([1,-1])
        for i in range(self.length):
            self.angle_list[i] = random_angle*(self.length-i)/self.length
        for _ in range(self.length-1):
            self.circles.append(self.get())
        self.head = self.circles[0]
    
    def update_angles(self):
        for idx, circle in enumerate(self.circles):
            circle.angle = self.angle_list[idx]
    
    def update_circles(self):
        for circle, next_circle in zip(self.circles, self.circles[1:]):
            next_circle.x = circle.x - math.cos(next_circle.angle)*self.distance
            next_circle.y = circle.y - math.sin(next_circle.angle)*self.distance
            
    def draw(self, screen):
        if self.alive:
            if self.skin == "camouflage":
                skins = [(82, 86, 90), (87, 95, 94), (34, 49, 34), (53, 72, 35), (193, 154, 107)]
                for idx, circle in enumerate(self.circles):
                    while idx >= len(skins):
                        idx = idx - len(skins)
                    circle.skin = skins[idx]
                    circle.draw(screen)
            elif self.skin == "rainbow":
                skins = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0),  (0, 0, 255), (75, 0, 130), (238, 130, 238)]
                for idx, circle in enumerate(self.circles):
                    while idx >= len(skins):
                        idx = idx - len(skins)
                    circle.skin = skins[idx]
                    circle.draw(screen)
            elif self.skin == "arctic":
                skins = [(187, 224, 227), (144, 190, 205), (230, 245, 255), (192, 202, 211), (167, 180, 196), (118, 151, 178), (69, 105, 144), (43, 64, 92)]
                for idx, circle in enumerate(self.circles):
                    while idx >= len(skins):
                        idx = idx - len(skins)
                    circle.skin = skins[idx]
                    circle.draw(screen)


    def move(self):
        self.head.move()
        self.update_circles()
        self.update_angles()
                