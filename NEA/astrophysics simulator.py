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
musicmuted = False
#code for if planets/stars should be created on click
planetcreate = False
starcreate = False


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
simSpeed = 1

#the below is used to store inputs for account creation and account login before checking them against the database
accountType = "None"
enterSimSpeed = "1"
usernameText = ""
passwordText = ""
securityQuestionID = ""
securityText = ""
#controls whether user is entering an input for planet attributes
enteringMass, enteringSpeed, enteringAngle = False, False, False
enteringSimSpeed = False

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
    menuBtn = Button(screen, [850,850,250,100])
    createStarBtn = Button(screen, [500,850,100,100])
    speedBtn = Button(screen, [1100,850,500,100])

    activeBtns = [musicBtn, playBtn, menuBtn, createPlanetBtn, createStarBtn, speedBtn]
    
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
    if enteringSimSpeed:
        mytext = my_font.render(str(enterSimSpeed), True, (0, 0, 0))
    else:
        mytext = my_font.render(str(simSpeed), True, (0, 0, 0))
    screen.blit(mytext, (1320,850))
    mytext = my_font.render("Speed multiplier: ", True, (0, 0, 0))
    screen.blit(mytext, (1100,850))

    #this iterates through all objects/celestial bodies currently in the file, and renders them properly
    for planet in placedobjects:
        #determines a planets radius which will scale in line with a planets mass
        if planet.__class__.__name__ == "MainSequenceStar" or planet.__class__.__name__ == "Planet":
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
    mytext = my_font.render("x 10^24 kg", True, (0, 0, 0))
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
        #but hide with asterisks
        textToDisplay = ""
        for i in range(len(passwordText)):
            textToDisplay += "*"
        mytext = my_font.render(textToDisplay, True, (0, 0, 0))
        screen.blit(mytext, (575+5,600+30))
    #draw text onto buttons
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    my_font = pygame.font.SysFont('Times new roman', 50)
    mytext = my_font.render("Sign in", True, (0,0,0))
    screen.blit(mytext, (725,815))

#below is the function to check whether a user with a certain username has already been registered within tht account system or not
def checkUserExists():
    #conect to the database
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    #create point of interaction
    cur = con.cursor()
    #selects usernames from the acccounts table where username is a parameter ? to be passed in with the execute
    search_query = ("""SELECT username
                    FROM accounts                           
                    WHERE username = ?""")
    #execute command with parameter
    result = cur.execute(search_query, (usernameText,))
    #error catching statement will try to fetch the username it is looking for by the parameter, if this fails
    try:
        result.fetchone()[0]
        #close database connection
        con.close()
    #then we know that username doesnt exist
    except:
        return False
    #otherwise, it does
    else:
        return True

#function while logging in, checks if the password matches what is in the database when hashed to authenticate password
def checkpassword():
    #connect to database
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    #object to interact with database
    cur = con.cursor()
    #returns the password from the accounts table where the username parameter is the one you are authenticatingg for
    search_query = ("""SELECT password
                        FROM accounts                           
                        WHERE username = ?""")
    #result holds the hashed value of the current users password
    result = cur.execute(search_query, (usernameText,))

    dbPassword = result.fetchone()[0]
    con.close()
    #check if the hash of the value they input is the same as the stored password for that account in db
    if hashingAlgorithm(passwordText) == int(dbPassword):
        #they can log in
        return True
    else:
        #they cannot
        return False

#checks the account type of the user to see if they are a teacher and should be prompted for a security question
def checkIfTeacher():
    #open database and create object to interact
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    #select account type from accounts table where username parameter is the username they put in
    search_query = ("""SELECT accountType
                        FROM accounts                           
                        WHERE username = ?""")
    #execute and pass their username as a parameter
    result = cur.execute(search_query, (usernameText,))
    try:
        #attempt to fetch their account type
        fetchedAccountType = result.fetchone()[0]
        con.close()
    except:
        #error catching/handling
        return "None"
    else:
        #if account type is T(teacher) then return true and they get a security question
        if fetchedAccountType == "T":
            return True
        else:
        #otherwise they can just log in
            return False
    
    
