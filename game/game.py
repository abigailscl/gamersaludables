import pygame
from menu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.input_rect = pygame.Rect(200, 50, 30, 30)
        self.color = pygame.Color(self.WHITE)
        self.user_text = ""

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.user_text =""
                    self.START_KEY = True
                if event.key == pygame.K_LEFT:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.user_text = ""
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.user_text = ""
                    self.UP_KEY = True
                self.user_text += event.unicode

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
    
    def inputName(self):
        
        self.window.blit(self.display, (0, 0))
        self.window.fill((0,0,0))
        pygame.draw.rect(self.window, self.color, self.input_rect, 2)
        font = pygame.font.Font(self.font_name,15)
        text_surface = font.render(self.user_text, True, self.WHITE)
        self.window.blit(text_surface, (self.input_rect.x +10, self.input_rect.y +10))
        self.input_rect.w = text_surface.get_width() + 20
        pygame.display.update()
        
