import pygame
from character import Player

from pygame.locals import*

class Recipes():
    def __init__(self, game):
        self.game = game
        self.coins = 0
        self.kitchen = pygame.image.load('kitchen1.png')
        self.kitchen = pygame.transform.scale(self.kitchen, (self.game.DISPLAY_W, self.game.DISPLAY_H))

        self.recipe1 = pygame.image.load('receta1info.png')
        self.recipe1 = pygame.transform.scale(self.recipe1, (300, 350))

        self.recipe2 = pygame.image.load('receta2info.png')
        self.recipe2 = pygame.transform.scale(self.recipe2, (300, 350))

        self.recipe3 = pygame.image.load('receta3info.png')
        self.recipe3 = pygame.transform.scale(self.recipe3, (300, 350))

        self.recipe4 = pygame.image.load('receta4info.png')
        self.recipe4 = pygame.transform.scale(self.recipe4, (300, 350))

        self.recipe4 = pygame.image.load('receta5info.png')
        self.recipe4 = pygame.transform.scale(self.recipe4, (300, 350))

        self.button = pygame.image.load('recetaLista.png')
        self.button = pygame.transform.scale(self.button, (150, 75))

        self.aguacate = pygame.image.load('aguacate.png')
        self.aguacate = pygame.transform.scale(self.aguacate, (50, 50))

        self.tomate = pygame.image.load('tomateRebanado.png')
        self.tomate = pygame.transform.scale(self.tomate, (50, 50))

        self.tazon = pygame.image.load('tazon.png')
        self.tazon = pygame.transform.scale(self.tazon, (150, 75))

        self.lechuga = pygame.image.load('lechuga.png')
        self.lechuga = pygame.transform.scale(self.lechuga, (50, 50))

        self.cebolla = pygame.image.load('cebollaVerde.png')
        self.cebolla = pygame.transform.scale(self.cebolla, (50, 50))

        self.pepino = pygame.image.load('pepinoRebanado.png')
        self.pepino = pygame.transform.scale(self.pepino, (50, 50))

        self.jugoLimon = pygame.image.load('jugoLimon.png')
        self.jugoLimon = pygame.transform.scale(self.jugoLimon, (50, 60))
        

        self.platillo = pygame.image.load('Receta1.png')
        self.platillo = pygame.transform.scale(self.platillo, (170, 150))

        self.platillo2 = pygame.image.load('Receta2.png')
        self.platillo2 = pygame.transform.scale(self.platillo2, (170, 150))

        self.platillo3 = pygame.image.load('Receta3.png')
        self.platillo3 = pygame.transform.scale(self.platillo3, (170, 150))

        self.platillo4 = pygame.image.load('Receta4.png')
        self.platillo4 = pygame.transform.scale(self.platillo4, (170, 150))

        self.platillo5 = pygame.image.load('Receta5.png')
        self.platillo5 = pygame.transform.scale(self.platillo5, (170, 150))

        self.plato = pygame.image.load('plato.png')
        self.plato = pygame.transform.scale(self.plato, (210, 90))


    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def check_events_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running, self.game.playing = False, False
                self.game.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.BACK_KEY = True
                self.game.user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN :
                print(self.game.posX)
                print(self.game.posY)
                #self.game.posX, self.game.posY = pygame.mouse.get_pos()
                if(self.game.posX >= 756 and self.game.posX <= 892 and self.game.posY >= 410 and self.game.posY <= 461):
                    if(self.game.recipe1_display ==  True and self.coins >= 300):
                        self.clean_table()
                        self.x_platillo,  self.y_platillo = 220,150
                        self.x_plato, self.y_plato =  200,220
                        print("receta lista")
                    elif(self.game.recipe2_display ==  True and self.coins > 50):
                        self.clean_table()
                        self.x_platillo2,  self.y_platillo2 = 220,150
                        self.x_plato, self.y_plato =  200,220
                        print("receta lista")
                    elif(self.game.recipe3_display ==  True and self.coins > 50):
                        self.clean_table()
                        self.x_platillo3,  self.y_platillo3 = 220,150
                        self.x_plato, self.y_plato =  200,220
                        print("receta lista")
                    elif(self.game.recipe4_display ==  True and self.coins > 50):
                        self.clean_table()
                        self.x_platillo4,  self.y_platillo4 = 220,150
                        self.x_plato, self.y_plato =  200,220
                    elif(self.game.recipe5_display ==  True and self.coins > 50):
                        self.clean_table()
                        self.x_platillo5,  self.y_platillo5 = 220,150
                        self.x_plato, self.y_plato =  200,220
                        print("receta lista")
                    self.inicialize_recipe()
                elif(self.game.posX >= 142 and self.game.posX <= 172 and self.game.posY >= 228 and self.game.posY <= 265):
                    self.x_jugoLimon, self.y_jugoLimon = 350,250  
                    self.x_mezcla, self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla
                    self.coins =  self.coins + 50
                    print("update")
                elif(self.game.posX >= 105 and self.game.posX <= 122 and self.game.posY >= 251 and self.game.posY <= 265):
                    self.x_pepino,  self.y_pepino = self.x_mezcla , self.y_mezcla 
                    self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
                    self.coins = self.coins + 50
                    print("update")
                elif(self.game.posX >= 178 and self.game.posX <= 193 and self.game.posY >= 272 and self.game.posY <= 293):
                    self.x_lechuga,  self.y_lechuga = self.x_mezcla , self.y_mezcla 
                    self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
                    self.coins = self.coins + 50
                    print("update")
                elif(self.game.posX >= 198 and self.game.posX <= 216 and self.game.posY >= 244 and self.game.posY <= 268):
                    self.x_tomate,  self.y_tomate = self.x_mezcla , self.y_mezcla 
                    self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
                    self.coins = self.coins + 50
                    print("update")
                elif(self.game.posX >= 232 and self.game.posX <= 261 and self.game.posY >= 244 and self.game.posY <= 270):
                    self.x_aguacate,  self.y_aguacate = self.x_mezcla , self.y_mezcla 
                    self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
                    self.coins = self.coins + 50
                    print("update")
                elif(self.game.posX >= 222 and self.game.posX <= 250 and self.game.posY >= 278 and self.game.posY <= 297):
                    self.x_cebolla,  self.y_cebolla = self.x_mezcla , self.y_mezcla 
                    self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
                    self.coins = self.coins + 50
                    print("update")
                if self.x_mezcla > 495:
                    self.x_mezcla = 50
                pygame.display.update()
    def inicialize_recipe(self):
        self.game.recipe1_display, self.game.recipe2_display, self.game.recipe3_display, self.game.recipe4_display, self.game.recipe5_display = False, False, False, False, False
        
    def inicialize(self):
        self.coins = 0
        if self.game.recipe1_display ==  True:
            self.x_recipe1, self.y_recipe1 = 650,50
            self.x_recipe2, self.y_recipe2 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe3, self.y_recipe3 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe4, self.y_recipe4 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe5, self.y_recipe5 = self.game.DISPLAY_W, self.game.DISPLAY_H
        elif self.game.recipe2_display ==  True:
            self.x_recipe1, self.y_recipe1 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe2, self.y_recipe2 = 650,50 
            self.x_recipe3, self.y_recipe3 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe4, self.y_recipe4 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe5, self.y_recipe5 = self.game.DISPLAY_W, self.game.DISPLAY_H
        elif self.game.recipe3_display ==  True:
            self.x_recipe1, self.y_recipe1 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe2, self.y_recipe2 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe3, self.y_recipe3 = 650,50 
            self.x_recipe4, self.y_recipe4 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe5, self.y_recipe5 = self.game.DISPLAY_W, self.game.DISPLAY_H
        elif self.game.recipe4_display ==  True:
            self.x_recipe1, self.y_recipe1 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe2, self.y_recipe2 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe3, self.y_recipe3 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe4, self.y_recipe4 = 650,50 
            self.x_recipe5, self.y_recipe5 = self.game.DISPLAY_W, self.game.DISPLAY_H
        elif self.game.recipe5_display ==  True:
            self.x_recipe1, self.y_recipe1 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe2, self.y_recipe2 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe3, self.y_recipe3 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe4, self.y_recipe4 = self.game.DISPLAY_W, self.game.DISPLAY_H
            self.x_recipe5, self.y_recipe5 = 650,50 
        self.x_mezcla, self.y_mezcla = 350,230
        self.x_button, self.y_button = 740,400
        self.x_aguacate,  self.y_aguacate = 219,235
        self.x_tomate,  self.y_tomate = 183,237
        self.x_tazon,  self.y_tazon = 350,240
        self.x_lechuga,  self.y_lechuga = 160,260
        self.x_cebolla,  self.y_cebolla = 210,260
        self.x_pepino,  self.y_pepino = 98,250
        self.x_jugoLimon,  self.y_jugoLimon =  140,225
        self.x_platillo,  self.y_platillo =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo2,  self.y_platillo2 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo3,  self.y_platillo3 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo4,  self.y_platillo4 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo5,  self.y_platillo5 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_plato,  self.y_plato =  self.game.DISPLAY_W, self.game.DISPLAY_H

    def clean_table(self):
        self.aguacate = pygame.image.load('aguacate.png')
        self.aguacate = pygame.transform.scale(self.aguacate, (50, 50))
        self.x_aguacate,  self.y_aguacate = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_tomate,  self.y_tomate =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_tazon,  self.y_tazon =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_lechuga,  self.y_lechuga =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_cebolla,  self.y_cebolla = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_pepino,  self.y_pepino =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_jugoLimon,  self.y_jugoLimon =  self.game.DISPLAY_W, self.game.DISPLAY_H
    def cooking(self, game ):
        game = False
        clock = pygame.time.Clock()
        moving_sprites = pygame.sprite.Group()
        player = Player(500,260)
        moving_sprites.add(player)
        self.inicialize()
        while self.game.playing:
            self.game.posX, self.game.posY = pygame.mouse.get_pos()  
            self.check_events_game()
            if self.game.BACK_KEY:
                self.game.playing= False 
            self.game.display.fill((0,0,0))
            moving_sprites.update(0.02)
            player.animate() 
            self.game.display.blit(self.kitchen, (0,0))
            self.game.display.blit(self.recipe1, (self.x_recipe1, self.y_recipe1))
            self.game.display.blit(self.button, (self.x_button, self.y_button))
            self.game.display.blit(self.tazon, (self.x_tazon,  self.y_tazon) )
            self.game.display.blit(player.image , player.rect )
            self.game.display.blit(self.jugoLimon, (self.x_jugoLimon,  self.y_jugoLimon) ) 
            self.game.display.blit(self.pepino, (self.x_pepino,  self.y_pepino) ) 
            self.game.display.blit(self.lechuga, (self.x_lechuga,  self.y_lechuga) ) 
            self.game.display.blit(self.tomate, (self.x_tomate,  self.y_tomate) ) 
            self.game.display.blit(self.cebolla, (self.x_cebolla,  self.y_cebolla) ) 
            self.game.display.blit(self.aguacate, (self.x_aguacate,  self.y_aguacate) ) 
            self.game.display.blit(self.plato, (self.x_plato, self.y_plato))
            self.game.display.blit(self.platillo, (self.x_platillo, self.y_platillo))
            self.game.display.blit(self.platillo2, (self.x_platillo2, self.y_platillo2))
            self.game.display.blit(self.platillo3, (self.x_platillo3, self.y_platillo3))
            self.game.display.blit(self.platillo4, (self.x_platillo4, self.y_platillo4))
            self.game.display.blit(self.platillo5, (self.x_platillo5, self.y_platillo5))
            clock.tick(60)
            self.game.window.blit(self.game.display, (0,0))
            pygame.display.update()
            self.game.reset_keys()
        