#renders the screen for the verification of their security question for logging in
def securityverifyscreen():
    #renders all the text to the screen
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Answer Security Question", True, (180,167,214))
    screen.blit(mytext, (360,100))
    my_font = pygame.font.SysFont('Times new roman', 75)
    mytext = my_font.render("Question", True, (217, 234, 211))
    screen.blit(mytext, (850,350))

    #creates button objects
    securityBtn = Button(screen, [300,400,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    backBtn = Button(screen, [575,910,450,20])
    signInBtn = Button(screen, [575,800,450,90])
    #puts them in an array to hold
    activeBtns = [securityBtn, signInBtn, backBtn]
    #loop through the active buttons for the security question verify screens to render them all individually
    for btn in activeBtns:
        btn.render(screen, btn.position)
    
    #displays text to tell them where to put in their answer directly on the input box
    my_font = pygame.font.SysFont('Times new roman', 30)
    #if they havent entered anything yet to actually verify
    if securityText == "":
        mytext = my_font.render("input answer here", True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))
    #otherwise it will just render the text they have entered to verify their question on top of it
    else:
        mytext = my_font.render(securityText, True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))

    #renders text onto back button
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    my_font = pygame.font.SysFont('Times new roman', 50)

#create connection to database and object to interact
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    #select the specific question from the question database that corresponds to the questionID of the question
    #the user picked as their question when making an account and displays this question
    search_query = ("""SELECT question
                        FROM accounts, securityQuestions                           
                        WHERE accounts.questionID = securityQuestions.questionID
                        AND username = ?""")
    #execute with username as a parameter
    result = cur.execute(search_query, (usernameText,))
    #and then fetch the question it has found
    securityQuestion = result.fetchone()[0]
    #close connection
    con.close()
    #render "question:" and then the security question of their account onto the screen so they know what to answer
    my_font = pygame.font.SysFont('Times new roman', 30)
    mytext = my_font.render("Question: " + str(securityQuestion), True, (133,143,146))
    screen.blit(mytext, (850,575))

    #and finally just the button to confirm verification has been entered
    mytext = my_font.render("Verify account", True, (0,0,0))
    screen.blit(mytext, (710,835))           

#like other verifies and especially the password one, this checks that the database has the same hashed value for the security question 
#as what hte user put in
def verifySecurityInput():
    #create database and object to interact
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    #this returns the answer to the question (which appears as an integer because its a hashed value) where the username is what they typed
    search_query = ("""SELECT questionanswer
                        FROM accounts                           
                        WHERE username = ?""")
    #pass in typed username as parameter
    result = cur.execute(search_query, (usernameText,))
    #then stores that answer in a variable
    dbSecurity = result.fetchone()[0]
    #checks whether the hashed value of the one they entered is conistent to the database one 
    if hashingAlgorithm(securityText) == int(dbSecurity):
        #if it is then it confirms true
        return True
    else:
        #if not then returns false and program deals with it 
        return False    

