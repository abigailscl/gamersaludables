import pygame
import os
class Picker():
    def __init__(self, pos_x, pos_y, window):
        self.stationary = pygame.image.load('robotsprite_1.png')
        self.left =  []
        self.left.append(pygame.image.load('walkLeft_0.png'))
        self.left.append(pygame.image.load('walkLeft_1.png'))
        self.right = []
        self.right.append(pygame.image.load('walkRight_1.png'))
        self.right.append(pygame.image.load('walkRight_2.png'))
        self.velocity = 10
        self.move_left = False
        self.move_right = False
        self.stepIndex = 0
        self.display = window
        
    def draw_game(self):
        if self.stepIndex >= 36:
            stepIndex = 0
        if move_left:
            self.display.blit(self.left[stepIndex//4], (self.pos_x,self.pos_y))
            stepIndex += 1
        elif move_right:
            self.display.blit(self.right[stepIndex//4], (self.pos_x,self.pos_y))
            stepIndex += 1
        else:
            self.display.blit(self.stationary, (self.pos_x,self.pos_y))

#pygame.init()
#win = pygame.display.set_mode((500, 500))

# Load Images of the Character (there are two popular ways)
#stationary = pygame.image.load('robotsprite_1.png')
# One way to do it - using the sprites that face left.
#left =  []
#left.append(pygame.image.load('walkLeft_0.png'))
#left.append(pygame.image.load('walkLeft_1.png'))

# Another (faster) way to do it - using the sprites that face right.
#right = []
#right.append(pygame.image.load('walkRight_1.png'))
#right.append(pygame.image.load('walkRight_2.png'))


#x = 250
#y = 250
#vel = 10
#move_left = False
#move_right = False
#stepIndex = 0

# Draw the Game
#def draw_game():
 #   global stepIndex
  #  win.fill((0, 0, 0))
   # if stepIndex >= 36:
    #    stepIndex = 0
    #if move_left:
     #   win.blit(self.left[stepIndex//4], (self.pos_x,self.pos_y))
      #  stepIndex += 1
    #elif move_right:
     #   win.blit(self.right[stepIndex//4], (self.pos_x,self.pos_y))
      #  stepIndex += 1
    #else:
     #   win.blit(stationary, (self.pos_x,self.pos_y))


# Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_game()

    # Movement
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        self.pos_x -= vel
        self.move_left = True
        move_right = False
    elif userInput[pygame.K_RIGHT]:
        self.pos_x += vel
        move_left = False
        move_right = True
    else:
        move_left = False
        move_right = False
        stepIndex = 0

    pygame.time.delay(30)
    pygame.display.update()  
  
