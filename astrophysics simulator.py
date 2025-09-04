import pygame
import time
from pygame import mixer
pygame.init()
background_colour = (138, 194, 212) 
screen = pygame.display.set_mode((1600,1000))


pygame.display.set_caption('Simulator')
screen.fill((180,167,214))
def createbtn():
    button = pygame.Rect(600,400,450,90)
    font = pygame.font.SysFont('Times new roman', 75)
    surf = font.render('Sign up', True, (0,0,0))
    a,b = pygame.mouse.get_pos()
    if button.x <= a <= button.x + 450 and button.y <= b <= button.y + 90:
        pygame.draw.rect(screen,(208,224,227),button)
        screen.blit(surf,(button.x+5, button.y+5))
    else:
        pygame.draw.rect(screen,(208,224,227),button)
        screen.blit(surf,(button.x+5, button.y+5))
    
    


my_font = pygame.font.SysFont('Times new roman', 100)
mytext = my_font.render("something about something", True, (0, 0, 0))
screen.blit(mytext, (300,100))
pygame.display.update()

mixer.init()
mixer.music.load(r"\\FS\ajubb7tq\downloads\NEA\joy_of_remembrance.ogg")
mixer.music.set_volume(0.5)
mixer.music.play(1)




#pygame.draw.rect(screen,(208,224,227), (600,400, 450, 90))
pygame.draw.rect(screen,(208,224,227), (600,600, 450, 90))
pygame.draw.rect(screen,(208,224,227), (600,800, 450, 90))

pygame.display.update()

while True:
    for event in pygame.event.get():
        createbtn()
        pygame.display.update()
