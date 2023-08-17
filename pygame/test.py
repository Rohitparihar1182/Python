import pygame
pygame.init()
root=pygame.display.set_mode((500,500))
pygame.display.set_caption("Hey there")
x= pygame.image.load('bg.jpg')
root.blit(x,(0,0))
pygame.display.update()
#pygame.quit()
