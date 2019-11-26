import pygame, sys
import random
import math

# window size
WIDTH = 600
HEIGHT = 600

# variables
x_pos = 120
y_pos = 280
length = 3
running = True
tail = []
direction = 'RIGHT'
foodSize = 20
snakeBlockSize = 35
gridBlock = 40
score = length
foodPos = (200, 200)
foodOnMap = False

# creates list of possible positions of food
# consists of values of products in "40 gangern"
possiblePos = [x for x in range(0, WIDTH-gridBlock) if x % gridBlock == 0]

# Frames pr second
FPS = 8

pygame.init()
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SNAKE')
#pygame.font.init()

# initilize text
fontBig = pygame.font.SysFont('Comic Sans MS', 80)
fontSmall = pygame.font.SysFont('Comic Sans MS', 50)

# creates a clock
clock = pygame.time.Clock()

#create grid
""" for i in range(0, WIDTH, 40):
    for m in range(0,WIDTH, 40):
        pygame.draw.rect(canvas, (255,255,255), (i,m,snakeBlockSize,snakeBlockSize),1) """


# function to initialize snake
def initializeSnake(x, y):
    for i in range(0, length):
        tail.append({'x': x-i*40, 'y': y})
        pygame.draw.rect(canvas, (255, 255, 255),(tail[i]['x'], tail[i]['y'], snakeBlockSize, snakeBlockSize))

# initialize snake at start position
initializeSnake(x_pos, y_pos)


# function to create food
def createFood():
    global foodOnMap
    global foodPos
    global possiblePos

    # update scoretext
    scoreTxt = fontBig.render(str(score), False, (255, 255, 255))
    canvas.blit(scoreTxt, (10, 10))

    # if no food on screen, make new food
    if not foodOnMap:
        #create foodposition in center of each grid block 40x40 
        foodPos = (random.choice(possiblePos)+(snakeBlockSize -foodSize)/2,
                    random.choice(possiblePos)+(snakeBlockSize-foodSize)/2)
        foodOnMap = True
    pygame.draw.rect(canvas, (255, 0, 0),
                     (foodPos[0], foodPos[1], foodSize, foodSize))


# function to be called if snake eats food
def eatFood():
    global score
    global length
    global foodOnMap

    foodOnMap = False
    score += 1
    length += 1

    # add block to snake
    tail.append({'x': tail[-1]['x'], 'y': tail[-1]['y']})

# create snake
def drawSnake(dir):
    global x_pos
    global y_pos
    global gridBlock

    # draw background color to blank the screen
    canvas.fill((0, 0, 0))

    # create new food
    createFood()

    if (dir == 'LEFT'):
        x_pos -= gridBlock
        tail.insert(0, {'x': x_pos, 'y': y_pos})
        tail.pop()
    elif (dir == 'RIGHT'):
        x_pos += gridBlock
        tail.insert(0, {'x': x_pos, 'y': y_pos})
        tail.pop()
    elif (dir == 'UP'):
        y_pos -= gridBlock
        tail.insert(0, {'x': x_pos, 'y': y_pos})
        tail.pop()
    elif (dir == 'DOWN'):
        y_pos += gridBlock
        tail.insert(0, {'x': x_pos, 'y': y_pos})
        tail.pop()

    for i in range(0, length):
        pygame.draw.rect(canvas, (255, 255, 255),
                         (tail[i]['x'], tail[i]['y'], snakeBlockSize, snakeBlockSize))
        
        # skip first block of the snake
        if i == 0:
            continue

        # check if snake collides with tail
        if (collide(tail[0]['x'], tail[i]['x'], tail[0]['y'], tail[i]['y'], snakeBlockSize, snakeBlockSize, snakeBlockSize, snakeBlockSize)):
            quitGame()

    # check if snake collides with food
    if (collide(tail[0]['x'], foodPos[0], tail[0]['y'], foodPos[1], snakeBlockSize, foodSize, snakeBlockSize, foodSize)):
        eatFood()

    # check if snake collides with walls
    if (tail[0]['x'] >= WIDTH-snakeBlockSize or tail[0]['x'] <= 0 or tail[0]['y'] >= HEIGHT-snakeBlockSize or tail[0]['y'] <= 0):
        quitGame()

   
# function to quit and pause game
def quitGame():
    global running
    
    # display game over text
    quitText = fontBig.render('Game over', False, (255, 0, 0))
    scoreTxt = fontSmall.render('Score: ' + str(score), False, (255, 0, 0))
    canvas.blit(quitText, (WIDTH/2 - quitText.get_rect().width/2, HEIGHT/2-60))
    canvas.blit(scoreTxt, (WIDTH/2 - scoreTxt.get_rect().width/2, HEIGHT/2+20))

    running = False

# function to check if two objects collide
# returns boolean
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if (x1+w1 > x2 and x1 < x2+w2 and y1+h1 > y2 and y1 < y2+h2):
        return True
    else:
        return False

# function to reset game
def resetGame():
    global running
    global tail
    global score
    global length
    global x_pos
    global y_pos
    global direction
    global foodOnMap

    # draw background color to blank the screen
    canvas.fill((0, 0, 0))

    # reset variables
    tail = []
    foodOnMap = False
    length = 3
    score = length
    x_pos = 120
    y_pos = 280
    direction = 'RIGHT'

    # initialize snake at start position
    initializeSnake(x_pos, y_pos)

    running = True

# function to pause game
def pauseGame():
    global running

    running = False
    pauseTxt = fontBig.render('PAUSED', False, (255, 255, 255))
    canvas.blit(pauseTxt, (WIDTH/2 - pauseTxt.get_rect().width/2, HEIGHT/2))

# function to resume game
def resumeGame():
    global running
    running = True
    

# game loop
while True:
    # if game is running
    if running:
        clock.tick(FPS)
        # draw new snake for every fps
        drawSnake(direction)

        # listen for key events
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if (e.key == pygame.K_LEFT and direction != 'RIGHT'):
                    direction = 'LEFT'
                elif (e.key == pygame.K_RIGHT and direction != 'LEFT'):
                    direction = 'RIGHT'
                elif (e.key == pygame.K_UP and direction != 'DOWN'):
                    direction = 'UP'
                elif (e.key == pygame.K_DOWN and direction != 'UP'):
                    direction = 'DOWN'
                elif (e.key == pygame.K_p):
                    pauseGame()

            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # game is not running, freeze game
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN):
                    resetGame()
                elif (e.key == pygame.K_p):
                    resumeGame()
            if event.type == pygame.QUIT:
                pygame.quit()

    pygame.display.flip()
