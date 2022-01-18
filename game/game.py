from tkinter.constants import TRUE
import pygame
from pygame.locals import*
from menu import *
from register import Regitration
from user import User
from recipes import *

class Game():
    def __init__(self):
        pygame.init()
        
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 977, 480
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.recipes = Recipes(self)
        self.posX = 0
        self.posY = 0
        self.curr_menu = self.main_menu
        self.input_rect = pygame.Rect(200, 50, 30, 30)
        self.color = pygame.Color(self.WHITE)
        self.user_text = ""
        self.registration = Regitration(self)
        self.user = User()
        self.img = pygame.image.load('canva3.png')
        self.kitchen = pygame.image.load('kitchen.png')
        self.vamosCocinar = pygame.image.load('vamosCocinar.png')
        self.receta1 = pygame.image.load('Receta1.png')
        self.receta2 = pygame.image.load('Receta2.png')
        self.receta3 = pygame.image.load('Receta3.png')
        self.receta4 = pygame.image.load('Receta4.png')
        self.receta5 = pygame.image.load('Receta5.png')
        self.menuRecetas = pygame.image.load('menuRecetas.png')
        self.recipe1_display, self.recipe2_display, self.recipe3_display, self.recipe4_display, self.recipe5_display = False, False, False, False, False
        


    def game_loop(self):
        clock = pygame.time.Clock()
        moving_sprites = pygame.sprite.Group()
        player = Player(40,260)
        moving_sprites.add(player)
        while self.playing:
            self.posX, self.posY = pygame.mouse.get_pos()  
            self.check_events_game()
            if self.BACK_KEY:
                self.playing= False 
                #self.recipe1()
            #display pantalla
            self.display.fill((0,0,0))
            moving_sprites.update(0.02)
            player.animate() 
            self.display.blit(self.kitchen, (0,0))
            self.display.blit(player.image , player.rect )
            self.display.blit(self.menuRecetas, (270,5) ) 
            self.display.blit(self.vamosCocinar, (160,140) )
            #llamada a la funcion para empezar el juego 
            clock.tick(60)
            #self.draw_text('Gracias por jugar', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
        
    def check_events_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_LEFT:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                self.user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN :
                print(self.posX)
                print(self.posY)
                if(self.posX > 346 and self.posX < 667 and self.posY > 19 and self.posY < 88):
                    print("Ensalada")
                    self.recipe1_display = True
                    self.recipes.cooking(self.playing)
                if(self.posX > 346 and self.posX < 667 and self.posY > 110 and self.posY < 176):
                    print("Quesadilla")
                    self.recipe2_display = True
                    self.recipes.cooking(self.playing)
                if(self.posX > 346 and self.posX < 667 and self.posY > 211 and self.posY < 277):
                    print("Frutas")
                    self.recipe3_display = True
                    self.recipes.cooking(self.playing)
                if(self.posX > 346 and self.posX < 667 and self.posY > 302 and self.posY < 369):
                    print("Brochetas")
                    self.recipe4_display = True
                    self.recipes.cooking(self.playing)
                if(self.posX > 346 and self.posX < 667 and self.posY > 404 and self.posY < 470):
                    print("Panquetas")
                    self.recipe5_display = True
                    self.recipes.cooking(self.playing)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_LEFT:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
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
    
    def input_name(self):
        self.window.blit(self.display, (0, 0))
        self.window.fill((0,0,0))
        pygame.draw.rect(self.window, self.color, self.input_rect, 2)
        font = pygame.font.Font(self.font_name,15)
        text_surface = font.render(self.user_text, True, self.WHITE)
        self.window.blit(text_surface, (self.input_rect.x +10, self.input_rect.y +10))
        self.input_rect.w = text_surface.get_width() + 20
        pygame.display.update()
    
    def register_user(self):
        self.registration.main_screen()
        self.registration.screen = None

