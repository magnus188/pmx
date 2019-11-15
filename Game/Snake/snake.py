import pygame
import random


# RULES:
# ikke bite seg selv
# ikke kræsj i veggen

x_pos = 100
y_pos = 300
length = 3
speed = 0.5
running = True
tail = []
direction = 'RIGHT'
foodSize = 20
snakeBlockSize = 35
score = length
foodPos = (200,200)
foodOnMap = False

#Frames pr second
FPS=8

#window size
WIDTH=600
HEIGHT=600

pygame.init()
canvas = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SNAKE')

# creates a clock
clock=pygame.time.Clock()

# initialize snake
for i in range(0,length):
    tail.append({'x': x_pos-i*40, 'y': y_pos})
    pygame.draw.rect(canvas, (255,255,255), (tail[i]['x'],tail[i]['y'],snakeBlockSize, snakeBlockSize))

def createFood():
    global foodOnMap
    global foodPos

    if not foodOnMap:
        foodPos = (random.randint(0,WIDTH-foodSize), random.randint(0,HEIGHT-foodSize))
        foodOnMap = True
    pygame.draw.rect(canvas, (255,255,255), (foodPos[0],foodPos[1],foodSize, foodSize))

def eatFood():
    global score
    global length
    global foodOnMap

    foodOnMap = False
    score += 1
    length += 1

    tail.append({'x': tail[-1]['x'], 'y': tail[-1]['y']})

# create snake
def drawSnake(dir):
    global x_pos
    global y_pos
    #draw background color to blank the screen
    canvas.fill((0,0,0))
    createFood()

    if (dir == 'LEFT'):
        x_pos -= 40
        tail.insert(0,{'x': x_pos, 'y': y_pos})
        tail.pop()
    elif (dir == 'RIGHT'):
        x_pos += 40
        tail.insert(0,{'x': x_pos, 'y': y_pos})
        tail.pop()
    elif (dir == 'UP'):
        y_pos -= 40
        tail.insert(0,{'x': x_pos, 'y': y_pos})
        tail.pop()
    elif (dir == 'DOWN'):
        y_pos += 40
        tail.insert(0,{'x': x_pos, 'y': y_pos})
        tail.pop()

    for i in range(0,length):
       pygame.draw.rect(canvas, (255,255,255), (tail[i]['x'],tail[i]['y'],snakeBlockSize, snakeBlockSize))
    
    # check if snake collides with food
    if (collide(tail[0]['x'], foodPos[0], tail[0]['y'], foodPos[1], snakeBlockSize, foodSize, snakeBlockSize, foodSize)):
        eatFood()

    # check if snake collides with walls
    if (tail[0]['x'] == WIDTH-snakeBlockSize or tail[0]['x'] == 0 or tail[0]['y'] == HEIGHT-snakeBlockSize or tail[0]['y'] == 0):
        quitGame()

def quitGame():
    length = 3
    print('U die')
    running = False
    #TODO: Show menu

#check if two elements collide
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if (x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2):return True
	else:return False

while True:
    if running:
        clock.tick(FPS)
        drawSnake(direction)
        for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if (e.key == pygame.K_LEFT):
                        print('Left')
                        direction = 'LEFT'
                    elif ( e.key == pygame.K_RIGHT):
                        print('Right')
                        direction = 'RIGHT'
                    elif (e.key == pygame.K_UP):
                        print('Up')
                        direction = 'UP'
                    elif (e.key == pygame.K_DOWN):
                        print('Down')
                        direction = 'DOWN'

                if e.type == pygame.QUIT:
                        pygame.quit()

        pygame.display.flip()