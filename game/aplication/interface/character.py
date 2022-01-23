import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        self.sprites.append(pygame.image.load('images/robotsprite_1.png'))
        self.sprites.append(pygame.image.load('images/robotsprite_0.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate (self):
        self.is_animating = True

    def update (self, speed):
        if self.is_animating == True:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                #self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]
    