#rendering and drawing of signup screen
def signUpScreen():
    #render text
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Sign up", True, (180,167,214))
    screen.blit(mytext, (650,100))
    my_font = pygame.font.SysFont('Times new roman', 75)
    mytext = my_font.render("Account Type", True, (217, 234, 211))
    screen.blit(mytext, (890,350))
    #create button objects
    usernameBtn = Button(screen, [300,400,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    passwordBtn = Button(screen, [300,600,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    studentBtn = Button(screen, [850,450,200,90], btncolour=(255,242,204), btncolourdark=(223, 210, 171))
    teacherBtn = Button(screen, [1150,450,200,90], btncolour=(234,209,220), btncolourdark=(206, 183, 193))
    backBtn = Button(screen, [575,910,450,20])
    signInBtn = Button(screen, [575,800,450,90])
    #store active buttons in an array
    activeBtns = [usernameBtn, passwordBtn, teacherBtn, studentBtn, signInBtn, backBtn]
    #iterate through array and just render all of them
    for btn in activeBtns:
        btn.render(screen, btn.position)

    #shows them where they can type in a username and password
    my_font = pygame.font.SysFont('Times new roman', 30)
    #if blank, tell them they can input password in this field
    if usernameText == "":
        mytext = my_font.render("input username here", True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))
    else:
        #update screen to what they are typing in if not
        mytext = my_font.render(usernameText, True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))
    #if blank then say they can input password in this field
    if passwordText == "":
        mytext = my_font.render("input password here", True, (0, 0, 0))
        screen.blit(mytext, (300+5,600+30))
    else:
        #update screen to what they are typing in if not
        textToDisplay = ""
        for i in range(len(passwordText)):
            textToDisplay += "*"
        mytext = my_font.render(textToDisplay, True, (0, 0, 0))
        screen.blit(mytext, (300+5,600+30))
    #render text on buttons
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    mytext = my_font.render("Student", True, (0, 0, 0))
    screen.blit(mytext, (900,450+30))
    mytext = my_font.render("Teacher", True, (0, 0, 0))
    screen.blit(mytext, (1200,450+30))
    my_font = pygame.font.SysFont('Times new roman', 50)
    #displays the teacher and student buttons as a brighter colour if they are currently selected
    if accountType == "Teacher":
        colour = (206, 183, 193)
    elif accountType == "Student":
        colour = (223, 210, 171)
    else:
        colour = (133,143,146)
    #take the account type they currently have on and display it to them
    mytext = my_font.render("Account type: " + accountType, True, (colour))
    screen.blit(mytext, (850,575))
    #renders create account button
    mytext = my_font.render("Create account", True, (0,0,0))
    screen.blit(mytext, (650,815))   
    
#handles rendering/management of security question screen, as in making one
def securityQuestionScreen():
    #render text
    my_font = pygame.font.SysFont('Times new roman', 100)
    mytext = my_font.render("Create Security Question", True, (180,167,214))
    screen.blit(mytext, (360,100))
    my_font = pygame.font.SysFont('Times new roman', 75)
    mytext = my_font.render("Question", True, (217, 234, 211))
    screen.blit(mytext, (890,350))

    #create button objects for all buttons
    securityBtn = Button(screen, [300,400,450,90], btncolour=(255,255,255), btncolourdark=(235, 235, 235))
    firstBtn = Button(screen, [850,450,100,90], btncolour=(255,242,244), btncolourdark=(206, 183, 213))
    secondBtn = Button(screen, [1025,450,100,90], btncolour=(255,242,204), btncolourdark=(223, 210, 171))
    thirdBtn = Button(screen, [1200,450,100,90], btncolour=(234,209,220), btncolourdark=(206, 183, 193))
    backBtn = Button(screen, [575,910,450,20])
    signInBtn = Button(screen, [575,800,450,90])
    #append all objects to an array so i can work on them
    activeBtns = [securityBtn, firstBtn, secondBtn, thirdBtn, signInBtn, backBtn]
    #iterates through array to place all of them on the screen
    for btn in activeBtns:
        btn.render(screen, btn.position)
    my_font = pygame.font.SysFont('Times new roman', 30)
    #if they havent typd anything here for user say they can
    if securityText == "":
        mytext = my_font.render("input answer here", True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))
    else:
        #if they have, show them the amount of asterisks that corresponds to the length of the password
        textToDisplay = ""
        mytext = my_font.render(securityText, True, (0, 0, 0))
        screen.blit(mytext, (300+5,400+30))

    #render buttons they can click to display different security questions as a part of account creation
    mytext = my_font.render("Back", True, (0,0,0))
    screen.blit(mytext, (767,905))
    mytext = my_font.render("1", True, (0, 0, 0))
    screen.blit(mytext, (890,450+30))
    mytext = my_font.render("2", True, (0, 0, 0))
    screen.blit(mytext, (1065,450+30))
    mytext = my_font.render("3", True, (0, 0, 0))
    screen.blit(mytext, (1240,450+30))

    my_font = pygame.font.SysFont('Times new roman', 50)
# connect to database and initialise cursor object to interact
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()

#if there is a security question id (student accounts dont have one)
    if securityQuestionID != "":
        #execute this which returns the security question in text using the parameter of the securityquestion ID they selected
        result = cur.execute("""
                    SELECT question
                    FROM securityQuestions
                    WHERE questionID = ?
                    """, (securityQuestionID,))
        #returns a tuple so fetch the result and have it as a string
        securityQuestion = result.fetchone()[0]
    else:
        #otherwise there will not be a security question to render
        securityQuestion = ""
    #close connection
    con.close()
    my_font = pygame.font.SysFont('Times new roman', 30)
    #this will render the security question they have selected onto the page as a result of working with the database
    mytext = my_font.render("Question: " + str(securityQuestion), True, (133,143,146))
    screen.blit(mytext, (850,575))

#render text to create account button
    mytext = my_font.render("Create account", True, (0,0,0))
    screen.blit(mytext, (650,815)) 

#simple hashing algorithm where the input is taken through a series of operations to produce an index at the end
def hashingAlgorithm(textToHash):
    #sets character values list to 0, important because we are going to convert all the ascii values of the entered string 
    charValueList = []
    for i in range(len(textToHash)):
        #converts letters all to ascii values and puts them in a list
        charValueList.append(ord(textToHash[i]))
        #sets the total value of the characters to 0
    totalValue = 0
    #for every character ascii value in the list, it will perform some certain operations on it before adding it to the total
    for i in range(len(charValueList)):
        #every fourth character gets 20 added to it
        if i % 4 == 0:
            charValueList[i] += 20
        #every 3rd character gets 1 taken away
        elif i % 3 == 0:
            charValueList[i] -= 1
        #every second character is doubled
        elif i % 2 == 0:
            charValueList[i] *= 2
        #every character past that just gets 67 added to it
        elif i % 1 == 0:
            charValueList[i] += 67
        #otherwise 4 gets taken away (logically impossible since all will fit into one if they dont in any others)
        else:
            charValueList[i] -= 4
        totalValue += (charValueList[i]+1)
    #return this random index so that it can be saved / compared
    return totalValue

#handles creation of a new account within the database. using sql insert commands
def newAccountDB():
    con = sqlite3.connect(r"C:\Users\alanj\Downloads\NEA\simulatorDB.db")
    cur = con.cursor()
    #select all fields from accounts and order by ID descending
    result = cur.execute("""
                    SELECT *
                    FROM accounts
                    ORDER BY accountID DESC;
                        """)
    #make sure program keeps track of hte new accounts id by adding one to the id field of hte first qsult
    g = int(result.fetchone()[0]) + 1
    #if account type is student then blank the questionid and the text hash fields
    if accountType != "Teacher":
        securityQuestionID = ""
        securityTextHash = ""
    #if it is teacher, then we setup the value to be put in the security text hash field for 2fa
    else:
        securityTextHash = hashingAlgorithm(securityText)
        #securityQuestionID <-
        securityQuestionID = 1
    #insert data query, passes 6 parameters into the account creation process for the fields
    insert_data_query = """
    INSERT INTO accounts VALUES(?, ?, ?, ?, ?, ?);
    """
    #uesrid, username, password-hash, account type, security-hash, questionid
    cur.execute(insert_data_query, (str(g), usernameText, str(hashingAlgorithm(passwordText)), accountType[0],  str(securityTextHash), str(securityQuestionID),))
    #commit makes sure its saved to the database
    con.commit()
    
    #update the other table to ensure it can stay consistent, passing one parameter
    insert_data_query = """
    INSERT INTO accountstats VALUES(?, 0, 0);
    """
    #executes insert with the account id for a parameter
    cur.execute(insert_data_query, (str(g),))
    con.commit()
    #important to commit then close
    con.close()

#handles the code part of saving the simulator and writing to a text file for this               
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

#code part of loading a simulation from file, and all its properties for each planets, converting in the process
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
                                
#my button class to render and perform various actions with buttons
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
    #renders the button depending on if its hovered over or not
    def render(self, surface, position):
        #if hovered over then changes to a light
        if self.x <= mouse[0] <= self.x+self.width and self.y <= mouse[1] <= self.y+self.height:
            pygame.draw.rect(screen,self.colour,self.position)
        #usually just remains a darker colour
        else:
            pygame.draw.rect(screen,self.colourdark,self.position)

#class for planets, this will be used for various calculations and attributes
class Planet:
    def __init__(self, position, radius, colour, speed, angle, angleincrement, mass):
        self.position = position
        self.radius = radius
        self.speed = speed
        self.angle = angle
        self.colour = colour
        self.angleincrement = angleincrement
        self.mass = mass
    #test movement function
    def move(self):
        self.position = (self.position[0]+5, self.position[1])
    #function to increment the angle of an object for testing
    def incrementangle(self):
        self.angle = self.angle + self.angleincrement
    #this one is used, it will scale the radius of the planet to be proportional to the mass of it and increase size
    def determineradius(self):
        #current formula
        self.radius = 10 + self.mass * 0.5

    #this method changes the position of the object depending on its speed and angle
    def anglemove(self):
        self.angle %= 360
        self.position = (self.position[0]+self.speed*math.sin(math.radians(self.angle)), self.position[1]-self.speed*math.cos(math.radians(self.angle)))

#this function calculates the force it experiences as a result of another planet and calculates what the new speed and angle should be when combined
    def movevectors(self, otherBody):
        #calculate the distances in pixels
        dx = otherBody.position[0] - self.position[0]
        dy = otherBody.position[1] - self.position[1]
        #get distances squared and then root it to get one distance vector
        distanceSquared = dx ** 2 + dy ** 2
        distance = math.sqrt(dx**2+dy**2)
        # f = Gm1m2/r^2 to calculate the force experienced by one body by the gravitational pull of another
        force = 0.0001*0.00000000006674 * self.mass* 100000000 * otherBody.mass * 100000000 / distanceSquared


        # f = ma rearranged to a = f/m
        acceleration = force / self.mass

    #calculates the current speed in its vectory componet forms
        speed = (self.speed * math.sin(math.radians(self.angle)), -self.speed * math.cos(math.radians(self.angle)))
        #this calculates a scale factor to use for calculations
        scaleFactor = acceleration / distance
        #and then converts the currently worked forces into speed vectors
        changeVelocityVectors = (scaleFactor * dx, scaleFactor * dy)        
        #adds velocities to get one overall velocity
        speed = (speed[0] + changeVelocityVectors[0], speed[1] + changeVelocityVectors[1])
        #magnitude of motion
        self.speed = math.sqrt(speed[0]**2+speed[1]**2)
        #direction by the tan function (we have x and y components)
        self.angle = math.degrees(math.atan2(speed[0],-speed[1]))

        
        
            

#render the planet
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)
    #keep a track of if the planet has been clicked to open up a menu
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

