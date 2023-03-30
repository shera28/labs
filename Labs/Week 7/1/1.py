import pygame
import datetime
pygame.init()
W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
t = datetime.datetime.now()
a=0
if t.hour%12>=3:
    a=a-(t.hour%12-3)*30-t.minute*0.5
else:
    a=a+(3-t.hour%12)*30-t.minute*0.5
b=0
if t.minute>=15:
    b=b-(t.minute-15)*6
else:
    b=b+(15-t.minute)*6
mickey = pygame.image.load("images/main-clock.png")
leftHand = pygame.image.load("images/left-hand.png") #minutes
rightHand = pygame.image.load("images/right-hand.png") #hours
mickeyRect = mickey.get_rect()
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image, new_rect)
langle = b
rangle = a
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    langle -= 0.001705
    rangle -= 0.0000284167
    
    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    
    blitRotateCenter(sc, leftHand, (x,y), langle) 
    blitRotateCenter(sc, rightHand, (x,y), rangle)
    pygame.display.update()