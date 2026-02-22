#imports pygame, which will be crucial for providing GUI handling, and the HCI for my program, also including audio outputs as seen below
import pygame
#the time module will allow me to keep track of time flow in the program (since the epoch) and perhaps more notably, allow me to do sleep() for the program
import time
#imports the mixer module specificically so I do not have to spend code doing the full pygame.mixer.etc... later, allows music and sound
from pygame import mixer
#below imports the maths function, which can handle trigonometry for angles, pythagoras for length, exponentials, roots, and more maths in general
import math
#importing the windll module from the ctypes library allows me to change properties/metadata of the python exectuable
from ctypes import windll
#importing sys allows the executable to stop running after pygame stops, all without returning an error
import sys
#sqlite 3 is my SQL connector and will allow me to interact with local .db files
import sqlite3
#os works with file handling and i use it to check for paths and delete paths
import os
#ast will allow me to read a list from a file effectively
import ast
#and random can be used for generating random planet colours
import random

#this handles graphics and basically stops the upscaling of the window, which would result in a pixel being defined differently for each device
#but this will keep it constant between devices so that my simulator will always be small enough to be displayed on the screen fully
windll.shcore.SetProcessDpiAwareness(1)

#initialises the pygame module
pygame.init()

#alternate background colours, because I ended up going with a simple black in the end
#background_colour = (138, 194, 212)
#background_colour = (180,167,214)

#defining some constants

#background colour is black
background_colour = (0,0,0)
#resolution
width = 1600
height = 950
#button colours
btncolour = (208,224,227)
btncolourdark = (133,143,146)

#here are the booleans for which screen should be displayed
mainmenuappear = True
mainmenu2appear = False
login_appear = False
signup_appear = False
securityCreateAppear = False
securityVerifyAppear = False
securityCreateInput = False
securityVerifyInput = False
main_appear = False
#music mute control
musicmuted = False
#determines if planets or stars should be created when clicked
planetcreate = False
starcreate = False
#plays/paused simulation
playing = False
#controls whether user is in the process of an input
logInUsername = False
logInPassword = False
signUpUsername =False
signUpPassword = False
#more code for if screens should appear
viewStudentStats = False
loadSims_appear = False
objectMenuAppear = False
createSaveAppear = False

#the below is used to store inputs for account creation and account login before checking them against the database
accountType = "None"
usernameText = ""
passwordText = ""
securityQuestionID = ""
securityText = ""
#controls whether user is entering an input for planet attributes
enteringMass, enteringSpeed, enteringAngle = False, False, False

#creates a blank array for placed objects at the beginning of the program (its just the menu so none should have been placed)
placedobjects = []

#this subroutine resets the screen by just filling it with black
def resetScreen():
    #fills screen with black
    screen.fill((0,0,0))

#below subroutine handles the drawing of my main menu for when you are not logged in
def mainMenu():
    #snippet of how I render font, this time it draws the program name
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Astrophysics Simulator", True, (180,167,214))
    screen.blit(mytext, (350,100))
    #define the currently active buttons
    signInBtn = Button(screen, [600,400,450,90])
    signUpBtn = Button(screen, [600,600,450,90])
    guestBtn = Button(screen, [600,800,450,90])
    activeBtns = [signInBtn, signUpBtn, guestBtn]
    #draw the currently active buttons by iterating throuugh the list
    for btn in activeBtns:
        btn.render(screen, btn.position)
    #draws text onto buttons
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("Sign in", True, (0,0,0))
    screen.blit(mytext, (750,415)) 
    mytext = my_font.render("Sign up", True, (0,0,0))
    screen.blit(mytext, (745,615)) 
    mytext = my_font.render("Guest", True, (0,0,0))
    screen.blit(mytext, (760,815)) 

#subroutine handles the rendering of the main menu after the user has logged in
def mainMenuLoggedIn():
    #draws the title of the program and that it is now logged in
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Astrophysics Simulator (logged in)", True, (180,167,214))
    screen.blit(mytext, (85,100))
    #define buttons
    newBtn = Button(screen, [600,400,450,90])
    loadBtn = Button(screen, [600,600,450,90])
    statsBtn = Button(screen, [600,800,450,90])
    activeBtns = [newBtn, loadBtn, statsBtn]
    #drawing buttons
    for btn in activeBtns:
        btn.render(screen, btn.position)
    #draw text onto the buttons
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("New Simulation", True, (0,0,0))
    screen.blit(mytext, (660,415)) 
    mytext = my_font.render("Load Simulation", True, (0,0,0))
    screen.blit(mytext, (655,615)) 
    mytext = my_font.render("View Student Stats", True, (0,0,0))
    screen.blit(mytext, (630,815))

