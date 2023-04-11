import pygame
import time
import random

pygame.init()
 
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
f=open("record.txt",'r')
record=int(f.read())
f.close()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)
GREEN=(0,255,0)
BLOCK_SIZE = 10
FPS = 10
game=True
score=0
foodw=1
FONT_STYLE = pygame.font.SysFont(None, 30)
LOSE_STYLE = pygame.font.SysFont(None, 80)
def show_score(score):

    value = FONT_STYLE.render("Your Score: " + str(score), True, YELLOW)
    window.blit(value, [0, 0])
 
c=True
def draw_snake(snake_list):
    
    for x in snake_list:
        pygame.draw.rect(window, WHITE, [x[0], x[1], 10, 10])
 
 
def generate_food():
    food_x = round(random.randrange(0, (WINDOW_WIDTH - BLOCK_SIZE) / 10.0)) * 10.0
    food_y = round(random.randrange(20, (WINDOW_HEIGHT - BLOCK_SIZE) / 10.0)) * 10.0
    return [food_x, food_y]
 
def draw_food(food_position,n):
    
    pygame.draw.rect(window, n, [food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE])
 
def loose():
    global window
    global x_change
    global y_change
    global record
    x_change = 0 
    y_change = 0
    window.fill('red')
    regame=FONT_STYLE.render("Press SPACE to restart!",True,WHITE)
    lose=LOSE_STYLE.render("GAME OVER!!!",False, WHITE)
    rerecord=FONT_STYLE.render("press R to reset the record",True,WHITE)
    window.blit(lose,[60,200])
    window.blit(regame,[140,260])
    window.blit(rerecord,[130,280])
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f=open("record.txt",'w')
                f.write(str(record))
                f.close()
                exit()
x = WINDOW_WIDTH / 2
y = WINDOW_HEIGHT / 2
 
x_change = 0
y_change = 0

food_position = generate_food()

snake_body = []
length_of_snake = 1
level=1
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")
bgsound=pygame.mixer.Sound("sounds/bg.mp3")
bite=pygame.mixer.Sound('sounds/bite.mp3')
bgsound.set_volume(0.5)
bite.set_volume(1)
bgsound.play()
clock = pygame.time.Clock()
a=pygame.USEREVENT+1
b=pygame.USEREVENT+2
pygame.time.set_timer(a,42500)
def timer():
    global b
    v=random.randint(7000,15000)
    pygame.time.set_timer(b,v)
t=False
while True:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f=open("record.txt",'w')
                f.write(str(record))
                f.close()
                exit()
            if event.type == a:
                bgsound.play()
            if event.type ==b:
                t=True
            if game:
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change!=BLOCK_SIZE:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change!=-BLOCK_SIZE:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change!=BLOCK_SIZE:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change!=-BLOCK_SIZE:
                    y_change = BLOCK_SIZE
                    x_change = 0
            if not game:
                if event.type == pygame.KEYUP:
                  if event.key== pygame.K_r:
                      c=False
                      record=0
                      f=open("record.txt",'w')
                      f.write('0')
                      f.close()
                  if event.key == pygame.K_SPACE:
                    food_position=generate_food()
                    timer()
                    window.fill(BLACK)
                    if c:
                     if score>record:
                        record=score
                    else:
                        c=True
                    snake_body=[]
                    length_of_snake=1
                    x=WINDOW_WIDTH / 2
                    y = WINDOW_HEIGHT / 2
                    level=1
                    FPS=10
                    score=0
                    foodw=1
                    bgsound.set_volume(0.5)
                    game=True
    x += x_change
    y += y_change

    window.fill(BLACK)
    record_show=FONT_STYLE.render("Record: "+str(record),True,YELLOW)
    show_score(score)
    if level<6:
      level_show=FONT_STYLE.render("LVL "+str(level),True,YELLOW)
    else:
      level_show=FONT_STYLE.render("LVL MAX!",True,YELLOW) 
    window.blit(record_show,[390,0])
    window.blit(level_show,[230,0])
    if foodw==1:
       draw_food(food_position,GREEN)
    elif foodw == 2:
       draw_food(food_position,YELLOW)
    elif foodw>=3:
        draw_food(food_position,RED)
    if t:
        food_position=generate_food()
        timer()
        t=False
    snake_head = [x, y]
    snake_body.append(snake_head)
    if len(snake_body) > length_of_snake:
        del snake_body[0]
    draw_snake( snake_body)
    pygame.draw.rect(window, WHITE, [0, 17, 500, 3])
    for block in snake_body[:-1]:
        if block == snake_head:
            game=False
            bgsound.set_volume(0.0)
            loose()
    if (x > WINDOW_WIDTH-5 or x < 0) or (y > WINDOW_HEIGHT-5 or y < 20):
        game=False
        bgsound.set_volume(0.0)
        loose()
    pygame.display.update()
    h=score//10
    if x == food_position[0] and y == food_position[1]:
        score+=foodw
        bite.play()
        length_of_snake += foodw
        
        if level<3:
            foodw=random.randint(1,level)
        else:
            foodw=random.randint(1,3)
        food_position = generate_food()
        timer()
        if score//10>h and level<6:
            FPS+=6
            level+=1
    clock.tick(FPS)