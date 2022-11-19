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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                pygame.quit()
                quit()

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action !=None:
            action()
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        smallText = pygame.font.SysFont("comicsansms",20)
        textSurf, textRect =( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()