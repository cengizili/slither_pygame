import pygame
from score_board import ScoreBoard
from obstacle import Obstacle
from static import Static
from snake import Snake
from spell import Spell, SpeedChanger, LengthChanger
import math
import random
from menu import Menu

pygame.init()

class Game:
    def __init__(self):
        self.game_state = "start"
        self.width = 800 # screen width
        self.height = 600 # screen height
        self.gameScreen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images/space.jpg")
        self.corner_rects = [pygame.Rect(0,0,100,100), pygame.Rect(0,self.height-100,100,100), pygame.Rect(self.width-100,0,100,100), pygame.Rect(self.width-100,self.height-100,100,100),]
        self.spawn_period = 3000   
        self.timer = 0 
        self.counter = 1
        self.initialize_objects()   
         
    def initialize_objects(self):
        self.players : list[Snake] = []
        self.spells : list[Spell] = []
        self.obstacles : list[Obstacle] = []
        x = random.randint(50, self.width-50)
        y = random.randint(50, self.height-50)
        self.user = Snake(skin="camouflage", length=50, angle=0, speed=2, nickname="Cengiz", distance=5, x=x, y=y, radius=20)
        self.score_board = ScoreBoard(self.user)
        self.players.append(self.user)
        self.red_spell = pygame.image.load("images/red_spell.png").convert_alpha()
        self.blue_spell = pygame.image.load("images/blue_spell.png").convert_alpha()
        for _ in range(5):
            self.spawn_bot()
        for i in range(80):
            x = random.randint(50, self.width-50)
            y = random.randint(50, self.height-50)
            self.spells.append(LengthChanger(x=x, y=y, duration=2, width=20, height=20, skin=self.blue_spell, isPermenant=True))
        for i in range(2):
            x = random.randint(50, self.width-50)
            y = random.randint(50, self.height-50)
            self.obstacles.append(Obstacle(x=x, y=y, width=20, height=100, skin=pygame.Color('red')))
        font = pygame.font.SysFont("arialblack", 30)
        self.pause_menu = Menu(x=50, y=50, button_spacing=50, font=font, screen=self.gameScreen, height=60, width=600, color=pygame.Color('orange'), button_texts=["GAME PAUSED","Resume", "Quit"], text="")
        self.game_over_menu = Menu(x=50, y=50, button_spacing=50, font=font, screen=self.gameScreen, height=60, width=600, color=pygame.Color('orange'), button_texts=["GAME OVER", "Restart", "Quit"], text="")
        self.start_menu = Menu(x=50, y=50, button_spacing=50, font=font, screen=self.gameScreen, height=60, width=600, color=pygame.Color('orange'), button_texts=["SLITHER", "Select Background", "Select Skin", "Start"], text="")
        self.select_background = Menu(x=50, y=50, button_spacing=50, font=font, screen=self.gameScreen, height=60, width=600, color=pygame.Color('orange'), button_texts=["SELECT BACKGROUND", "Rainbow", "Space", "Lake", "Back"], text="")
        self.select_skin = Menu(x=50, y=50, button_spacing=50, font=font, screen=self.gameScreen, height=60, width=600, color=pygame.Color('orange'), button_texts=["SELECT SKIN", "Arctic", "Rainbow", "Camouflage", "Back"], text="")

    def update_spells(self):
        for player in self.players:
            for spell in self.spells:
                if player.alive and spell.isAppear and spell.rect:
                    if player.head.rect.colliderect(spell.rect): 
                        spell.snake = player
                        player.lock = True
                        spell.disappear()

        
    def spawn_bot(self):
        p1 = (random.randint(0, self.width), 0)
        p2 = (random.randint(0, self.width), self.height)
        p3 = (0, random.randint(0, self.height))
        p4 = (self.width, random.randint(0, self.height))
        pt = random.choice([p1, p2, p3, p4]) 
        new_bot = Snake(skin="arctic", length=50, angle=0, speed=2, nickname="bot", distance=5, x=pt[0], y=pt[1], radius=20)
        self.timer = pygame.time.get_ticks()       
        self.players.append(new_bot)
    
    def update_obstacles(self):
        for player in self.players:
            for obstacle in self.obstacles:
                if player.head.rect.colliderect(obstacle.rect): 
                    if player.alive:
                        player.dissolve()
                        newSpells = [SpeedChanger(x=circle.x, y=circle.y, duration=3, speed_change=2/50, width=20, height=20, skin=self.red_spell, isPermenant=False) for circle in player.circles]
                        self.spells.extend(newSpells)
                        if player == self.user:
                            self.game_state = "game_over"
    
    def update_players(self):
        for player1 in self.players:
            for player2 in self.players:
                if player1.check_collide(player2):
                    if player1 == self.user:
                        self.game_state = "game_over"
                    else:
                        player1.dissolve()
                        newSpells = [SpeedChanger(x=circle.x, y=circle.y, duration=3, speed_change=2/50, width=20, height=20, skin=self.red_spell, isPermenant=False) for circle in player1.circles]
                        self.spells.extend(newSpells)

        
    def run(self):
        while True:
            self.gameScreen.fill((255,255,255))                    
            if self.game_state == "pause":
                self.pause_menu.draw()
                for button in self.pause_menu.buttons:
                    if button.clicked:
                        if button.text == "Resume":
                            self.game_state = "game"
                        elif button.text == "Quit":
                            self.game_state = "start"
                            self.initialize_objects()
                        button.clicked = False
                        self.pause_menu.selected = button.text
            elif self.game_state == "game_over":
                self.game_over_menu.draw()
                for button in self.game_over_menu.buttons:
                    if button.clicked:
                        if button.text == "Restart":
                            self.game_state = "game"
                        elif button.text == "Quit":
                            self.game_state = "start"
                        button.clicked = False
                        self.initialize_objects()
                        self.game_over_menu.selected = button.text
            elif self.game_state == "select_skin":
                self.select_skin.draw()
                for sub_button in self.select_skin.buttons:
                    if sub_button.clicked:
                        if sub_button.text == "Arctic":
                            self.user.skin = "arctic"
                        elif sub_button.text == "Rainbow":
                            self.user.skin = "rainbow"
                        elif sub_button.text == "Camouflage":
                            self.user.skin = "camouflage"
                        elif sub_button.text == "Back":
                            self.game_state = "start"
                        sub_button.clicked = False
                        self.select_skin.selected = sub_button.text
            elif self.game_state == "select_background":
                self.select_background.draw()
                for sub_button in self.select_background.buttons:
                    if sub_button.clicked:
                        if sub_button.text == "Space":
                            self.background = pygame.image.load("images/space.jpg")
                        elif sub_button.text == "Rainbow":
                            self.background = pygame.image.load("images/rainbow.jpg")
                        elif sub_button.text == "Lake":
                            self.background = pygame.image.load("images/lake.jpg")
                        elif sub_button.text == "Back":
                            self.game_state = "start"
                        sub_button.clicked = False
                        self.select_background.selected = sub_button.text
            elif self.game_state == "start":
                self.start_menu.draw()
                for button in self.start_menu.buttons:
                    if button.clicked:
                        if button.text == "Select Background":
                            self.game_state = "select_background"   
                        elif button.text == "Select Skin":
                            self.game_state = "select_skin"  
                        elif button.text == "Start":
                            self.game_state = "game"
                        button.clicked = False
                        self.start_menu.selected = button.text
            elif self.game_state == "game":
                self.background = pygame.transform.scale(self.background, (self.width, self.height))
                self.gameScreen.blit(self.background, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_over = True
                    elif event.type == pygame.KEYDOWN:
                        self.game_state = "pause"
                    elif event.type == pygame.MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                        angle = math.atan2(mouse_pos[1] - self.user.head.y, mouse_pos[0] - self.user.head.x)
                        self.user.angle_list.insert(0, angle)
                        self.user.angle_list.pop()
                        self.user.move()  
                self.user.draw(screen=self.gameScreen)
                self.score_board.draw(self.gameScreen)
                if pygame.time.get_ticks() - self.timer >= self.spawn_period:
                    self.spawn_bot()
                for spell in self.spells:
                    spell.draw(self.gameScreen)
                for bot in self.players[1:]:
                    bot.draw(self.gameScreen)
                    bot.update_bot_path(self.spells)
                    bot.move()
                self.update_players()
                self.update_spells()
                for obstacle in self.obstacles:
                    obstacle.draw(self.gameScreen)
                self.update_obstacles()
            pygame.display.update() # update the display
            self.clock.tick(60)


game = Game()
game.run()

