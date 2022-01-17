import pygame
from pygame.locals import *
from random import randint
import sys

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("TUTORIAL DIEZ")

pera = pygame.image.load("pera.png")
posX = 200
posY = 200

speed = 5
white = (255,255,255)
right = True

while True:
    screen.fill(white)
    screen.blit(pera,(posX,posY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if  event.key == K_LEFT:
                posX -= speed
            elif event.key == K_RIGHT:
                posX += speed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("clic clic")

    posX, posY = pygame.mouse.get_pos()    

    posX = posX-100
    posY = posY -50        
    pygame.display.update()


#screen.blit(pera,(posX,posY))
 #   for event in pygame.event.get():
  #      if event.type == QUIT:
   #         pygame.quit()
    #        sys.exit()
     #   elif event.type == pygame.MOUSEBUTTONDOWN:
      #      print("clic clic")
       #     posX, posY = pygame.mouse.get_pos()
        #    if right == 1:
         #       screen.fill(white)
          #      
           #     right = 0
            #right = 1
    # pygame.display.update() 