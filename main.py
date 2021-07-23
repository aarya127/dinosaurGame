##
# Pygame base template for opening a window - MVC version
# Simpson College Computer Science
# http://programarcadegames.com/
##
#This program will be a game where user gets to control the bus and the dinosaur
#
#@author: Aarya Shah
#@course: ICS3UI-03
#@date: 2020/05/21
#
# Import a library of functions called 'pygame'
import pygame
import random

#LIST OF COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE= (255,140,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKYBLUE=(135,206,235)
DARKGRAY = (64,64,64)
GRAY=(128, 128, 128)
LIGHTBROWN = (245,222,179)
BROWN = (139,69,19)
DARKBROWN = (128,0,0)
GOLD=(255,215,0)

# Set the height and width of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bus Game")

# Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

#Inital Bus xcoordinate and speed
bus_x = 15
bus_speed = 0

#Game Functions
def draw_bus(screen, x, y):
    #Body of the bus
    pygame.draw.rect(screen,ORANGE, [100+bus_x, 240,300,60], )
    pygame.draw.rect(screen,ORANGE, [100+bus_x, 210,250,40], )
    pygame.draw.rect(screen,GRAY, [100+bus_x, 290,300,10], )
    #Tires
    pygame.draw.circle(screen, BLACK, [150+bus_x, 320], 30, 0)
    pygame.draw.circle(screen, BLACK, [350+bus_x, 320], 30, 0)
    #Windows
    pygame.draw.rect(screen,RED, [300+bus_x, 220,25,70], )
    pygame.draw.rect(screen,RED, [120+bus_x, 220,25,30], )
    pygame.draw.rect(screen,RED, [160+bus_x, 220,25,30], )
    pygame.draw.rect(screen,RED, [200+bus_x,220,25,30], )
    pygame.draw.rect(screen,RED, [240+bus_x, 220,25,30], )

def draw_rock(screen, x, y):
  pygame.draw.ellipse(screen, DARKGRAY, [100, 400,70, 50])

