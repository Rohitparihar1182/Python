import pygame

pygame.init()

win=pygame.display.set_mode((500,500))
pygame.display.set_caption("First time in pygame ")

x=50
y=425
width=40
height=60
vel=5

isJump=False
jumpcount=10

run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.quit():
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x>=0:
            x-=vel
    if keys[pygame.K_RIGHT]:
        if x<=460-vel:
            x+=vel
    if isJump==False:
        if keys[pygame.K_UP]:
            if y>=0:
                y-=vel
        if keys[pygame.K_DOWN]:
            if y<440-vel:
                y+=vel
        if keys[pygame.K_SPACE]:
            isJump=True
    else:
        if jumpcount>=-10:
            neg=1
            if jumpcount<0:
                neg=-1
            y-=(jumpcount**2)*0.5*neg
            jumpcount-=1
        else:
            isJump=False
            jumpcount=10
    win.fill("green")
    pygame.draw.rect(win, ("red"),(x,y,width,height))
    pygame.display.update()
    
pygame.quit()

