import pygame
from interface.character import Player
from interface.whatsapp import Whatsapp
from pygame.locals import*
from datetime import datetime


class Recipes():
    def __init__(self, game):
        self.game = game
        self.time = None
        self.whatsapp = Whatsapp()
        self.coins = 0
        self.kitchen = pygame.image.load('images/kitchen1.png')
        self.kitchen = pygame.transform.scale(self.kitchen, (self.game.DISPLAY_W, self.game.DISPLAY_H))
       
        self.preparando = pygame.image.load('images/preparando.png')
        self.preparando = pygame.transform.scale(self.preparando, (150, 100))
        
        self.estupendo = pygame.image.load('images/estupendo.png')
        self.estupendo = pygame.transform.scale(self.estupendo, (150, 150))
        
        self.faltaron_ingredientes = pygame.image.load('images/faltaron_ingredientes.png')
        self.faltaron_ingredientes = pygame.transform.scale(self.faltaron_ingredientes, (150, 150))
        
        self.recipe1 = pygame.image.load('images/receta1info.png')
        self.recipe1 = pygame.transform.scale(self.recipe1, (300, 350))

        self.recipe2 = pygame.image.load('images/receta2info.png')
        self.recipe2 = pygame.transform.scale(self.recipe2, (300, 350))

        self.recipe3 = pygame.image.load('images/receta3info.png')
        self.recipe3 = pygame.transform.scale(self.recipe3, (300, 350))

        self.recipe4 = pygame.image.load('images/receta4info.png')
        self.recipe4 = pygame.transform.scale(self.recipe4, (300, 350))

        self.recipe5 = pygame.image.load('images/receta5info.png')
        self.recipe5 = pygame.transform.scale(self.recipe5, (300, 350))

        self.button = pygame.image.load('images/recetaLista.png')
        self.button = pygame.transform.scale(self.button, (150, 75))

        self.aguacate = pygame.image.load('images/aguacate.png')
        self.aguacate = pygame.transform.scale(self.aguacate, (50, 50))

        self.tomate = pygame.image.load('images/tomateRebanado.png')
        self.tomate = pygame.transform.scale(self.tomate, (50, 50))

        self.lechuga = pygame.image.load('images/lechuga.png')
        self.lechuga = pygame.transform.scale(self.lechuga, (50, 50))

        self.cebolla = pygame.image.load('images/cebollaVerde.png')
        self.cebolla = pygame.transform.scale(self.cebolla, (50, 50))

        self.pepino = pygame.image.load('images/pepinoRebanado.png')
        self.pepino = pygame.transform.scale(self.pepino, (50, 50))

        self.jugoLimon = pygame.image.load('images/jugoLimon.png')
        self.jugoLimon = pygame.transform.scale(self.jugoLimon, (50, 60))
        
        self.pimiento = pygame.image.load('images/pimiento.png')
        self.pimiento = pygame.transform.scale(self.pimiento, (35, 40))

        self.maiz = pygame.image.load('images/choclo.png')
        self.maiz = pygame.transform.scale(self.maiz, (35, 40))

        self.cheddar = pygame.image.load('images/cheddar.png')
        self.cheddar = pygame.transform.scale(self.cheddar, (40, 35))

        self.cilantro = pygame.image.load('images/cilantro.png')
        self.cilantro = pygame.transform.scale(self.cilantro, (40, 35))

        self.tortilla = pygame.image.load('images/tortilla.png')
        self.tortilla = pygame.transform.scale(self.tortilla, (40, 35))
        
        self.pollo = pygame.image.load('images/pollo.png')
        self.pollo = pygame.transform.scale(self.pollo, (40, 35))

        self.tazon = pygame.image.load('images/tazon.png')
        self.tazon = pygame.transform.scale(self.tazon, (150, 75))

        self.sarten = pygame.image.load('images/sarten.png')
        self.sarten = pygame.transform.scale(self.sarten, (100, 40))

        self.platillo = pygame.image.load('images/Receta1.png')
        self.platillo = pygame.transform.scale(self.platillo, (170, 150))

        self.platillo2 = pygame.image.load('images/Receta2.png')
        self.platillo2 = pygame.transform.scale(self.platillo2, (170, 150))

        self.platillo3 = pygame.image.load('images/Receta3.png')
        self.platillo3 = pygame.transform.scale(self.platillo3, (170, 150))

        self.platillo4 = pygame.image.load('images/Receta4.png')
        self.platillo4 = pygame.transform.scale(self.platillo4, (170, 150))

        self.platillo5 = pygame.image.load('images/Receta5.png')
        self.platillo5 = pygame.transform.scale(self.platillo5, (170, 150))

        self.plato = pygame.image.load('images/plato.png')
        self.plato = pygame.transform.scale(self.plato, (210, 90))
        
        #ingredientes dulces
        self.jugoNaranja = pygame.image.load('images/jugoNaranja.png')
        self.jugoNaranja = pygame.transform.scale(self.jugoNaranja, (50, 60))
        
        self.almendra = pygame.image.load('images/almendra.png')
        self.almendra = pygame.transform.scale(self.almendra, (40, 35))
        
        self.banana = pygame.image.load('images/banana.png')
        self.banana = pygame.transform.scale(self.banana, (40, 35))
        
        self.fresas = pygame.image.load('images/fresas.png')
        self.fresas = pygame.transform.scale(self.fresas, (40, 35))
        
        self.avena = pygame.image.load('images/avena.png')
        self.avena = pygame.transform.scale(self.avena, (55, 50))
        
        self.frutos_secos = pygame.image.load('images/frutossecos.png')
        self.frutos_secos = pygame.transform.scale(self.frutos_secos, (55, 50))
        ##
        self.x_mezcla, self.y_mezcla = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_button, self.y_button = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_aguacate,  self.y_aguacate = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_tomate,  self.y_tomate = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_tazon,  self.y_tazon =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_lechuga,  self.y_lechuga = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_cebolla,  self.y_cebolla = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_pepino,  self.y_pepino = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_jugoLimon,  self.y_jugoLimon =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_pimiento, self.y_pimiento = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_maiz, self.y_maiz = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_cheddar, self.y_cheddar = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_cilantro, self.y_cilantro = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_tortilla, self.y_tortilla = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_pollo, self.y_pollo = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_almendra, self.y_almendra = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_frutos_secos, self.y_frutos_secos = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_banana, self.y_banana = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_fresas, self.y_fresas = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_avena, self.y_avena = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_jugoNaranja, self.y_jugoNaranja = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_faltaron_ingredientes, self.y_faltaron_ingredientes = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_estupendo, self.y_estupendo = self.game.DISPLAY_W, self.game.DISPLAY_H
        
        self.x_recipe1, self.y_recipe1 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe2, self.y_recipe2 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe3, self.y_recipe3 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe4, self.y_recipe4 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe5, self.y_recipe5 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_preparando, self.y_preparando = self.game.DISPLAY_W, self.game.DISPLAY_H

        self.x_platillo,  self.y_platillo =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo2,  self.y_platillo2 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo3,  self.y_platillo3 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo4,  self.y_platillo4 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo5,  self.y_platillo5 =  self.game.DISPLAY_W, self.game.DISPLAY_H

        self.x_plato,  self.y_plato =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_sarten, self.y_sarten = self.game.DISPLAY_W, self.game.DISPLAY_H
    
    def sweet_recipe(self):
        if(self.game.posX >= 142 and self.game.posX <= 172 and self.game.posY >= 228 and self.game.posY <= 265):
            self.x_jugoLimon, self.y_jugoLimon = 350,250  
            self.x_mezcla, self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla
            self.coins =  self.coins + 50
            print("update")
        elif(self.game.posX >= 104 and self.game.posX <= 127 and self.game.posY >= 256 and self.game.posY <= 281):
            self.x_almendra,  self.y_almendra = self.x_mezcla , self.y_mezcla 
            self.x_mezcla, self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla
            self.coins =  self.coins + 50
            print("update")
        elif(self.game.posX >= 197 and self.game.posX <= 227 and self.game.posY >= 247 and self.game.posY <= 275):  
            self.x_frutos_secos,  self.y_frutos_secos = self.x_mezcla , self.y_mezcla 
            self.x_mezcla, self.y_mezcla = self.x_mezcla + 25 , self.y_mezcla
            self.coins =  self.coins + 50
            print("update")    
        elif(self.game.posX >= 138 and self.game.posX <= 159 and self.game.posY >= 284 and self.game.posY <= 305):  
            self.x_fresas,  self.y_fresas = self.x_mezcla , self.y_mezcla 
            self.x_mezcla, self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla
            self.coins =  self.coins + 50
            print("update")  
        elif(self.game.posX >= 249 and self.game.posX <= 275 and self.game.posY >= 278 and self.game.posY <= 301):  
            self.x_banana,  self.y_banana = self.x_mezcla , self.y_mezcla 
            self.x_mezcla, self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla
            self.coins =  self.coins + 50
            print("update")  
        elif(self.game.posX >= 296 and self.game.posX <= 331 and self.game.posY >= 260 and self.game.posY <= 290):  
            self.x_avena,  self.y_avena = self.x_mezcla , self.y_mezcla 
            self.x_mezcla, self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla
            self.coins =  self.coins + 50
            print("update")  
        elif(self.game.posX >= 265 and self.game.posX <= 285 and self.game.posY >= 217 and self.game.posY <= 259):  
            self.x_jugoNaranja,  self.y_jugoNaranja = 354,214
            self.x_mezcla, self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla
            self.coins =  self.coins + 50
            print("update")  
         
    
    def salty_recipe(self):
        if(self.game.posX >= 142 and self.game.posX <= 172 and self.game.posY >= 228 and self.game.posY <= 265):
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
        elif(self.game.posX >= 272 and self.game.posX <= 296 and self.game.posY >= 241 and self.game.posY <= 261):
            self.x_pimiento,  self.y_pimiento = self.x_mezcla , self.y_mezcla 
            self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
            self.coins = self.coins + 50
            print("update")
        elif(self.game.posX >= 272 and self.game.posX <= 299 and self.game.posY >= 278 and self.game.posY <= 296):
            self.x_maiz,  self.y_maiz = self.x_mezcla , self.y_mezcla 
            self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
            self.coins = self.coins + 50
            print("update")
        elif(self.game.posX >= 307 and self.game.posX <= 328 and self.game.posY >= 283 and self.game.posY <= 308):
            self.x_cilantro,  self.y_cilantro = self.x_mezcla , self.y_mezcla 
            self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
            self.coins = self.coins + 50
            print("update")
        elif(self.game.posX >= 307 and self.game.posX <= 330 and self.game.posY >= 251 and self.game.posY <= 278):
            self.x_cheddar,  self.y_cheddar = self.x_mezcla , self.y_mezcla 
            self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
            self.coins = self.coins + 50
            print("update")
        elif(self.game.posX >= 337 and self.game.posX <= 373 and self.game.posY >= 280 and self.game.posY <= 307):
            self.x_tortilla,  self.y_tortilla = 540 , 190 
            self.coins = self.coins + 50
            print("update")
        elif(self.game.posX >= 348 and self.game.posX <= 372 and self.game.posY >= 255 and self.game.posY <= 278):
            self.x_pollo,  self.y_pollo = self.x_mezcla , self.y_mezcla 
            self.x_mezcla , self.y_mezcla = self.x_mezcla + 20 , self.y_mezcla 
            self.coins = self.coins + 50
            print("update")
            
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def display_message(self):
        self.time = datetime.now()
        self.whatsapp.hour = self.time.hour
        self.whatsapp.minutes = self.time.minute + 2
        self.whatsapp.number = self.game.user.phone
        self.whatsapp.send_mesage()
        
    def button_preparation(self):
        if(self.game.recipe1_display ==  True and self.coins >= 300):
            self.x_platillo,  self.y_platillo = 220,150
            self.x_plato, self.y_plato =  200,220
            self.game.user.points = self.coins
            self.game.user.update(self.game.user.id, self.game.user.name, self.game.user.phone, self.game.user.points)
            self.whatsapp.message = " Ingredientes: lechuga tomates cebollas pepino aguacate jugo de limón Receta: En un tazón mezcla la lechuga y el tomate. Agrega pepinos y cebollas. Adorna con aguacate. Agrega un poco dejugo de limón"
            self.display_message()
            print("receta lista")
            self.x_estupendo, self.y_estupendo = 653,135
        elif(self.game.recipe2_display ==  True and self.coins >= 350):
            self.x_platillo2,  self.y_platillo2 = 220,150
            self.x_plato, self.y_plato =  200,220
            self.game.user.points = self.coins
            self.game.user.update(self.game.user.id, self.game.user.name, self.game.user.phone, self.game.user.points)
            self.whatsapp.message = "Ingredientes: Pimiento verde tomates cebollas choclo en granos tortilla cilantro queso Receta: Calentar las tortillas en el sartén. Hacer una mezcla de los demás vegetales agregar el queso decorando."
            self.display_message()
            print("receta lista") 
            self.x_estupendo, self.y_estupendo = 653,135        
        elif(self.game.recipe3_display ==  True and self.coins >= 250):
            self.x_platillo3,  self.y_platillo3 = 220,150
            self.x_plato, self.y_plato =  200,220
            self.game.user.points = self.coins
            self.game.user.update(self.game.user.id, self.game.user.name, self.game.user.phone, self.game.user.points)
            self.whatsapp.message = "Ingredientes: Avena frutos secos banana almendras jugo de limón Receta: Hacer una mezcla de avena y miel. Incorporar los frutos secos. Adornar con almendras y banana picada."
            self.display_message()
            print("receta lista")
            self.x_estupendo, self.y_estupendo = 653,135
        elif(self.game.recipe4_display ==  True and self.coins >= 250):
            self.x_platillo4,  self.y_platillo4 = 220,150
            self.x_plato, self.y_plato =  200,220
            self.game.user.points = self.coins
            self.game.user.update(self.game.user.id, self.game.user.name, self.game.user.phone, self.game.user.points)
            self.whatsapp.message = "Ingredientes: Pollo en cuadritos tomates cebollas pimiento verde jugo de limón. Receta: Poner el pollo, el pimiento, jugo de limón y cebolla en un tazón por 30minutos. Poner en un palillo todas las verduras y el pollo. Asar hasta que el pollo este cocido"
            self.display_message()
            print("receta lista")
            self.x_estupendo, self.y_estupendo = 653,135
        elif(self.game.recipe5_display ==  True and self.coins >= 100):
            self.x_platillo5,  self.y_platillo5 = 220,150
            self.x_plato, self.y_plato =  200,220
            self.game.user.points = self.coins
            self.game.user.update(self.game.user.id, self.game.user.name, self.game.user.phone, self.game.user.points)
            self.whatsapp.message = "Ingredientes: Fresas banana avena jugo de naranja Receta: Hacer una masa con la banana, la avena y el jugo de naranja. Cocinar en una sartén la masa. Adornar con fresas."
            self.display_message()
            print("receta lista")
            self.x_estupendo, self.y_estupendo = 653,135
        else:
            self.x_faltaron_ingredientes, self.y_faltaron_ingredientes = 653,135
          
    def check_events_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running, self.game.playing = False, False
                self.game.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.user.points = self.coins
                    self.inicialize_recipe()
                    self.game.BACK_KEY = True
                self.game.user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN :
                
                print(self.game.posX)
                print(self.game.posY)
                
                if(self.game.posX >= 756 and self.game.posX <= 892 and self.game.posY >= 410 and self.game.posY <= 461):
                    self.clean_table()
                    self.button_preparation()
                    self.inicialize_recipe()
                    
                elif(self.game.recipe1_display or self.game.recipe2_display or self.game.recipe4_display):
                    self.salty_recipe()
                    
                elif(self.game.recipe3_display or self.game.recipe5_display):
                    self.sweet_recipe()
                    
                if self.x_mezcla > 495:
                    self.x_mezcla = 370
                    self.y_mezcla = self.y_mezcla + 10
                
                pygame.display.update()
    
    def inicialize_recipe(self):
        self.game.recipe1_display, self.game.recipe2_display, self.game.recipe3_display, self.game.recipe4_display, self.game.recipe5_display = False, False, False, False, False
        
    def inicialize(self):
        
        self.coins = 0
        self.x_mezcla, self.y_mezcla = 370,230
        self.x_button, self.y_button = 740,400
        self.x_tazon,  self.y_tazon =  370,240
        
        if self.game.recipe1_display ==  True:
            self.x_recipe1, self.y_recipe1 = 650,50

        elif self.game.recipe2_display ==  True:
            self.x_recipe2, self.y_recipe2 = 650,50 
            self.x_tortilla, self.y_tortilla = 337,280
            self.x_sarten, self.y_sarten = 527,200
            
        elif self.game.recipe3_display ==  True:
            self.x_recipe3, self.y_recipe3 = 650,50 
            self.x_sarten, self.y_sarten = 527,225

        elif self.game.recipe4_display ==  True:
            self.x_recipe4, self.y_recipe4 = 650,50 
            self.x_pollo, self.y_pollo = 335,250

        elif self.game.recipe5_display ==  True:
            self.x_recipe5, self.y_recipe5 = 650,50 
               
        if self.game.recipe4_display or self.game.recipe2_display or self.game.recipe1_display:
           
            self.x_aguacate,  self.y_aguacate = 219,235
            self.x_tomate,  self.y_tomate = 183,237
            self.x_lechuga,  self.y_lechuga = 160,260
            self.x_cebolla,  self.y_cebolla = 210,260
            self.x_pepino,  self.y_pepino = 98,250
            self.x_jugoLimon,  self.y_jugoLimon =  140,225
            self.x_pimiento, self.y_pimiento = 265, 236
            self.x_maiz, self.y_maiz = 265, 260
            self.x_cheddar, self.y_cheddar = 300, 248
            self.x_cilantro, self.y_cilantro = 303, 280
            
        self.x_jugoNaranja, self.y_jugoNaranja = self.game.DISPLAY_W, self.game.DISPLAY_H
            
        if self.game.recipe3_display or self.game.recipe5_display:
            #ingredientes dulces
            self.x_almendra,  self.y_almendra = 98,250
            self.x_frutos_secos,  self.y_frutos_secos = 183,237
            self.x_jugoLimon,  self.y_jugoLimon =  140,225
            self.x_banana, self.y_banana = 240, 270
            self.x_fresas, self.y_fresas = 131, 275
            self.x_avena, self.y_avena = 285, 250
            self.x_jugoNaranja, self.y_jugoNaranja = 240,210
                
            print("ingredintes dulces")
        
        self.x_platillo,  self.y_platillo =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo2,  self.y_platillo2 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo3,  self.y_platillo3 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo4,  self.y_platillo4 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo5,  self.y_platillo5 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_plato,  self.y_plato =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_faltaron_ingredientes, self.y_faltaron_ingredientes = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_estupendo, self.y_estupendo = self.game.DISPLAY_W, self.game.DISPLAY_H

    def clean_table(self):
        self.x_aguacate,  self.y_aguacate = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_tomate,  self.y_tomate =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_tazon,  self.y_tazon =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_lechuga,  self.y_lechuga =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_cebolla,  self.y_cebolla = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_pepino,  self.y_pepino =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_jugoLimon,  self.y_jugoLimon =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_pimiento, self.y_pimiento = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_maiz, self.y_maiz = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_cheddar, self.y_cheddar = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_cilantro, self.y_cilantro = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_tortilla, self.y_tortilla = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_pollo, self.y_pollo = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_almendra,  self.y_almendra = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_frutos_secos,  self.y_frutos_secos = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_banana, self.y_banana = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_fresas, self.y_fresas = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_avena, self.y_avena = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_jugoNaranja, self.y_jugoNaranja = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_sarten, self.y_sarten = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe1, self.y_recipe1 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe2, self.y_recipe2 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe4, self.y_recipe4 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe3, self.y_recipe3 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_recipe5, self.y_recipe5 = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_sarten, self.y_sarten = self.game.DISPLAY_W, self.game.DISPLAY_H 
        self.x_preparando, self.y_preparando = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo,  self.y_platillo =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo2,  self.y_platillo2 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo3,  self.y_platillo3 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo4,  self.y_platillo4 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_platillo5,  self.y_platillo5 =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_plato,  self.y_plato =  self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_faltaron_ingredientes, self.y_faltaron_ingredientes = self.game.DISPLAY_W, self.game.DISPLAY_H
        self.x_estupendo, self.y_estupendo = self.game.DISPLAY_W, self.game.DISPLAY_H
        

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
            self.game.display.blit(self.recipe2, (self.x_recipe2, self.y_recipe2))
            self.game.display.blit(self.recipe3, (self.x_recipe3, self.y_recipe3))
            self.game.display.blit(self.recipe4, (self.x_recipe4, self.y_recipe4))
            self.game.display.blit(self.recipe5, (self.x_recipe5, self.y_recipe5))

            self.game.display.blit(self.button, (self.x_button, self.y_button))
            self.game.display.blit(self.tazon, (self.x_tazon,  self.y_tazon) )
            self.game.display.blit(player.image , player.rect )
            self.game.display.blit(self.plato, (self.x_plato, self.y_plato))
            
            self.game.display.blit(self.jugoNaranja, (self.x_jugoNaranja, self.y_jugoNaranja))
            self.game.display.blit(self.jugoLimon, (self.x_jugoLimon,  self.y_jugoLimon) ) 
            self.game.display.blit(self.pepino, (self.x_pepino,  self.y_pepino) ) 
            self.game.display.blit(self.lechuga, (self.x_lechuga,  self.y_lechuga) ) 
            self.game.display.blit(self.tomate, (self.x_tomate,  self.y_tomate) ) 
            self.game.display.blit(self.cebolla, (self.x_cebolla,  self.y_cebolla) ) 
            self.game.display.blit(self.aguacate, (self.x_aguacate,  self.y_aguacate) )
            self.game.display.blit(self.pimiento, (self.x_pimiento, self.y_pimiento))
            self.game.display.blit(self.maiz, (self.x_maiz,  self.y_maiz) ) 
            self.game.display.blit(self.cheddar, (self.x_cheddar,  self.y_cheddar) )
            self.game.display.blit(self.cilantro, (self.x_cilantro,  self.y_cilantro) )
            self.game.display.blit(self.sarten, (self.x_sarten,  self.y_sarten) ) 
            self.game.display.blit(self.tortilla, (self.x_tortilla,  self.y_tortilla) )
            self.game.display.blit(self.pollo, (self.x_pollo,  self.y_pollo) )
            self.game.display.blit(self.frutos_secos, (self.x_frutos_secos,  self.y_frutos_secos))
            self.game.display.blit(self.almendra, (self.x_almendra,  self.y_almendra) )
            self.game.display.blit(self.fresas, (self.x_fresas,  self.y_fresas) )
            self.game.display.blit(self.avena, (self.x_avena,  self.y_avena) )
            self.game.display.blit(self.banana, (self.x_banana,  self.y_banana) )
            
            #self.game.display.blit(self.preparando, (self.x_preparando, self.y_preparando))
            self.game.display.blit(self.estupendo, (self.x_estupendo,  self.y_estupendo) )
            self.game.display.blit(self.faltaron_ingredientes, (self.x_faltaron_ingredientes,  self.y_faltaron_ingredientes) )

            self.game.display.blit(self.platillo, (self.x_platillo, self.y_platillo))
            self.game.display.blit(self.platillo2, (self.x_platillo2, self.y_platillo2))
            self.game.display.blit(self.platillo3, (self.x_platillo3, self.y_platillo3))
            self.game.display.blit(self.platillo4, (self.x_platillo4, self.y_platillo4))
            self.game.display.blit(self.platillo5, (self.x_platillo5, self.y_platillo5))
            clock.tick(60)
            self.game.window.blit(self.game.display, (0,0))
            pygame.display.update()
            self.game.reset_keys()