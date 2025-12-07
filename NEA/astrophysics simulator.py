import pygame
import time
from pygame import mixer
import math
from ctypes import windll
import sys
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
signup_appear = False
main_appear = False
planetcreate = False
playing = False
logInUsername = False
logInPassword = False
signUpUsername =False
signUpPassword = False
objectMenuAppear = False
accountType = "None"
usernameText = ""
passwordText = ""
enteringMass, enteringSpeed, enteringAngle = False, False, False

placedobjects = []

def resetScreen():
    screen.fill((0,0,0))

def mainMenu():
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Astrophysics Simulator", True, (180,167,214))
    screen.blit(mytext, (350,100))
    signInBtn = Button(screen, [600,400,450,90])
    signUpBtn = Button(screen, [600,600,450,90])
    guestBtn = Button(screen, [600,800,450,90])
    activeBtns = [signInBtn, signUpBtn, guestBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("Sign in", True, (0,0,0))
    screen.blit(mytext, (750,415)) 
    mytext = my_font.render("Sign up", True, (0,0,0))
    screen.blit(mytext, (745,615)) 
    mytext = my_font.render("Guest", True, (0,0,0))
    screen.blit(mytext, (760,815)) 

def mainSimulator():
    resetScreen()
    playBtn = Button(screen, [0,850,200,100])
    placeholderBtn = Button(screen, [200,850,800,100])
    createPlanetBtn = Button(screen, [1000,850,100,100])
    activeBtns = [playBtn, placeholderBtn, createPlanetBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)
    for planet in placedobjects:
        planet.determineradius()
        planet.draw(screen)

def objectMenu(body):
    pygame.draw.rect(screen, (180,167,214), (1100, 0, 600, 950))
    speedBtn = Button(screen, [1200,250,200,50], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    angleBtn = Button(screen, [1200,400,200,50], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    massBtn = Button(screen, [1200,550,200,50], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    activeBtns = [speedBtn, angleBtn, massBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)
    my_font = pygame.font.SysFont('Times new roman', 75)
    mytext = my_font.render("Planet", True, (0,0,0))
    screen.blit(mytext, (1250,25))
    mytext = my_font.render(str(body+1), True, (0,0,0))
    screen.blit(mytext, (1330,95))
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("Mass", True, (0,0,0))
    screen.blit(mytext, (1235,195))
    mytext = my_font.render("Speed", True, (0,0,0))
    screen.blit(mytext, (1235,340))
    mytext = my_font.render("Angle (bearing)", True, (0,0,0))
    screen.blit(mytext, (1155,490))
    my_font = pygame.font.SysFont('Times new roman', 30)
    mytext = my_font.render(str(placedobjects[body].mass), True, (0, 0, 0))
    screen.blit(mytext, (1200+5,257))
    mytext = my_font.render(str(placedobjects[body].speed), True, (0, 0, 0))
    screen.blit(mytext, (1200+5,407))
    mytext = my_font.render(str(placedobjects[body].angle), True, (0, 0, 0))
    screen.blit(mytext, (1200+5,557))
    mytext = my_font.render("x 10^8 kg", True, (0, 0, 0))
    screen.blit(mytext, (1400+5,257))
    mytext = my_font.render("km/s", True, (0, 0, 0))
    screen.blit(mytext, (1400+5,407))
    mytext = my_font.render("°", True, (0, 0, 0))
    screen.blit(mytext, (1400+5,547))

def signInScreen():
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Log in", True, (180,167,214))
    screen.blit(mytext, (675,100))
    typingUsername, typingPassword = False, False
    usernameBtn = Button(screen, [575,400,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    passwordBtn = Button(screen, [575,600,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    signInBtn = Button(screen, [575,800,450,90])
    backBtn = Button(screen, [575,910,450,20])
    activeBtns = [usernameBtn, passwordBtn,signInBtn, backBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)
    my_font = pygame.font.SysFont('Times new roman', 30)
    if usernameText == "":
        mytext = my_font.render("input username here", True, (0, 0, 0))
        screen.blit(mytext, (575+5,400+30))
    else:
        mytext = my_font.render(usernameText, True, (0, 0, 0))
        screen.blit(mytext, (575+5,400+30))
    if passwordText == "":
        mytext = my_font.render("input password here", True, (0, 0, 0))
        screen.blit(mytext, (575+5,600+30))
    else:
        mytext = my_font.render(passwordText, True, (0, 0, 0))
        screen.blit(mytext, (575+5,600+30))
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("Sign in", True, (0,0,0))
    screen.blit(mytext, (725,815))

    
def signUpScreen():
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Sign up", True, (180,167,214))
    screen.blit(mytext, (650,100))
    my_font = pygame.font.SysFont('Times new roman', 75)
    mytext = my_font.render("Account Type", True, (217, 234, 211))
    screen.blit(mytext, (890,350))
    typingUsername, typingPassword = False, False
    usernameBtn = Button(screen, [300,400,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    passwordBtn = Button(screen, [300,600,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    studentBtn = Button(screen, [850,450,200,90], btncolour=(255,242,204), btncolourdark=(223, 210, 171))
    teacherBtn = Button(screen, [1150,450,200,90], btncolour=(234,209,220), btncolourdark=(206, 183, 193))
    backBtn = Button(screen, [575,910,450,20])
    
    signInBtn = Button(screen, [575,800,450,90])
    activeBtns = [usernameBtn, passwordBtn, teacherBtn, studentBtn, signInBtn, backBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)
    my_font = pygame.font.SysFont('Times new roman', 30)
    if usernameText == "":
        mytext = my_font.render("input username here", True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))
    else:
        mytext = my_font.render(usernameText, True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))
    if passwordText == "":
        mytext = my_font.render("input password here", True, (0, 0, 0))
        screen.blit(mytext, (300+5,600+30))
    else:
        mytext = my_font.render(passwordText, True, (0, 0, 0))
        screen.blit(mytext, (300+5,600+30))
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    mytext = my_font.render("Student", True, (0, 0, 0))
    screen.blit(mytext, (900,450+30))
    mytext = my_font.render("Teacher", True, (0, 0, 0))
    screen.blit(mytext, (1200,450+30))
    my_font = pygame.font.SysFont('Times new roman', 50)
    if accountType == "Teacher":
        colour = (206, 183, 193)
    elif accountType == "Student":
        colour = (223, 210, 171)
    else:
        colour = (133,143,146)
    mytext = my_font.render("Account type: " + accountType, True, (colour))
    screen.blit(mytext, (850,575))
    mytext = my_font.render("Create account", True, (0,0,0))
    screen.blit(mytext, (650,815))   
    

#this hashing algorithm is a bit scuffed icl
def hashingAlgorithm():
    charValueList = []
    for i in range(len(passwordText)):
        charValueList.append(ord(passwordText[i]))
    totalValue = 0
    for i in range(charValueList()):
        if i % 4 == 0:
            charValueList[i] += 20
        elif i % 3 == 0:
            charValueList[i] -= 1
        elif i % 2 == 0:
            charValueList[i] *= 2
        elif i % 1 == 0:
            charValueList[i] += 67
        else:
            charValueList[i] -= 4
        totalValue += (charValueList[i]+1)
    return totalValue

class Button:
    def __init__(self, surface, position, btncolour = (208,224,227), btncolourdark = (133,143,146)):
        self.surface = surface
        self.x = position[0]
        self.y = position [1]
        self.width = position [2]
        self.height = position[3]
        self.position = position
        self.colour = btncolour
        self.colourdark = btncolourdark
    def render(self, surface, position):
        if self.x <= mouse[0] <= self.x+self.width and self.y <= mouse[1] <= self.y+self.height:
            pygame.draw.rect(screen,self.colour,self.position)
        else:
            pygame.draw.rect(screen,self.colourdark,self.position)
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
    def determineradius(self):
        self.radius = 15 + self.mass * 0.5

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
        force = 0.00000000006674 * self.mass * otherBody.mass / distanceSquared
    #is this really right? maybe remove a 0 from force modifier
    def movevectors(self, otherBody):
        #sort out later, its really inefficient and an eyesore

        
        



        self.dx = self.position[0] - otherBody.position[0]
        self.dy = self.position[1] - otherBody.position[1]
        distance = math.sqrt(self.dx**2+self.dy**2)
        force = 0.00000000006674 * self.mass* 100000000 * otherBody.mass * 100000000 / (((self.position[0] - otherBody.position[0]) ** 2 + (self.position[1] - otherBody.position[1]) ** 2)*1000)
        scaleFactor = force / distance
        
        self.position = (self.position[0] - scaleFactor*self.dx, self.position[1] - scaleFactor*self.dy)

        
        
            

        
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)

    def checkclick(self):
        self.dy = mouse[1] -self.position[1]
        self.dx = mouse[0] - self.position[0]
        distance = math.sqrt(self.dx**2+self.dy**2)
        if distance <= self.radius:
            return True
    

    
    
#1600x950
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
resetScreen()





mixer.init()
mixer.music.load(r"C:\Users\alanj\Downloads\NEA\above_story.ogg")
mixer.music.set_volume(0.5)
mixer.music.play(1)


while True:
     
    for event in pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:

#code for button presses            
            if mainmenuappear == True:
               
                if 600 <= mouse[0] <= 600+450 and 400 <= mouse[1] <= 400+90:
                    login_appear = True
                    mainmenuappear = False
                    resetScreen()
                if 600 <= mouse[0] <= 600+450 and 600 <= mouse[1] <= 600+90:
                    signup_appear = True
                    mainmenuappear = False
                    resetScreen()
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90:
                    main_appear = True
                    mainmenuappear = False
                    resetScreen()

            elif login_appear == True:
                if 600 <= mouse[0] <= 600+450 and 400 <= mouse[1] <= 400+90:
                    usernameText = ""
                    logInUsername = True
                else:
                    logInUsername = False    
                if 600 <= mouse[0] <= 600+450 and 600 <= mouse[1] <= 600+90:
                    passwordText = ""
                    logInPassword = True
                else:
                    logInPassword = False    
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90:
                    main_appear = True
                    login_appear = False
                    resetScreen()
                elif 575 <= mouse[0] <= 575+450 and 910<= mouse[1] <= 910+20:
                    mainmenuappear = True
                    login_appear = False
                    resetScreen()
            

            elif signup_appear:
                if 300 <= mouse[0] <= 300+450 and 400 <= mouse[1] <= 400+90:
                    usernameText = ""
                    signUpUsername = True
                else:
                    signUpUsername = False    
                if 300 <= mouse[0] <= 300+450 and 600 <= mouse[1] <= 600+90:
                    passwordText = ""
                    signUpPassword = True
                else:
                    signUpPassword = False 
                
                if 850 <= mouse[0] <= 850+200 and 450 <= mouse[1] <= 450+90:
                    accountType = "Student"
                elif 1150 <= mouse[0] <= 1150+200 and 450 <= mouse[1] <= 450+90:
                    accountType = "Teacher"    
                
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90:
                    main_appear = True
                    signup_appear = False
                elif 575 <= mouse[0] <= 575+450 and 910<= mouse[1] <= 910+20:
                    mainmenuappear = True
                    signup_appear = False
                    resetScreen()
                #careful of this particular reset
                resetScreen()


            elif main_appear == True:
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
                    placedobjects.append(planet)
                elif mouse[0]<1100 and objectMenuAppear == True:
                    objectMenuAppear = False
                #change later to display stats as travel
                elif not planetcreate and playing == False and objectMenuAppear == False:
                    for checkedplanet in range(len(placedobjects)):
                        if placedobjects[checkedplanet].checkclick():
                            objectMenuAppear = True
                            break
                    print(checkedplanet)
                    
                #check

                if objectMenuAppear == True:
                    if 1200 <= mouse[0] <= 1200+200 and 250 <= mouse[1] <= 250+50:
                        enterMass = str(placedobjects[checkedplanet].mass)
                        enteringMass = True
                    elif enteringMass == True:
                        placedobjects[checkedplanet].mass = int(enterMass)
                        enteringMass = False

                    if 1200 <= mouse[0] <= 1200+200 and 400 <= mouse[1] <= 400+50:
                        enterSpeed = str(placedobjects[checkedplanet].speed)
                        enteringSpeed = True
                    elif enteringSpeed == True:
                        placedobjects[checkedplanet].speed = int(enterSpeed)
                        enteringSpeed = False

                    if 1200 <= mouse[0] <= 1200+200 and 550 <= mouse[1] <= 550+50:
                        enterAngle = str(placedobjects[checkedplanet].angle)
                        enteringAngle = True
                    elif enteringAngle == True:
                        placedobjects[checkedplanet].angle = int(enterAngle)
                        enteringAngle = False
                    

                
        if event.type == pygame.KEYDOWN:
            
            if logInUsername == True:
                if event.key == pygame.K_BACKSPACE:
                    usernameText = usernameText[:-1]
                elif len(usernameText)>=30:
                    my_font = pygame.font.SysFont('Times new roman', 50)
                    mytext = my_font.render("username too long", True, (180,167,214))
                    screen.blit(mytext, (575,500))
                else:
                    usernameText += event.unicode
            if logInPassword == True:
                if event.key == pygame.K_BACKSPACE:
                    passwordText = passwordText[:-1]
                elif len(passwordText)>=30:
                    my_font = pygame.font.SysFont('Times new roman', 50)
                    mytext = my_font.render("password too long", True, (180,167,214))
                    screen.blit(mytext, (575,500))
                else:
                    passwordText += event.unicode
            if signUpUsername == True:
                if event.key == pygame.K_BACKSPACE:
                    usernameText = usernameText[:-1]
                elif len(usernameText)>=30:
                    my_font = pygame.font.SysFont('Times new roman', 50)
                    mytext = my_font.render("username too long", True, (180,167,214))
                    screen.blit(mytext, (575,500))
                else:
                    usernameText += event.unicode
            if signUpPassword == True:
                if event.key == pygame.K_BACKSPACE:
                    passwordText = passwordText[:-1]
                elif len(passwordText)>=30:
                    my_font = pygame.font.SysFont('Times new roman', 50)
                    mytext = my_font.render("password too long", True, (180,167,214))
                    screen.blit(mytext, (575,500))
                else:
                    passwordText += event.unicode
                    
            if enteringMass == True:
                if event.key == pygame.K_BACKSPACE:
                    enterMass = enterMass[:-1]
                else:
                    enterMass += event.unicode
            if enteringSpeed == True:
                if event.key == pygame.K_BACKSPACE:
                    enterSpeed = enterSpeed[:-1]
                else:
                    enterSpeed += event.unicode
            if enteringAngle == True:
                if event.key == pygame.K_BACKSPACE:
                    enterAngle = enterAngle[:-1]
                else:
                    enterAngle += event.unicode
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
        if objectMenuAppear:
            objectMenu(checkedplanet)
            
        if playing:

            resetScreen()
            mytext = my_font.render("playing", True, (0, 0, 0))
            screen.blit(mytext, (50,850))

            for i in range(len(placedobjects)):
                #to be removed some point ofc
                placedobjects[i].incrementangle()
                placedobjects[i].anglemove()
                #code could be more optimised if below dealt with
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
        signInScreen()

    elif signup_appear == True:
        signUpScreen()


        
    pygame.display.update()