#this menu handles the loading of simulations from files and should provide 6 save slots
def loadSimsMenu():
    #draw the title of the page, which is loading
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Load Simulation", True, (180,167,214))
    screen.blit(mytext, (500,100))
    #instantiate buttons
    btn1 = Button(screen, [400,400,250,90])
    btn2 = Button(screen, [400,600,250,90])
    btn3 = Button(screen, [400,800,250,90])
    btn4 = Button(screen, [1000,400,250,90])
    btn5 = Button(screen, [1000,600,250,90])
    btn6 = Button(screen, [1000,800,250,90])
    backBtn = Button(screen, [575,910,450,20])
    activeBtns = [btn1, btn2, btn3, btn4, btn5, btn6, backBtn]
    #render buttons via iteration
    for btn in activeBtns:
        btn.render(screen, btn.position)
    #draw the text onto the save slots to number them
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("Sim 1", True, (0,0,0))
    screen.blit(mytext, (460,415)) 
    mytext = my_font.render("Sim 2", True, (0,0,0))
    screen.blit(mytext, (460,615)) 
    mytext = my_font.render("Sim 3", True, (0,0,0))
    screen.blit(mytext, (460,815))
    mytext = my_font.render("Sim 4", True, (0,0,0))
    screen.blit(mytext, (1060,415)) 
    mytext = my_font.render("Sim 5", True, (0,0,0))
    screen.blit(mytext, (1060,615)) 
    mytext = my_font.render("Sim 6", True, (0,0,0))
    screen.blit(mytext, (1060,815))
    my_font = pygame.font.SysFont('Times new roman', 30)
    #draw other button text
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))

#below subroutine handles the drawing of the view stats menu, which should only be accessible by teachers, tracks student engagement        
def viewStatsMenu():
    #draw title of page
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("User Statistics", True, (180,167,214))
    screen.blit(mytext, (530,100))
    #define buttons
    backBtn = Button(screen, [575,910,450,20])
    activeBtns = [backBtn]
    #draw buttons
    for btn in activeBtns:
        btn.render(screen, btn.position)
    #draw text onto buttons
    my_font = pygame.font.SysFont('Times new roman', 30)
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))    

#this will draw the base screen of the main simulator part of the program and provide an interaface
def mainSimulator():
    #reset the screen before rendering
    resetScreen()
    #define buttons
    musicBtn = Button(screen, [0,850,200,100])
    playBtn = Button(screen, [200,850,200,100])
    createPlanetBtn = Button(screen, [400,850,100,100])
    createStarBtn = Button(screen, [500,850,100,100])
    menuBtn = Button(screen, [850,850,250,100])

    activeBtns = [musicBtn, playBtn, menuBtn, createPlanetBtn, createStarBtn]
    
    #checks that the create save button has not been pressed before seeing if it should define and draw the larger save button
    if not createSaveAppear:
        saveBtn = Button(screen, [600,850,250,100])
        activeBtns.append(saveBtn)
    #draw the buttons
    for btn in activeBtns:
        btn.render(screen, btn.position)
    #draw text onto buttons
    my_font = pygame.font.SysFont('Times new roman', 30)
    mytext = my_font.render("Save sim", True, (0,0,0))
    screen.blit(mytext, (670,850))
    mytext = my_font.render("Back to menu", True, (0,0,0))
    screen.blit(mytext, (890,850))

    #this iterates through all objects/celestial bodies currently in the file, and renders them properly
    for planet in placedobjects:
        #determines a planets radius which will scale in line with a planets mass
        planet.determineradius()
        #draws each planet individually
        planet.draw(screen)

