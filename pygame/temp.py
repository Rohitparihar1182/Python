import pygame
import time
#initialization
pygame.init()

#display size n title
win=pygame.display.set_mode((500,475))
pygame.display.set_caption("hiii ")

#declaring variables
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
x=20
y=200
x1=20
y1=300

clock=pygame.time.Clock()

win.blit(bg,(0,0))
pygame.display.update()

for i in range(9):
    temp=walkRight[i]
    temp2=walkLeft[i]
    win.blit(temp2,(x1,y1))
    win.blit(temp,(x,y))
    x+=30
    x1+=30
    pygame.display.update()
    