def draw_dinosaur(screen, x, y):
  pygame.draw.rect(screen,BROWN, [100+x, 305+y,10,10], )
  pygame.draw.rect(screen,BROWN, [110+x, 295+y,10,10], )
  pygame.draw.rect(screen,BROWN, [120+x, 285+y,10,10], )
  pygame.draw.rect(screen,BROWN, [130+x, 265+y,300,20], )
  pygame.draw.rect(screen,BROWN, [190+x, 285+y,30,10], )
  pygame.draw.rect(screen,BROWN, [300+x, 255+y,190,10], )#arm
  pygame.draw.rect(screen,BROWN, [370+x, 295+y,20,10], )
  pygame.draw.rect(screen,BROWN, [360+x, 305+y,20,10], )
  pygame.draw.rect(screen,BROWN, [350+x, 315+y,20,10], )
  pygame.draw.rect(screen,BROWN, [340+x, 325+y,20,10], )
  pygame.draw.rect(screen,BROWN, [330+x, 335+y,20,10], )
  pygame.draw.rect(screen,BROWN, [330+x, 335+y,10,50], )
  pygame.draw.rect(screen,BROWN, [390+x, 325+y,10,20], )
  pygame.draw.rect(screen,BROWN, [380+x, 335+y,10,30], )
  pygame.draw.rect(screen,BROWN, [410+x, 355+y,10,20], )
  pygame.draw.rect(screen,BROWN, [420+x, 375+y,10,10], )
  pygame.draw.rect(screen,BROWN, [430+x, 385+y,10,10], )
  pygame.draw.rect(screen,BROWN, [320+x, 245+y,160,10], )#arms
  pygame.draw.rect(screen,BROWN, [420+x, 215+y,10,80], )
  pygame.draw.rect(screen,BROWN, [380+x, 215+y,60,30], )
  pygame.draw.rect(screen,BROWN, [410+x, 205+y,60,30], )
  pygame.draw.rect(screen,BROWN, [460+x, 185+y,110,10], )
  pygame.draw.rect(screen,BROWN, [460+x, 195+y,40,10], )
  pygame.draw.rect(screen,BROWN, [510+x, 215+y,60,10], )
  pygame.draw.rect(screen,BROWN, [540+x, 225+y,30,10], )
  pygame.draw.rect(screen,BROWN, [460+x, 205+y,80,10], )
  pygame.draw.rect(screen,BROWN, [350+x, 255+y,50,50], )
  pygame.draw.rect(screen,BROWN, [420+x, 235+y,30,30], )
  pygame.draw.rect(screen,BROWN, [460+x, 215+y,20,20], )
  pygame.draw.rect(screen,DARKBROWN, [100+x, 295+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [110+x, 285+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [120+x, 275+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [130+x, 265+y,20,10], )
  pygame.draw.rect(screen,DARKBROWN, [220+x, 295+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [250+x, 305+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [280+x, 295+y,90,10], )
  pygame.draw.rect(screen,DARKBROWN, [350+x, 285+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [150+x, 255+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [180+x, 265+y,90,10], )
  pygame.draw.rect(screen,DARKBROWN, [250+x, 275+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [270+x, 255+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [270+x, 275+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [280+x, 265+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [290+x, 245+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [310+x, 235+y,100,10], )
  pygame.draw.rect(screen,DARKBROWN, [340+x, 225+y,20,100], )
  pygame.draw.rect(screen,DARKBROWN, [340+x, 345+y,10,60], )
  pygame.draw.rect(screen,DARKBROWN, [350+x, 335+y,10,70], )
  pygame.draw.rect(screen,DARKBROWN, [330+x, 385+y,40,10], )
  pygame.draw.rect(screen,DARKBROWN, [350+x, 335+y,20,10], )
  pygame.draw.rect(screen,DARKBROWN, [360+x, 325+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [370+x, 315+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [380+x, 305+y,30,10], )
  pygame.draw.rect(screen,BROWN, [400+x, 315+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [410+x, 265+y,10,60], )
  pygame.draw.rect(screen,DARKBROWN, [420+x, 295+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [410+x, 295+y,10,50], )
  pygame.draw.rect(screen,DARKBROWN, [400+x, 325+y,10,80], )
  pygame.draw.rect(screen,DARKBROWN, [390+x, 345+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [410+x, 375+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [420+x, 385+y,10,20], )
  pygame.draw.rect(screen,DARKBROWN, [410+x, 195+y,50,10], )
  pygame.draw.rect(screen,DARKBROWN, [400+x, 205+y,40,10], )
  pygame.draw.rect(screen,DARKBROWN, [380+x, 215+y,40,10], )
  pygame.draw.rect(screen,DARKBROWN, [430+x, 205+y,10,20], )
  pygame.draw.rect(screen,DARKBROWN, [450+x, 185+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [450+x, 185+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [460+x, 175+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [470+x, 165+y,80,10], )
  pygame.draw.rect(screen,DARKBROWN, [480+x, 155+y,50,10], )
  pygame.draw.rect(screen,DARKBROWN, [560+x, 175+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [470+x, 225+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [460+x, 235+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [430+x, 265+y,10,20], )
  pygame.draw.rect(screen,DARKBROWN, [440+x, 245+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [450+x, 235+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [480+x, 215+y,10,10], )
  pygame.draw.rect(screen,DARKBROWN, [480+x, 255+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [460+x, 255+y,10,30], )
  pygame.draw.rect(screen,DARKBROWN, [490+x, 215+y,20,10], )
  pygame.draw.rect(screen,DARKBROWN, [510+x, 225+y,30,10], )
  pygame.draw.rect(screen,DARKBROWN, [540+x, 235+y,30,10], )
  pygame.draw.rect(screen,WHITE, [360+x, 395+y,30,10], )
  pygame.draw.rect(screen,WHITE, [370+x, 385+y,10,10], )

  pygame.draw.rect(screen,WHITE, [430+x, 395+y,30,10], )
  pygame.draw.rect(screen,WHITE, [440+x, 385+y,10,10], )
  #mouth
  pygame.draw.rect(screen,RED, [510+x, 185+y,10,10], )
  pygame.draw.rect(screen,RED, [520+x, 195+y,10,10], )
  pygame.draw.rect(screen,RED, [530+x, 185+y,10,10], )
  pygame.draw.rect(screen,RED, [540+x, 205+y,10,10], )
  pygame.draw.rect(screen,WHITE, [520+x, 185+y,10,10], )
  pygame.draw.rect(screen,WHITE, [530+x, 195+y,10,10], )
  pygame.draw.rect(screen,WHITE, [550+x, 195+y,10,10], )
  pygame.draw.rect(screen,WHITE, [560+x, 205+y,10,10], )
  #eyes
  pygame.draw.rect(screen,BLACK, [500+x, 165+y,10,10], )
  pygame.draw.rect(screen,ORANGE, [510+x, 165+y,10,10], )
pygame.init()  

# MAIN
# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

          #Bus Movement

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bus_speed = 10
            if event.key == pygame.K_LEFT:
                bus_speed = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                bus_speed = 0
            if event.key == pygame.K_LEFT:
                bus_speed = 0

    #Movement
    position = pygame.mouse.get_pos()
    print(position)
    x = position[0]
    y = position[1]

    #Background
    screen.fill(SKYBLUE)

    #Bus Movement according to Speed
    bus_x += bus_speed

    #Ground
    pygame.draw.rect(screen, GREEN, [0, 350, 1000, 1200], )
    pygame.draw.rect(screen, LIGHTBROWN, [0, 350, 1000, 100, ] )

    #Showing the bus
    draw_bus(screen, bus_x, 100)
    
    #Showing the Dinosaur
    draw_dinosaur(screen, x, y)

    #Showing the Rock
    draw_rock(screen, 300, 300)
    
 # Go ahead and update the screen with what we've drawn.

    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()