import pygame
import time
import random

pygame.init()

# Define colors, because the PyGame library
# does not do this by default
white = (255, 255, 255)
darkGray = (50, 50, 50)
lightGray = (150, 150, 150)
black = (0, 0, 0)
red = (245, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
# the title of the window
pygame.display.set_caption('Snake')

# clock
clock = pygame.time.Clock()
FPS = 15

block_size = 20

font = pygame.font.SysFont(None, 25) # font-size 25

def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, lightGray, [XnY[0], XnY[1], block_size, block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

# while gameExit is false
# the game loop
def gameLoop():

    gameExit = False
    gameOver = False

    # leader/head of the snake starting coords
    lead_x = display_width/2
    lead_y = display_height/2
    # track the change in position for constant motion
    lead_x_change = 0
    lead_y_change = 0
    # randoms for apple and stuff
    randAppleX = round(random.randrange(0, display_width - block_size))#/10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size))#/10.0) * 10.0

    snakeList = []
    snakeLength = 1

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(darkGray)
            message_to_screen("Game over, press C to play again, Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit event
                gameExit = True # stops the loop and makes the X work
            # moving the snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # if left arrow
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT: # if right arrow
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP: # if up arrow
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN: # if down arrow
                    lead_y_change = block_size
                    lead_x_change = 0

            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameOver = True

            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #        lead_x_change = 0
        lead_x += lead_x_change # sum the values
        lead_y += lead_y_change # sum y values

        gameDisplay.fill(darkGray)

        AppleThickness = 30
        # draw apple
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        # the snakeList
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        # call snake function
        # pass variables from the gameLoop()
        snake(block_size, snakeList)

        # rect(where, color, coordinates [startX, startY, w, h])
        pygame.draw.rect(gameDisplay, lightGray, [lead_x, lead_y, block_size, block_size])

        # using fill to draw rectangles
        # using fill lets you use graphics acceleration
        #gameDisplay.fill(red, rect=[200, 200, 50, 50])

        # draw everything first, then render it
        pygame.display.update()

        # logic for collision of snake and apple
#        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
#            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
#                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0) * 10.0
#                randAppleY = round(random.randrange(0, display_height - block_size))#/10.0) * 10.0
#                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_x + block_size < randAppleX + AppleThickness:
                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size))#/10.0) * 10.0
                snakeLength += 1
                
        # frames per second
        # this is the speed at which the snake will move/refresh
        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
