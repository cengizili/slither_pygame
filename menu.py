import pygame
from button import Button

class Menu(Button):
    def __init__(self, x, y, width, height, font, screen, text, color, button_texts, button_spacing):
        super().__init__(x, y, width, height, font, screen, text, color)
        self.buttons = []
        total_buttons_height = self.height * len(button_texts) + button_spacing * (len(button_texts) - 1)
        start_y = (screen.get_height() - total_buttons_height) // 2
        self.selected = None

        for i, text in enumerate(button_texts):
            self.x = (screen.get_width() - width) // 2
            self.y = start_y + i * (height + button_spacing)
            self.text = text
            self.buttons.append(self.get())

    def draw(self):
        for button in self.buttons:
            if self.buttons.index(button) == 0:
                button.color = pygame.Color('white')
                button.clicked = None
            elif button.text == self.selected:
                button.color = pygame.Color('blue')
            else:
                button.color = self.color
            button.draw()