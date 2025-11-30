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
height = 950

btncolour = (208,224,227)
btncolourdark = (133,143,146)

mainmenuappear = True
login_appear = False
signup = False
main_appear = False
planetcreate = False
playing = False

placedobjects = []

def resetScreen():
    screen.fill((0,0,0))

def mainMenu():
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Astrophysics Simulator", True, (180,167,214))
    screen.blit(mytext, (300,100))
    signInBtn = Button(screen, [600,400,450,90])
    signUpBtn = Button(screen, [600,600,450,90])
    guestBtn = Button(screen, [600,800,450,90])
    activeBtns = [signInBtn, signUpBtn, guestBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)

def mainSimulator():
    playBtn = Button(screen, [0,850,200,100])
    placeholderBtn = Button(screen, [200,850,800,100])
    createPlanetBtn = Button(screen, [1000,850,100,100])
    activeBtns = [playBtn, placeholderBtn, createPlanetBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)

def signUpScreen():
    print("hi")
    #placeholder
def signInScreen():
    print("hi")
    #placeholder

class Button:
    def __init__(self, surface, position, btncolour = (208,224,227), btncolourdark = (133,143,146)):
        self.surface = surface
        self.x = position[0]
        self.y = position [1]
        self.width = position [2]
        self.height = position[3]
        self.position = position
    def render(self, surface, position):
        if self.x <= mouse[0] <= self.x+self.width and self.y <= mouse[1] <= self.y+self.height:
            pygame.draw.rect(screen,btncolour,self.position)
        else:
            pygame.draw.rect(screen,btncolourdark,self.position)
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
        force = 981000000000*0.00000000006674 * self.mass * otherBody.mass / distanceSquared
    #is this really right? maybe remove a 0 from force modifier
    def movevectors(self, otherBody):
        #sort out later, its really inefficient and an eyesore

        
        



        self.dx = self.position[0] - otherBody.position[0]
        self.dy = self.position[1] - otherBody.position[1]
        distance = math.sqrt(self.dx**2+self.dy**2)
        force = 98100000000000*0.00000000006674 * self.mass * otherBody.mass / ((self.position[0] - otherBody.position[0]) ** 2 + (self.position[1] - otherBody.position[1]) ** 2)
        scaleFactor = force / distance
        
        self.position = (self.position[0] - scaleFactor*self.dx, self.position[1] - scaleFactor*self.dy)

        
        
            

        
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)



    

    
    
#1600x950
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
resetScreen()





mixer.init()
mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
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
                    resetScreen()
                if 600 <= mouse[0] <= 600+450 and 600 <= mouse[1] <= 600+90:
                    signup = True
                    mainmenuappear = False
                    resetScreen()
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90:
                    main_appear = True
                    mainmenuappear = False
                    resetScreen()

            if main_appear == True:
                #play button
                if 0 <= mouse[0] <= 0+200 and 850 <= mouse[1] <= 850+100:
                    resetScreen()
                    if playing == False:
                        playing = True
                    else:
                        playing = False

                #toggle planet creation    
                elif 1000 <= mouse[0] <= 1000+100 and 850 <= mouse[1] <= 850+100:
                    resetScreen()
                    if planetcreate == False:
                        planetcreate = True
                    else:
                        planetcreate = False
                elif planetcreate: 
                    planet = Planet(mouse, 15, (255,204,156), 5, 3, 1, 5)
                    planet.draw(screen)
                    placedobjects.append(planet)
                    
                    
#code for shading rectangles
     #main menu       
    if mainmenuappear == True:
        mainMenu()

    if main_appear == True:
        mainSimulator()

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

            resetScreen()
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
    elif login_appear == True:
        my_font = pygame.font.SysFont('Times new roman', 45)
        mytext = my_font.render("log in", True, (155, 0, 0))
        screen.blit(mytext, (500,850))
    elif signup == True:
        my_font = pygame.font.SysFont('Times new roman', 45)
        mytext = my_font.render("sign up", True, (155, 0, 0))
        screen.blit(mytext, (500,850))

        
    pygame.display.update()
