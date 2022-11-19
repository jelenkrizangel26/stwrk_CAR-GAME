import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("Assignment4\stwrk_CAR-GAME\\crash.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race and Dashed')
clock = pygame.time.Clock()

carImg = pygame.image.load('Assignment4\stwrk_CAR-GAME\\racecar.png')
gameIcon = pygame.image.load('Assignment4\stwrk_CAR-GAME\\carIcon.png')

pygame.display.set_icon(gameIcon)

pause = False

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rext()

def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Oh no! You Crashed (X_X)", largeText)
    gameDisplay.blit(TextSurf, TextRect)

    