#the objectmenu subroutine is called when the user clicks on a planet, presumably to edit its attributes
#this will handle the drawing of everything related to it
def objectMenu(body):
    #fills in a portion of the right hand side of the screen so that buttons and text can be displayed over it
    pygame.draw.rect(screen, (180,167,214), (1100, 0, 600, 950))
    #define buttons
    speedBtn = Button(screen, [1200,250,200,50], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    angleBtn = Button(screen, [1200,400,200,50], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    massBtn = Button(screen, [1200,550,200,50], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    activeBtns = [speedBtn, angleBtn, massBtn]
    #render buttons
    for btn in activeBtns:
        btn.render(screen, btn.position)
    #draws text onto the object menu
    my_font = pygame.font.SysFont('Times new roman', 75)
    #name of planet
    mytext = my_font.render("Planet", True, (0,0,0))
    screen.blit(mytext, (1250,25))
    #still name of planet, this is numbers based off the position in the list
    mytext = my_font.render(str(body+1), True, (0,0,0))
    screen.blit(mytext, (1330,95))
    #allows the user to see the attribute they are editing by drawing the text to the left of the input box
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("Mass", True, (0,0,0))
    screen.blit(mytext, (1235,195))
    mytext = my_font.render("Speed", True, (0,0,0))
    screen.blit(mytext, (1235,340))
    mytext = my_font.render("Angle (bearing)", True, (0,0,0))
    screen.blit(mytext, (1155,490))
    my_font = pygame.font.SysFont('Times new roman', 30)
    #this code uses the input variables to display the current attributes fora body, and this also updates as they type in so they can
    #see what they are typing in
    mytext = my_font.render(str(enterMass), True, (0, 0, 0))
    screen.blit(mytext, (1200+5,257))
    mytext = my_font.render(str(enterSpeed), True, (0, 0, 0))
    screen.blit(mytext, (1200+5,407))
    mytext = my_font.render(str(enterAngle), True, (0, 0, 0))
    screen.blit(mytext, (1200+5,557))
    #draws units to the right of the input boxes
    mytext = my_font.render("x 10^8 kg", True, (0, 0, 0))
    screen.blit(mytext, (1400+5,257))
    mytext = my_font.render("km/s", True, (0, 0, 0))
    screen.blit(mytext, (1400+5,407))
    mytext = my_font.render("°", True, (0, 0, 0))
    screen.blit(mytext, (1400+5,547))

#below subroutine handles rendering of the create save menu, which overlays the save button in the main simulator program
#this is only run once the button in question has been pressed
def createSaveMenu():
    #define buttons
    slot1Btn = Button(screen, [600,850,83,50])
    slot2Btn = Button(screen, [600,900,83,50])
    slot3Btn = Button(screen, [683.3,850,83,50])
    slot4Btn = Button(screen, [683.3,900,83,50])
    slot5Btn = Button(screen, [766.6,850,84,50])
    slot6Btn = Button(screen, [766.6,900,84,50])
    activeBtns = [slot1Btn, slot2Btn, slot3Btn, slot4Btn, slot5Btn, slot6Btn]
    #render buttons
    for btn in activeBtns:
        btn.render(screen, btn.position)
    #draw text onto each of the save slot buttons, just the numbered files
    my_font = pygame.font.SysFont('Times new roman', 30)
    mytext = my_font.render("1", True, (0,0,0))
    screen.blit(mytext, (635,850))
    mytext = my_font.render("2", True, (0,0,0))
    screen.blit(mytext, (635,900))
    mytext = my_font.render("3", True, (0,0,0))
    screen.blit(mytext, (718.6,850))
    mytext = my_font.render("4", True, (0,0,0))
    screen.blit(mytext, (718.5,900))
    mytext = my_font.render("5", True, (0,0,0))
    screen.blit(mytext, (801,850))
    mytext = my_font.render("6", True, (0,0,0))
    screen.blit(mytext, (801,900))

#handles the rendering of the sign in screen
def signInScreen():
    #displays title of the screen
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Log in", True, (180,167,214))
    screen.blit(mytext, (675,100))
    #sets whether the user is typing to false, as to not record any inputs
    typingUsername, typingPassword = False, False
    #defines buttons
    usernameBtn = Button(screen, [575,400,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    passwordBtn = Button(screen, [575,600,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    signInBtn = Button(screen, [575,800,450,90])
    backBtn = Button(screen, [575,910,450,20])
    activeBtns = [usernameBtn, passwordBtn,signInBtn, backBtn]
    #renders buttons
    for btn in activeBtns:
        btn.render(screen, btn.position)
    #displays that the user is inputting their username to the left of the input
    my_font = pygame.font.SysFont('Times new roman', 30)
    #checks if input is empty
    if usernameText == "":
        #if it is, display "input username here"
        mytext = my_font.render("input username here", True, (0, 0, 0))
        screen.blit(mytext, (575+5,400+30))
    else:
        #if it isnt, draw what they currently have typed in onto the input button/box
        mytext = my_font.render(usernameText, True, (0, 0, 0))
        screen.blit(mytext, (575+5,400+30))
    #check if password input is empty
    if passwordText == "":
        #if it is, then say they can enter their password here
        mytext = my_font.render("input password here", True, (0, 0, 0))
        screen.blit(mytext, (575+5,600+30))
    else:
        #if it isnt, draw what they have typed in onto the screen so they can see what they are inputting
        mytext = my_font.render(passwordText, True, (0, 0, 0))
        screen.blit(mytext, (575+5,600+30))
    #draw text onto buttons
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("Sign in", True, (0,0,0))
    screen.blit(mytext, (725,815))

#below 
def checkUserExists():
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    search_query = ("""SELECT username
                    FROM accounts                           
                    WHERE username = ?""")
    result = cur.execute(search_query, (usernameText,))
    try:
        result.fetchone()[0]
        con.close()
    except:
        return False
    else:
        return True
    
def checkpassword():
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    search_query = ("""SELECT password
                        FROM accounts                           
                        WHERE username = ?""")
    result = cur.execute(search_query, (usernameText,))
    dbPassword = result.fetchone()[0]
    if hashingAlgorithm(passwordText) == int(dbPassword):
        return True
    else:
        return False

def checkIfTeacher():
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    search_query = ("""SELECT accountType
                        FROM accounts                           
                        WHERE username = ?""")
    result = cur.execute(search_query, (usernameText,))
    try:
        fetchedAccountType = result.fetchone()[0]
        con.close()
    except:
        return "None"
    else:
        if fetchedAccountType == "T":
            return True
        else:
            return False
    
    

def securityverifyscreen():
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Answer Security Question", True, (180,167,214))
    screen.blit(mytext, (360,100))
    my_font = pygame.font.SysFont('Times new roman', 75)
    mytext = my_font.render("Question", True, (217, 234, 211))
    screen.blit(mytext, (850,350))
    securityBtn = Button(screen, [300,400,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    backBtn = Button(screen, [575,910,450,20])

    signInBtn = Button(screen, [575,800,450,90])
    activeBtns = [securityBtn, signInBtn, backBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)
    my_font = pygame.font.SysFont('Times new roman', 30)
    if securityText == "":
        mytext = my_font.render("input answer here", True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))
    else:
        mytext = my_font.render(securityText, True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))

    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    my_font = pygame.font.SysFont('Times new roman', 50)

    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    search_query = ("""SELECT question
                        FROM accounts, securityQuestions                           
                        WHERE accounts.questionID = securityQuestions.questionID
                        AND username = ?""")
    result = cur.execute(search_query, (usernameText,))
    securityQuestion = result.fetchone()[0]

    con.close()
    my_font = pygame.font.SysFont('Times new roman', 30)
    mytext = my_font.render("Question: " + str(securityQuestion), True, (133,143,146))
    screen.blit(mytext, (850,575))

    mytext = my_font.render("Verify account", True, (0,0,0))
    screen.blit(mytext, (710,835))           

def verifySecurityInput():
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    search_query = ("""SELECT questionanswer
                        FROM accounts                           
                        WHERE username = ?""")
    result = cur.execute(search_query, (usernameText,))
    dbSecurity = result.fetchone()[0]
    if hashingAlgorithm(securityText) == int(dbSecurity):
        return True
    else:
        return False    

def signUpScreen():
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Sign up", True, (180,167,214))
    screen.blit(mytext, (650,100))
    my_font = pygame.font.SysFont('Times new roman', 75)
    mytext = my_font.render("Account Type", True, (217, 234, 211))
    screen.blit(mytext, (890,350))
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
    
def securityQuestionScreen():
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Create Security Question", True, (180,167,214))
    screen.blit(mytext, (360,100))
    my_font = pygame.font.SysFont('Times new roman', 75)
    mytext = my_font.render("Question", True, (217, 234, 211))
    screen.blit(mytext, (890,350))
    securityBtn = Button(screen, [300,400,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    firstBtn = Button(screen, [850,450,100,90], btncolour=(255,242,244), btncolourdark=(206, 183, 213))
    secondBtn = Button(screen, [1025,450,100,90], btncolour=(255,242,204), btncolourdark=(223, 210, 171))
    thirdBtn = Button(screen, [1200,450,100,90], btncolour=(234,209,220), btncolourdark=(206, 183, 193))
    backBtn = Button(screen, [575,910,450,20])
    
    signInBtn = Button(screen, [575,800,450,90])
    activeBtns = [securityBtn, firstBtn, secondBtn, thirdBtn, signInBtn, backBtn]
    for btn in activeBtns:
        btn.render(screen, btn.position)
    my_font = pygame.font.SysFont('Times new roman', 30)
    if securityText == "":
        mytext = my_font.render("input answer here", True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))
    else:
        mytext = my_font.render(securityText, True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))

    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    mytext = my_font.render("1", True, (0, 0, 0))
    screen.blit(mytext, (890,450+30))
    mytext = my_font.render("2", True, (0, 0, 0))
    screen.blit(mytext, (1065,450+30))
    mytext = my_font.render("3", True, (0, 0, 0))
    screen.blit(mytext, (1240,450+30))
    my_font = pygame.font.SysFont('Times new roman', 50)

# here goes the question from database, make sure to try put it in a where
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    result = cur.execute("""
                    SELECT *
                    FROM securityQuestions;
                        """)
    if securityQuestionID != "":
        securityQuestion = result.fetchall()[int(securityQuestionID-1)][1]
    else:
        securityQuestion = ""
    con.close()
    my_font = pygame.font.SysFont('Times new roman', 30)
    mytext = my_font.render("Question: " + str(securityQuestion), True, (133,143,146))
    screen.blit(mytext, (850,575))

    mytext = my_font.render("Create account", True, (0,0,0))
    screen.blit(mytext, (650,815))       
#this hashing algorithm is a bit scuffed icl
def hashingAlgorithm(textToHash):
    charValueList = []
    for i in range(len(textToHash)):
        charValueList.append(ord(textToHash[i]))
    totalValue = 0
    for i in range(len(charValueList)):
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

def newAccountDB():
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    result = cur.execute("""
                    SELECT *
                    FROM accounts
                    ORDER BY accountID DESC;
                        """)
    g = int(result.fetchone()[0]) + 1
    if accountType != "Teacher":
        securityQuestionID = ""
        securityTextHash = ""
    else:
        securityTextHash = hashingAlgorithm(securityText)
        #lookhere
        securityQuestionID = 1
    insert_data_query = """
    INSERT INTO accounts VALUES(?, ?, ?, ?, ?, ?);
    """
    cur.execute(insert_data_query, (str(g), usernameText, str(hashingAlgorithm(passwordText)), accountType[0],  str(securityTextHash), str(securityQuestionID),))
    con.commit()
    
    insert_data_query = """
    INSERT INTO accountstats VALUES(?, 0, 0);
    """
    cur.execute(insert_data_query, (str(g),))
    con.commit()

    con.close()
                         
def saveSimToFile(saveslot):
    path = str(saveslot) + ".txt"
    if os.path.exists(r"C:\Users\alanj\Downloads\NEA\save" + path):
        os.remove(r"C:\Users\alanj\Downloads\NEA\save" + path)

    f = open(r"C:\Users\alanj\Downloads\NEA\save" + path, "a")
    for i in range(len(placedobjects)):
        f.write(str(placedobjects[i].position) + "\n")
        f.write(str(placedobjects[i].radius) + "\n")
        f.write(str(placedobjects[i].colour) + "\n")
        f.write(str(placedobjects[i].speed) + "\n")
        f.write(str(placedobjects[i].angle) + "\n")
        f.write(str(placedobjects[i].angleincrement) + "\n")
        f.write(str(placedobjects[i].mass) + "\n")
        f.write("\n")
    f.close()

def loadSimFromFile(saveslot):
    placedobjects = []
    path = str(saveslot) + ".txt"
    f = open(r"C:\Users\alanj\Downloads\NEA\save" + path, "r")
    while True:
        position = f.readline().strip()
        if position == "":
            break
        else:
            position = ast.literal_eval(position)

        radius = float(f.readline().strip())
        colour = ast.literal_eval(f.readline().strip())
        print(type(colour))
        speed = float(f.readline().strip())
        angle = float(f.readline().strip())
        angleincrement = float(f.readline().strip())
        mass = float(f.readline().strip())
        f.readline()
        planet = Planet(position, radius, colour, speed, angle, angleincrement, mass)
        placedobjects.append(planet)
    f.close()
    return placedobjects
                                

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
    def move(self):
        self.position = (self.position[0]+5, self.position[1])
    def incrementangle(self):
        self.angle = self.angle + self.angleincrement
    def determineradius(self):
        self.radius = 15 + self.mass * 0.5

    def anglemove(self):
        self.angle %= 360
        self.position = (self.position[0]+self.speed*math.sin(math.radians(self.angle)), self.position[1]-self.speed*math.cos(math.radians(self.angle)))

    def movevectors(self, otherBody):
        dx = otherBody.position[0] - self.position[0]
        dy = otherBody.position[1] - self.position[1]
        distanceSquared = dx ** 2 + dy ** 2
        distance = math.sqrt(dx**2+dy**2)
        force = 0.0001*0.00000000006674 * self.mass* 100000000 * otherBody.mass * 100000000 / distanceSquared



        acceleration = force / self.mass

        speed = (self.speed * math.sin(math.radians(self.angle)), -self.speed * math.cos(math.radians(self.angle)))
        scaleFactor = acceleration / distance
        changeVelocityVectors = (scaleFactor * dx, scaleFactor * dy)        

        speed = (speed[0] + changeVelocityVectors[0], speed[1] + changeVelocityVectors[1])
        self.speed = math.sqrt(speed[0]**2+speed[1]**2)
        self.angle = math.degrees(math.atan2(speed[0],-speed[1]))

        
        
            

        
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)

    def checkclick(self):
        dy = mouse[1] -self.position[1]
        dx = mouse[0] - self.position[0]
        distance = math.sqrt(dx**2+dy**2)
        if distance <= self.radius:
            return True
    
    def checkCollision(self, otherBody):
        dx = otherBody.position[0] - self.position[0]
        dy = otherBody.position[1] - self.position[1]
        distanceSquared = dx**2 + dy**2
        combinedRadiiSquared = (self.radius + otherBody.radius)**2
        if distanceSquared <= combinedRadiiSquared:
            return True
    def mergeBodies(self, otherBody):
        self.mass += otherBody.mass




    
    
#1600x950
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
resetScreen()





mixer.init()
mixer.music.load(r"C:\Users\alanj\Downloads\NEA\above_story.ogg")
mixer.music.set_volume(1)
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
                    mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
                    mixer.music.play(1)
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
                    if checkUserExists():
                        if checkpassword():
                            if checkIfTeacher():
                                securityVerifyAppear = True
                                login_appear = False
                            else:
                                mainmenu2appear = True
                                login_appear = False
                        else:
                            print("pass fail")
                    else:
                        print("user fail")

                    resetScreen()
                elif 575 <= mouse[0] <= 575+450 and 910<= mouse[1] <= 910+20:
                    mainmenuappear = True
                    login_appear = False
                    resetScreen()
            
            elif securityVerifyAppear:
                if 300 <= mouse[0] <= 300+450 and 400 <= mouse[1] <= 400+90:
                    securityText = ""
                    securityVerifyInput = True
                else:
                    securityVerifyInput = False    
                
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90 and len(passwordText) > 4 and len(usernameText) > 4:
                        if verifySecurityInput():
                            mainmenu2appear = True
                            securityVerifyAppear = False
                elif 575 <= mouse[0] <= 575+450 and 910<= mouse[1] <= 910+20:
                    mainmenuappear = True
                    securityVerifyAppear = False
                    resetScreen()
                #careful of this particular reset
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
                
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90 and len(passwordText) > 4 and len(usernameText) > 4 and not checkUserExists():
                    if accountType == "Student":
                        newAccountDB()
                        mainmenu2appear = True
                        signup_appear = False
                    elif accountType == "Teacher":
                        signup_appear = False
                        securityCreateAppear = True
                elif 575 <= mouse[0] <= 575+450 and 910<= mouse[1] <= 910+20:
                    mainmenuappear = True
                    signup_appear = False
                    resetScreen()
                #careful of this particular reset
                resetScreen()

            elif securityCreateAppear:
                if 300 <= mouse[0] <= 300+450 and 400 <= mouse[1] <= 400+90:
                    securityText = ""
                    securityCreateInput = True
                else:
                    securityCreateInput = False    
                
                if 850 <= mouse[0] <= 850+100 and 450 <= mouse[1] <= 450+90:
                    securityQuestionID = 1
                elif 1025 <= mouse[0] <= 1025+100 and 450 <= mouse[1] <= 450+90:
                    securityQuestionID = 2   
                elif 1200 <= mouse[0] <= 1200+100 and 450 <= mouse[1] <= 450+90:
                    securityQuestionID = 3   
                
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90 and len(passwordText) > 4 and len(usernameText) > 4:
                    newAccountDB()
                    mainmenu2appear = True
                    securityCreateAppear = False
                elif 575 <= mouse[0] <= 575+450 and 910<= mouse[1] <= 910+20:
                    mainmenuappear = True
                    securityCreateAppear = False
                    resetScreen()
                #careful of this particular reset
                resetScreen()

            elif mainmenu2appear:
               
                if 600 <= mouse[0] <= 600+450 and 400 <= mouse[1] <= 400+90:
                    main_appear = True
                    mainmenu2appear = False
                    resetScreen()
                    mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
                    mixer.music.play(1)
                if 600 <= mouse[0] <= 600+450 and 600 <= mouse[1] <= 600+90:
                    loadSims_appear = True
                    mainmenu2appear = False
                    resetScreen()
                if 600 <= mouse[0] <= 600+450 and 800 <= mouse[1] <= 800+90:
                    viewStudentStats = True
                    mainmenu2appear = False
                    resetScreen()

            elif loadSims_appear:
                    if 400 <= mouse[0] <= 400+250 and 400<= mouse[1] <= 400+90:
                        placedobjects = loadSimFromFile(1)
                        main_appear = True
                        loadSims_appear = False
                        resetScreen()
                        mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
                        mixer.music.play(1)
                    elif 400 <= mouse[0] <= 400+250 and 600<= mouse[1] <= 600+90:
                        placedobjects = loadSimFromFile(2)
                        main_appear = True
                        loadSims_appear = False
                        resetScreen()
                        mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
                        mixer.music.play(1)        
                    elif 400 <= mouse[0] <= 400+250 and 800<= mouse[1] <= 800+90:
                        placedobjects = loadSimFromFile(3)
                        main_appear = True
                        loadSims_appear = False
                        resetScreen()                        
                        mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
                        mixer.music.play(1)        
                    elif 1000 <= mouse[0] <= 1000+250 and 400<= mouse[1] <= 400+90:
                        placedobjects = loadSimFromFile(4)
                        main_appear = True
                        loadSims_appear = False
                        resetScreen()                        
                        mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
                        mixer.music.play(1)        
                    elif 1000 <= mouse[0] <= 1000+250 and 600<= mouse[1] <= 600+90:
                        placedobjects = loadSimFromFile(5)
                        main_appear = True
                        loadSims_appear = False
                        resetScreen()
                        mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
                        mixer.music.play(1)        
                    elif 1000 <= mouse[0] <= 1000+250 and 800<= mouse[1] <= 800+90:
                        placedobjects = loadSimFromFile(6)
                        main_appear = True
                        loadSims_appear = False
                        resetScreen()
                        mixer.music.load(r"C:\Users\alanj\Downloads\NEA\joy_of_rememberance.ogg")
                        mixer.music.play(1)                            
                    elif 575 <= mouse[0] <= 575+450 and 910<= mouse[1] <= 910+20:
                        mainmenu2appear = True
                        loadSims_appear = False
                        resetScreen()
            elif viewStudentStats:
                    if 575 <= mouse[0] <= 575+450 and 910<= mouse[1] <= 910+20:
                        mainmenu2appear = True
                        viewStudentStats = False
                        resetScreen()                

            elif main_appear == True:
                if 0 <= mouse[0] <= 0+200 and 850 <= mouse[1] <= 850+100:
                    resetScreen()
                    if musicmuted == False:
                        musicmuted = True
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                        musicmuted = False

                #play button
                elif 200 <= mouse[0] <= 200+200 and 850 <= mouse[1] <= 850+100:
                    resetScreen()
                    if playing == False:
                        playing = True
                    else:
                        playing = False


                elif mouse[0]<1100 and objectMenuAppear == True:
                    objectMenuAppear = False
                    placedobjects[checkedplanet].mass = float(enterMass)
                    placedobjects[checkedplanet].angle = float(enterAngle)
                    placedobjects[checkedplanet].speed = float(enterSpeed)                 
                elif not planetcreate and not starcreate and playing == False and objectMenuAppear == False and mouse[1] < 850:
                    for checkedplanet in range(len(placedobjects)):
                        if placedobjects[checkedplanet].checkclick():
                            enterMass = placedobjects[checkedplanet].mass
                            enterAngle = placedobjects[checkedplanet].angle
                            enterSpeed = placedobjects[checkedplanet].speed
                            objectMenuAppear = True
                            break

                elif 600 <= mouse[0] <= 600+250 and 850 <= mouse[1] <= 850+100:
                    if createSaveAppear:
                        if 600 <= mouse[0] <= 600+83 and 850 <= mouse[1] <= 850+50:
                            saveSimToFile(1)
                        elif 600 <= mouse[0] <= 600+83 and 900 <= mouse[1] <= 900+50:
                            saveSimToFile(2)
                        elif 683 <= mouse[0] <= 683+83 and 850 <= mouse[1] <= 850+50:
                            saveSimToFile(3)
                        elif 683 <= mouse[0] <= 683+83 and 900 <= mouse[1] <= 900+50:
                            saveSimToFile(4)
                        elif 766 <= mouse[0] <= 766+84 and 850 <= mouse[1] <= 850+50:
                            saveSimToFile(5)
                        elif 766 <= mouse[0] <= 766+84 and 900 <= mouse[1] <= 900+50:
                            saveSimToFile(6)
                        my_font = pygame.font.SysFont('Times new roman', 30)
                        mytext = my_font.render("Saved to file", True, (1, 200, 50))
                        screen.blit(mytext, (655,800))
                        pygame.display.update()
                        time.sleep(.5)
                        
                        createSaveAppear = False
                    else:
                        planetcreate = False
                        starcreate = False
                        createSaveAppear = True
                        resetScreen()
                        
                                #toggle planet creation    
                elif 400 <= mouse[0] <= 400+100 and 850 <= mouse[1] <= 850+100:
                    resetScreen()
                    if not planetcreate:
                        planetcreate = True
                        starcreate = False
                    else:
                        planetcreate = False
                elif 500 <= mouse[0] <= 500+100 and 850 <= mouse[1] <= 850+100:
                    resetScreen()
                    if not starcreate:
                        starcreate = True
                        planetcreate = False
                    else:
                        starcreate = False
                elif planetcreate: 
                    planet = Planet(mouse, 15, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 5, 0, 1, 5)
                    placedobjects.append(planet)
                elif starcreate:
                    star = Planet(mouse, 15, (255,155,0), 0, 0, 0, 100)    
                    placedobjects.append(star)
                elif 850 <= mouse[0] <= 850+250 and 850 <= mouse[1] <= 850+100:
                    playing = False
                    objectMenuAppear = False
                    planetcreate = False
                    starcreate = False
                    mainmenu2appear = True
                    placedobjects = []
                    main_appear = False
                    resetScreen()
                    mixer.music.load(r"C:\Users\alanj\Downloads\NEA\above_story.ogg")
                    mixer.music.play(1)

                    
                #checkwhatthehell

                if objectMenuAppear == True:
                    if 1200 <= mouse[0] <= 1200+200 and 250 <= mouse[1] <= 250+50:
                        enterMass = str(placedobjects[checkedplanet].mass)
                        enteringMass = True
                    elif enteringMass == True:
                        try:
                            placedobjects[checkedplanet].mass = float(enterMass)
                        except:
                            enterMass = 0
                            placedobjects[checkedplanet].mass = float(enterMass)
                        enteringMass = False

                    if 1200 <= mouse[0] <= 1200+200 and 400 <= mouse[1] <= 400+50:
                        enterSpeed = str(placedobjects[checkedplanet].speed)
                        enteringSpeed = True
                    elif enteringSpeed == True:
                        try:
                            placedobjects[checkedplanet].speed = float(enterSpeed)#
                        except:
                            enterSpeed = 0
                            placedobjects[checkedplanet].speed = float(enterSpeed)
                        enteringSpeed = False

                    if 1200 <= mouse[0] <= 1200+200 and 550 <= mouse[1] <= 550+50:
                        enterAngle = str(placedobjects[checkedplanet].angle)
                        enteringAngle = True
                    elif enteringAngle == True:
                        try:
                            placedobjects[checkedplanet].angle = float(enterAngle)#
                        except:
                            enterAngle = 0
                            placedobjects[checkedplanet].angle = float(enterAngle)
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
            
            if securityCreateInput:
                if event.key == pygame.K_BACKSPACE:
                    securityText = securityText[:-1]
                elif len(securityText)>=30:
                    my_font = pygame.font.SysFont('Times new roman', 50)
                    mytext = my_font.render("answer too long", True, (180,167,214))
                    screen.blit(mytext, (575,500))
                else:
                    securityText += event.unicode

            if securityVerifyInput:
                if event.key == pygame.K_BACKSPACE:
                    securityText = securityText[:-1]
                elif len(securityText)>=30:
                    my_font = pygame.font.SysFont('Times new roman', 50)
                    mytext = my_font.render("answer too long", True, (180,167,214))
                    screen.blit(mytext, (575,500))
                else:
                    securityText += event.unicode

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

        if musicmuted:
            mytext = my_font.render("unmute music", True, (0, 0, 0))
            screen.blit(mytext, (20,850))  
        else:
            mytext = my_font.render("mute music", True, (0, 0, 0))
            screen.blit(mytext, (30,850))                           
        if planetcreate:
            mytext = my_font.render("planet on", True, (0, 0, 0))
            screen.blit(mytext, (400,850))
        else:
            mytext = my_font.render("planet off", True, (0, 0, 0))
            screen.blit(mytext, (400,850))
        if starcreate:
            mytext = my_font.render("star on", True, (0, 0, 0))
            screen.blit(mytext, (515,850))
        else:
            mytext = my_font.render("star off", True, (0, 0, 0))
            screen.blit(mytext, (515,850))
        
        pygame.draw.rect(screen, (133,143,146), (1100, 850, 500, 100))
        mytext = my_font.render("click on a planet while paused", True, (0, 0, 0))
        screen.blit(mytext, (1100,850))
        mytext = my_font.render("and not placing to edit", True, (0, 0, 0))
        screen.blit(mytext, (1100,90))

        if objectMenuAppear:
            objectMenu(checkedplanet)
        
        if createSaveAppear:
            createSaveMenu()
            
        if playing:

            resetScreen()
            mytext = my_font.render("playing", True, (0, 0, 0))
            screen.blit(mytext, (250,850))

            for i in range(len(placedobjects)):
                collisionFound = False
                #to be removed some point ofc
                placedobjects[i].anglemove()
                #code could be more optimised if below dealt with


                #heres a thing
                for j in range(len(placedobjects)):
                    if i != j:
                        if placedobjects[i].checkCollision(placedobjects[j]):
                            placedobjects[i].mergeBodies(placedobjects[j])
                            placedobjects.pop(j)
                            collisionFound = True
                            break
                        placedobjects[i].movevectors(placedobjects[j]) 
                if collisionFound: 
                    break
                placedobjects[i].draw(screen)      

            pygame.display.update() 
                              
        else:
            mytext = my_font.render("paused", True, (0, 0, 0))
            screen.blit(mytext, (250,850))
    elif login_appear == True:
        signInScreen()
    
    elif securityVerifyAppear:
        securityverifyscreen()

    elif signup_appear == True:
        signUpScreen()

    elif securityCreateAppear:
        securityQuestionScreen()

    elif mainmenu2appear:
        mainMenuLoggedIn()

    elif loadSims_appear:
        loadSimsMenu()
    
    elif viewStudentStats:
        viewStatsMenu()
        
    pygame.display.update()