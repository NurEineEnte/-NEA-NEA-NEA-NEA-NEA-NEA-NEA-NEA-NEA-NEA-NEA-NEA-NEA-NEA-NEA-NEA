import pygame
import time
from pygame import mixer
import math
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

pygame.init()
#background_colour = (138, 194, 212)
#background_colour = (180,167,214)
background_colour = (0,0,0)
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

placedobjects = []

def resetscreen():
    screen.fill((0,0,0))

def mainMenu():
    signInBtn = Button(screen, [600,400,450,90])
    signUpBtn = Button(screen, [600,600,450,90])
    guestBtn = Button(screen, [600,800,450,90])
    activeBtns = [signInBtn, signUpBtn, guestBtn]
    for btn in activeBtns:
        btn.render(screen,[self.x, self.y, self.width, self.height])
    
class Button:
    def __init__(self, surface, position, btncolour = (208,224,227), btncolourdark = (133,143,146)):
        self.surface = surface
        self.x = position[0]
        self.y = position [1]
        self.width = position [2]
        self.height = position[3]
    def render(surface, position):
        if self.x <= mouse[0] <= self.x+self.width and self.y <= mouse[1] <= self.x+self.height:
            pygame.draw.rect(screen,btncolour,position)
        else:
            pygame.draw.rect(screen,btncolourdark,position)
class Planet:
    def __init__(self, position, radius, colour, speed, angle, angleincrement, mass):
        self.position = position
        self.radius = radius
        self.speed = speed
        self.angle = angle
        self.colour = colour
        self.angleincrement = angleincrement
        self.mass = mass
        print(self.position)
    def move(self):
        self.position = (self.position[0]+5, self.position[1])
    def incrementangle(self):
        self.angle = self.angle + self.angleincrement

    # i ought to remove one of these i suppose
    def anglemove(self):
        while True:
            if self.angle >= 360:
                self.angle -= 360
            elif self.angle < 0:
                self.angle +=360
            else:
                break
        if self.angle >= 0:
            self.position = (self.position[0]+self.speed*math.sin(math.radians(self.angle)), self.position[1]-self.speed*math.cos(math.radians(self.angle)))
        elif self.angle >= 90:
            self.position = (self.position[0]-self.speed*math.cos(math.radians(self.angle)), self.position[1]-self.speed*math.sin(math.radians(self.angle)))   
        elif self.angle >= 180:
            self.position = (self.position[0]+self.speed*math.cos(math.radians(self.angle)), self.position[1]+self.speed*math.sin(math.radians(self.angle)))    
        else:
            self.position = (self.position[0]-self.speed*math.sin(math.radians(self.angle)), self.position[1]+self.speed*math.cos(math.radians(self.angle)))
    def calculateforce(self, otherBody):
        distanceSquared = (self.position[0] - otherBody.position[0]) ** 2 + (self.position[1] - otherBody.position[1]) ** 2
        force = 98100000000*0.00000000006674 * self.mass * otherBody.mass / distanceSquared
    #is this really right?
    def movevectors(self, otherBody):
        #sort out later, its really inefficient and an eyesore

        
        



        self.dx = self.position[0] - otherBody.position[0]
        self.dy = self.position[1] - otherBody.position[1]
        distance = math.sqrt(self.dx**2+self.dy**2)
        force = 9810000000000*0.00000000006674 * self.mass * otherBody.mass / ((self.position[0] - otherBody.position[0]) ** 2 + (self.position[1] - otherBody.position[1]) ** 2)
        scaleFactor = force / distance
        
        self.position = (self.position[0] - scaleFactor*self.dx, self.position[1] - scaleFactor*self.dy)

        
        
            

        
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)



    

    
    
#1600x1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
resetscreen()





mixer.init()
mixer.music.load(r"C:\Users\alanj\Downloads\joy_of_remembrance.ogg")
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
                elif 1000 <= mouse[0] <= 1000+100 and 850 <= mouse[1] <= 850+100:
                    resetscreen()
                    if planetcreate == False:
                        planetcreate = True
                    else:
                        planetcreate = False
                elif planetcreate: 
                    #planet = Planet(mouse, 15, (255,204,156), 4, 3, 1, 5)
                    planet = Planet(mouse, 15, (64, 130, 222), 4, 3, 1, 5)
                    planet.draw(screen)
                    placedobjects.append(planet)
                    
                    
#code for shading rectangles
     #main menu       
    if mainmenuappear == True:
        mainMenu()
        my_font = pygame.font.SysFont('Times new roman', 100)
        mytext = my_font.render("Astrophysics Simulator", True, (180,167,214))
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

            resetscreen()
            for i in range(len(placedobjects)):
                placedobjects[i].incrementangle()
                placedobjects[i].anglemove()
                placedobjects[i].draw(screen)

                #heres a thing
                for j in range(len(placedobjects)):
                    if i != j:
                        placedobjects[i].calculateforce(placedobjects[j])
                        placedobjects[i].movevectors(placedobjects[j])
            
            pygame.display.update()
           
                              
        else:
            mytext = my_font.render("paused", True, (0, 0, 0))
            screen.blit(mytext, (50,850))

        
    pygame.display.update()
