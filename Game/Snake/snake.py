import pygame
import random
import time

# RULES:
# ikke bite seg selv
# ikke kræsj i veggen


global x_pos
global y_pos
global length
global speed
global running
global tail
global direction

x_pos = 50
y_pos = 10
length = 3
speed = 0.5
running = True
tail = []
direction = 'LEFT'

# initialize snake
for i in range(0,length-1,40):
    tail.append({'x': x_pos+i, 'y': y_pos+i})

print(tail)


#Frames pr second
FPS=24

#window size
WIDTH=600
HEIGHT=600

pygame.init()
canvas = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SNAKE')

# creates a clock
clock=pygame.time.Clock()

# create snake
def drawSnake(x, y, dir):
    #draw background color to blank the screen
    canvas.fill((0,0,0))

    if (dir == 'LEFT' and dir != 'RIGHT'):
        tail.insert(0,{'x': x+40, 'y': y})
        tail.pop(-1)
    elif (dir == 'RIGHT' and dir != 'LEFT'):
        tail.insert(0,{'x': x-40, 'y': y})
        tail.pop(-1)
    elif (dir == 'UP' and dir != 'DOWN'):
        tail.insert(0,{'x': x, 'y': y+40})
        tail.pop(-1)
    elif (dir == 'DOWN' and dir != 'UP'):
        tail.insert(0,{'x': x, 'y': y-40})
        tail.pop(-1)

    for i in range(0,length-1):
        print(i)
        pygame.draw.rect(canvas, (255,255,255), (tail[i]['x'],tail[i]['y'],35,35))

def quitGame():
    length = 3
    running = False
    #TODO: Show menu

while True:
    #time.sleep (100.0 / 1000.0)
    drawSnake(x_pos, y_pos, direction)
    if running:
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