class Protostar(Planet):
    def __init__(self, position, radius, colour, speed, angle, angleincrement, mass, temperature):
        super().__init__(position, radius, colour, speed, angle, angleincrement, mass)
        self.temperature = temperature
        self.colour = (100,100,100)
        self.radius = 30 + self.mass * 0.1
        for i in range(20):
            planet = Planet((self.position[0]+ random.randint(-250,250), self.position[1]+ random.randint(-250,250),), 5, (100,100,100), 0, 90, 1, 0.1)
            placedobjects.append(planet)
    def incrementRadius(self, multiplier=1):
        self.radius += (0.05 * multiplier)
    def incrementTemperature(self):
        self.temperature += 10000
    

class MainSequenceStar(Planet):
    def __init__(self, position, radius, colour, speed, angle, angleincrement, mass, temperature):
        super().__init__(position, radius, colour, speed, angle, angleincrement, mass)
        self.temperature = temperature
    def determineradius(self,):
        #current formula
        self.radius = 50 + self.mass * 0.1
    def determineSpectralClass(self):
        stemperature = 5740*((self.mass/20) ** 0.54)
        if stemperature < 2500:
            self.colour = (159,82,81)
        elif stemperature < 3500:
            self.colour = (254,3,0)
        elif stemperature < 5000:
            self.colour = (253,102,0)
        elif stemperature < 6000:
            self.colour = (254,255,0)
        elif stemperature < 7500:
            self.colour = (246,152,157)            
        elif stemperature < 11000:
            self.colour = (249,249,249)            
        elif stemperature < 25000:
            self.colour = (151,204,253)      
        else:
            self.colour = (2,113,194)
    def incrementTemperature(self):
        self.temperature += 85000

