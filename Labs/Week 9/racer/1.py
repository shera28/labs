import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
a=pygame.image.load("images/Player.png")
a=pygame.transform.scale(a,(200,200))
while True:
    #Cycles through all events occurring  
    screen.fill('black')
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            exit()
    screen.blit(a,(20,0))
    pygame.display.update()