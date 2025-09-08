import pygame
import time
from pygame import mixer
pygame.init()
background_colour = (138, 194, 212)
width = 1600
height = 1000

btncolour = (208,224,227)
btncolourdark = (133,143,146)

mainmenuappear = True
login_appear = False
signup = False
main_appear = False
planetcreate = False
playing = False

global placedobjects
placedobjects = []

def resetscreen():
    screen.fill((180,167,214))

class Planet:
    def __init__(self, position, radius, colour, speed, angle):
        self.position = position
        self.radius = radius
        self.speed = speed
        self.angle = angle
        self.colour = colour
        print(self.position)
    def move(self):
        self.position = (self.position[0]+5, self.position[1])
        resetscreen()
    def draw(self):
        pygame.draw.circle(screen, planet.colour, planet.position, planet.radius)



    

    
    
#1600x1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
resetscreen()





mixer.init()
mixer.music.load(r"C:\Users\alanj\Downloads\nea\joy of remembrance.ogg")
mixer.music.set_volume(0.5)
mixer.music.play(1)


while True:
     
    for event in pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:

#code for button presses            
            if mainmenuappear == True:                
                if 600 <= mouse[0] <= 600+450 and 400 <= mouse[1] <= 400+90:
                    login_appear = True
                    mainmenuappear = False
                    resetscreen()
                if 600 <= mouse[0] <= 600+450 and 600 <= mouse[1] <= 600+90:
                    signup = True
                    mainmenuappear = False
                    resetscreen()
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90:
                    main_appear = True
                    mainmenuappear = False
                    resetscreen()

            if main_appear == True:
                #play button
                if 0 <= mouse[0] <= 0+200 and 850 <= mouse[1] <= 850+100:
                    resetscreen()
                    if playing == False:
                        playing = True
                    else:
                        playing = False

                #toggle planet creation    
                if 1000 <= mouse[0] <= 1000+100 and 850 <= mouse[1] <= 850+100:
                    resetscreen()
                    if planetcreate == False:
                        planetcreate = True
                    else:
                        planetcreate = False
                elif planetcreate:
                    global planet 
                    planet = Planet(mouse, 15, (255,204,156), 5, 90)
                    planet.draw()
                    
                    
#code for shading rectangles
     #main menu       
    if mainmenuappear == True:
        my_font = pygame.font.SysFont('Times new roman', 100)
        mytext = my_font.render("something about something", True, (0, 0, 0))
        screen.blit(mytext, (300,100))
        if 600 <= mouse[0] <= 600+450 and 400 <= mouse[1] <= 400+90:
            pygame.draw.rect(screen,btncolour,[600,400,450,90])
        else:
            pygame.draw.rect(screen,btncolourdark,[600,400,450,90])

        if 600 <= mouse[0] <= 600+450 and 600 <= mouse[1] <= 600+90:
            pygame.draw.rect(screen,btncolour,[600,600,450,90])
        
        else:
            pygame.draw.rect(screen,btncolourdark,[600,600,450,90])

        if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90:
            pygame.draw.rect(screen,btncolour,[600,800,450,90])
        
        else:
            pygame.draw.rect(screen,btncolourdark,[600,800,450,90])
    if main_appear == True:
        if 0 <= mouse[0] <= 0+200 and 850 <= mouse[1] <= 850+100:
            pygame.draw.rect(screen,btncolour,[0,850,200,100])
        else:
            pygame.draw.rect(screen,btncolourdark,[0,850,200,100])
            
        if 200 <= mouse[0] <= 200+800 and 850 <= mouse[1] <= 850+100:
            pygame.draw.rect(screen,btncolour,[200,850,800,100])
        else:
            pygame.draw.rect(screen,btncolourdark,[200,850,800,100])
            
        if 1000 <= mouse[0] <= 1000+100 and 850 <= mouse[1] <= 850+100:
            pygame.draw.rect(screen,btncolour,[1000,850,100,100])
        else:
            pygame.draw.rect(screen,btncolourdark,[1000,850,100,100])

        my_font = pygame.font.SysFont('Times new roman', 25)                  
        if planetcreate:
            mytext = my_font.render("planet on", True, (0, 0, 0))
            screen.blit(mytext, (1000,850))
        else:
            mytext = my_font.render("planet off", True, (0, 0, 0))
            screen.blit(mytext, (1000,850))

        if playing:
            mytext = my_font.render("playing", True, (0, 0, 0))
            screen.blit(mytext, (50,850))
            planet.move()
            planet.draw()
        else:
            mytext = my_font.render("paused", True, (0, 0, 0))
            screen.blit(mytext, (50,850))

        

    pygame.display.update()