class RedGiant(Planet):
    def __init__(self, position, radius, colour, speed, angle, angleincrement, mass, temperature):
        super().__init__(position, radius, colour, speed, angle, angleincrement, mass)
        self.temperature = temperature
        self.colour = (254,3,0)
        self.radius = 50 + self.mass * 0.1
    def incrementRadius(self, multiplier=1):
        self.radius += (0.05 * multiplier)
        
    def incrementTemperature(self):
        self.temperature += 200000



class DwarfStar(Planet):
    def __init__(self, position, radius, colour, speed, angle, angleincrement, mass, temperature):
        super().__init__(position, radius, colour, speed, angle, angleincrement, mass)
        self.temperature = temperature
        self.colour = (202,206,255)
        self.radius = 10 + self.mass * 0.1
    def determineRadius(self):
        #current formula
        self.radius = 10 + self.mass * 0.1
    def incrementTemperature(self):
        self.temperature -= 300000
    def determineColour(self):
        colourscale = self.temperature / 300000000
        if colourscale > 1:
            colourscale = 1
        elif colourscale < 0:
            colourscale = 0
        self.colour = ((colourscale * 255)//1, (colourscale * 255)//1, (colourscale * 255)//1)
    def incrementRadius(self):
      self.radius += 0.5

class NeutronStar(Planet):
    def __init__(self, position, radius, colour, speed, angle, angleincrement, mass, temperature):
        super().__init__(position, radius, colour, speed, angle, angleincrement, mass)
        self.temperature = temperature
        self.colour = (202,206,255)
        self.radius = 10 + self.mass * 0.1
        loopvalues = [[0,-25],[25,-25],[25,0],[25,25],[0,25],[-25,25],[-25,0],[-25,-25]]
        for i in range(8):
            planet = Planet((self.position[0] + loopvalues[i][0], self.position[1] + loopvalues[i][1],), 5, (100,100,100), 17, 45*i, 1, 0.1)
            placedobjects.append(planet)
            
    def determineradius(self):
        #current formula
        self.radius = 50 + self.mass * 0.1
    def incrementTemperature(self):
        self.temperature += 200000
    def incrementRadius(self):
      self.radius += 0.5

class BlackHole(Planet):
    def __init__(self, position, radius, colour, speed, angle, angleincrement, mass, temperature):
        super().__init__(position, radius, colour, speed, angle, angleincrement, mass)
        self.temperature = temperature
        self.colour = (45, 36, 105)
        self.radius = 4 + self.mass * 0.
        loopvalues = [[0,-25],[25,-25],[25,0],[25,25],[0,25],[-25,25],[-25,0],[-25,-25]]
        for i in range(8):
            planet = Planet((self.position[0] + loopvalues[i][0], self.position[1] + loopvalues[i][1],), 5, (100,100,100), 17, 45*i, 1, 0.1)
            placedobjects.append(planet)
    def determineradius(self):
        #current formula
        self.radius = 4 + self.mass * 0.001
    def incrementTemperature(self):
        self.temperature += 200000
    def incrementRadius(self):
      self.radius += 0.5

#1600x950
#initialise pygame and window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
resetScreen()




#load music
mixer.init()
mixer.music.load(r"C:\Users\alanj\Downloads\NEA\above_story.ogg")
mixer.music.set_volume(1)
mixer.music.play(1)

#sets up pygame events
while True:
     
    for event in pygame.event.get():

        mouse = pygame.mouse.get_pos()
        #if pygame quits, exit pygame and the execution of the program to prevent throwing an error
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
                        print("user fale")

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

                #important one, this is for the object menu and displaying what they type as a part of the simulation
                elif mouse[0]<1100 and objectMenuAppear == True:
                    objectMenuAppear = False
                    placedobjects[checkedplanet].mass = float(enterMass)
                    placedobjects[checkedplanet].angle = float(enterAngle)
                    placedobjects[checkedplanet].speed = float(enterSpeed)                 
                #if they click outside of the object menu on a planet then opens the objectmenu by setting it to appear
                elif not planetcreate and not starcreate and playing == False and objectMenuAppear == False and mouse[1] < 850:
                    for checkedplanet in range(len(placedobjects)):
                        if placedobjects[checkedplanet].checkclick():
                            enterMass = placedobjects[checkedplanet].mass
                            enterAngle = placedobjects[checkedplanet].angle
                            enterSpeed = placedobjects[checkedplanet].speed
                            objectMenuAppear = True
                            break

                elif 600 <= mouse[0] <= 600+250 and 850 <= mouse[1] <= 850+100:
                    #clicking on any save file slots will save it to said slot
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
                        #display that it saved to a file for half a second and dissapear
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
                    planet = Planet(mouse, 15, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 5, 90, 1, 5)
                    placedobjects.append(planet)
                elif starcreate:
                    star = Protostar(mouse, 15, (20,20,20), 0, 0, 0, 100,0)    
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
                elif 1100 <= mouse[0] <= 1100+500 and 850 <= mouse[1] <= 850+100 and objectMenuAppear == False:
                    playing = False
                    enteringSimSpeed = True
                    enterSimSpeed = str(simSpeed)
                
                if  not 1100 <= mouse[0] <= 1100+500 and  not 850 <= mouse[1] <= 850+100:
                    enteringSimSpeed = False
                    try:
                        enterSimSpeed = float(enterSimSpeed)
                    except:
                        simSpeed = 1
                    else:
                        if enterSimSpeed < 0:
                            simSpeed = 0
                        elif enterSimSpeed > 100 :
                            simSpeed = 100
                        else:
                            simSpeed = enterSimSpeed
                    enterSimSpeed = str(simSpeed)
                    

                    
                #checkwhatthehell

                if objectMenuAppear == True:
                    if 1200 <= mouse[0] <= 1200+200 and 250 <= mouse[1] <= 250+50:
                        enterMass = str(placedobjects[checkedplanet].mass)
                        enteringMass = True
                    elif enteringMass == True:
                    # putting it to 0 could be an alright idea, and good it works, just put some thought to mass
                        try:
                            placedobjects[checkedplanet].mass = float(enterMass)#
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
                    #how i add text to my username and password strings
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
            if enterSimSpeed == True:
                if event.key == pygame.K_BACKSPACE:
                    enterSimSpeed = enterSimSpeed[:-1]
                else:
                    enterSimSpeed += event.unicode

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
                            if placedobjects[j].__class__.__name__ == "Planet":
                                placedobjects[i].mergeBodies(placedobjects[j])
                                placedobjects.pop(j)
                                collisionFound = True
                                break
                        placedobjects[i].movevectors(placedobjects[j]) 
                if collisionFound: 
                    break
                if placedobjects[j].__class__.__name__ == "Protostar":
                    placedobjects[j].incrementTemperature()
                    if placedobjects[j].temperature >= 10000000:
                        star = MainSequenceStar(placedobjects[j].position, placedobjects[j].radius, placedobjects[j].colour, placedobjects[j].speed, placedobjects[j].angle,  placedobjects[j].angleincrement, placedobjects[j].mass, placedobjects[j].temperature)    
                        placedobjects.append(star)
                        placedobjects.pop(j)

                elif placedobjects[j].__class__.__name__ == "MainSequenceStar":
                    placedobjects[j].determineSpectralClass()
                    placedobjects[j].incrementTemperature()
                    if placedobjects[j].temperature >= 100000000:
                        star = RedGiant(placedobjects[j].position, placedobjects[j].radius, placedobjects[j].colour, placedobjects[j].speed, placedobjects[j].angle,  placedobjects[j].angleincrement, placedobjects[j].mass, placedobjects[j].temperature)    
                        placedobjects.append(star)
                        placedobjects.pop(j)
                elif placedobjects[j].__class__.__name__ == "RedGiant":
                    placedobjects[j].incrementTemperature()
                    placedobjects[j].incrementRadius()
                    
                    if placedobjects[j].temperature >= 300000000 and placedobjects[j].mass < (1.4*20):
                        placedobjects[j].incrementRadius(80)
                        if placedobjects[j].radius >= 400:
                            star = DwarfStar(placedobjects[j].position, placedobjects[j].radius, placedobjects[j].colour, placedobjects[j].speed, placedobjects[j].angle,  placedobjects[j].angleincrement, placedobjects[j].mass, placedobjects[j].temperature)    
                            placedobjects.append(star)
                            placedobjects.pop(j)
                    elif placedobjects[j].temperature >= 800000000 and placedobjects[j].mass >= (1.4*20):
                        if placedobjects[j].colour == (255,255,255):
                            placedobjects[j].incrementRadius(500)
                        else:                            
                            placedobjects[j].incrementRadius(-8)
                        if placedobjects[j].radius <= 0.5:
                            placedobjects[j].colour = (255,255,255)
                        if placedobjects[j].radius >= 1500:
                            if placedobjects[j].mass < (3*20):
                                star = NeutronStar(placedobjects[j].position, placedobjects[j].radius, placedobjects[j].colour, placedobjects[j].speed, placedobjects[j].angle,  placedobjects[j].angleincrement, placedobjects[j].mass, placedobjects[j].temperature)    
                            elif placedobjects[j].mass >= (3*20):
                                star = BlackHole(placedobjects[j].position, placedobjects[j].radius, placedobjects[j].colour, placedobjects[j].speed, placedobjects[j].angle,  placedobjects[j].angleincrement, placedobjects[j].mass, placedobjects[j].temperature)                           
                            placedobjects.append(star)
                            placedobjects.pop(j)
                elif placedobjects[j].__class__.__name__ == "DwarfStar":
                    placedobjects[j].determineRadius()
                    placedobjects[j].incrementTemperature()
                    placedobjects[j].determineColour()
 
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
