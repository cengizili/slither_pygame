import pygame

class Button():
    def __init__(self, x, y, width, height, font, screen, text, color):
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False
        self.text = text
        self.screen = screen
    
    def draw_text_rect(self, text, rect, font,):
        surface = pygame.Surface(rect.size)
        surface.fill(self.color)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(rect.width // 2, rect.height // 2))
        surface.blit(text_surface, text_rect)
        self.screen.blit(surface, rect)
    
    def get(self):
       return Button(self.x, self.y, self.width, self.height, self.font, self.screen, self.text, self.color) 

    def draw(self):
        pygame.event.get()
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.selected = self.text
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_rect = pygame.Rect(self.rect.x + 10, self.rect.y + 10, self.rect.width - 20, self.rect.height - 20)
        self.draw_text_rect(self.text, text_rect, self.font)

