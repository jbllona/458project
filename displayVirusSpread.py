import numpy as N
import pygame
from enum import Enum
import sys

def drawGraphFromFile(fileName):
    retVal = []
    with open(fileName, 'r') as file:
        for line in file:
            if line[0] != '#':
                if line.find('\n') != -1:
                    retVal.append(line[:line.find('\n')].split("\t"))
                else:
                    retVal.append(line.split("\t"))
    return retVal

display_width  = 640
display_height = 480

RING_GRAPH          = drawGraphFromFile('ring.txt')
STAR_GRAPH          = drawGraphFromFile('star.txt')
# MESH_GRAPH          = drawGraphFromFile('meshGraph.txt')
# ALL_CONNECTED_GRAPH = drawGraphFromFile('allConnectedGraph.txt')
# BUS_GRAPH           = drawGraphFromFile('busGraph.txt')
# HYBRID_GRAPH        = drawGraphFromFile('hybridGraph.txt')
# LINE_GRAPH          = drawGraphFromFile('lineGraph.txt')
# TREE_GRAPH          = drawGraphFromFile('treeGraph.txt')

computerImage = pygame.image.load("compImage.png")
computerImage = pygame.transform.scale(computerImage, (50, 50))


def getComputerLocationsOnDisplay(typeOfGraph):
    retVal = [[0, -1, -1]]
    if typeOfGraph == graphType.STAR:
        centerOfFieldX = int(display_width/2)
        centerOfFieldY = int(display_height/2)

        numberOfNodes = N.amax(N.array(STAR_GRAPH).astype(int))
        retVal.append([1, centerOfFieldX, centerOfFieldY])
        for x in range(2, (numberOfNodes + 1)):
            retVal.append([x, \
            centerOfFieldX + ((display_height / 3) * N.sin((x - 2) * ((2 * N.pi) / (numberOfNodes-1)))), \
            centerOfFieldY - ((display_height / 3) * N.cos((x - 2) * ((2 * N.pi) / (numberOfNodes-1))))])
    elif typeOfGraph == graphType.RING:
        centerOfFieldX = int(display_width/2)
        centerOfFieldY = int(display_height/2)

        numberOfNodes = N.amax(N.array(RING_GRAPH).astype(int))
        for x in range(1, (numberOfNodes + 1)):
            retVal.append([x, \
            centerOfFieldX + ((display_height / 3) * N.sin((x - 2) * ((2 * N.pi) / numberOfNodes))), \
            centerOfFieldY - ((display_height / 3) * N.cos((x - 2) * ((2 * N.pi) / numberOfNodes)))])

    return retVal

class graphType(Enum):
    NONE          = 0
    RING          = 1
    STAR          = 2
    MESH          = 3
    ALL_CONNECTED = 4
    BUS           = 5
    HYBRID        = 6
    LINE          = 7
    TREE          = 8

class dataToDisplay:

    #this needs to be set to the type of graph (star, ring, etc)
    typeOfGraph = graphType.NONE
    
    #this represents the nodes that the virus starts at
    startNodes = None

    #this list shall contain lists of tuples representing how the virus spreads.
    # 
    # Example:
    # [[(1,2), (1,3)]
    # [(1,4), (2,5), (2,6)]]
    #
    # in this example, during the first step of the simulation the virus spreads 
    # from node 1 to node 2, and node 1 to node 3. In the second step, it spreads 
    # from node 1 to node 4, and node 2 to nodes 5 and 6
    animationSteps = None
    def __init__(self):
        self.startNodes = []
        self.animationSteps = []

linesToDraw = []
defaultLines = []

def roundTuple(tuple):
    return (round(tuple[0]),round(tuple[1]))

def distanceBetweenTwoPoints(pointA, pointB):
    return ((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)**.5

def nodeToLocations(nodeMoves, positionsInImage):
    retVal = []
    for move in nodeMoves:
        x1 = positionsInImage[move[0]][1]
        y1 = positionsInImage[move[0]][2]
        x2 = positionsInImage[move[1]][1]
        y2 = positionsInImage[move[1]][2]
        retVal.append([(x1,y1),(x2,y2), 0])
    return retVal

def startAnimation(computerPositions, dataToDisplay):
    clock = pygame.time.Clock()
    displayImage = None
    done = False
    screen = None
    displayImage = N.zeros((display_width,display_height,3), dtype = N.uint8) + 255
    pygame.init()
    screen = pygame.display.set_mode((display_width,display_height))
    stepsDone = 0
    linesToDraw.append(nodeToLocations(dataToDisplay.animationSteps[0], computerPositions))

    while not done:
        iterationDone = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((255,255,255))

        # draw the computer images at each node, and the faint gray lines
        if dataToDisplay.typeOfGraph == graphType.STAR:
            for x in range(1, computerPositions[:,0].size):
                numberPairs = [(computerPositions[1,1], computerPositions[1,2]), (computerPositions[x,1], computerPositions[x,2])]
                pygame.draw.lines(screen, (100,100,100), False, numberPairs, 2)
                screen.blit(computerImage,(numberPairs[1][0]-25, numberPairs[1][1]-25))
        elif dataToDisplay.typeOfGraph == graphType.RING:

            screen.blit(computerImage, (computerPositions[1,1] - 25, computerPositions[1,2] - 25))
            numberPairs = [(computerPositions[-1,1], computerPositions[-1,2]), (computerPositions[1,1], computerPositions[1,2])]
            pygame.draw.lines(screen, (100,100,100), False, numberPairs,2)
            for x in range(2, computerPositions[:,0].size):
                numberPairs = [(computerPositions[x - 1,1], computerPositions[x - 1,2]), (computerPositions[x,1], computerPositions[x,2])]
                pygame.draw.lines(screen, (100,100,100), False, numberPairs, 2)
                screen.blit(computerImage,(numberPairs[1][0]-25, numberPairs[1][1]-25))

        #draw completed lines
        for x in range(stepsDone):
            for line in linesToDraw[x]:
                pygame.draw.lines(screen, (255,0,0), False, (line[0],line[1]),4)

        # draw in progress lines
        for line in linesToDraw[stepsDone]:
            totalDistance = distanceBetweenTwoPoints(line[0],line[1])
            x3 = line[0][0] + ((line[2]/totalDistance) * (line[1][0] - line[0][0]))
            y3 = line[0][1] + ((line[2]/totalDistance) * (line[1][1] - line[0][1]))
            toDraw = [line[0], (x3,y3)]
            pygame.draw.lines(screen, (255,0,0), False, toDraw, 4)

            if roundTuple(toDraw[1]) == roundTuple(line[1]):
                iterationDone = True
            else:
                line[2] += totalDistance/200
           
        pygame.display.update()

        if iterationDone == True:
            stepsDone += 1
            if stepsDone == len(dataToDisplay.animationSteps):
                done = True
            else:
                linesToDraw.append(nodeToLocations(dataToDisplay.animationSteps[stepsDone], computerPositions))
        clock.tick(60)

        

def display(data):
    computerLocations = N.array(getComputerLocationsOnDisplay(data.typeOfGraph))
    startAnimation(computerLocations, data)
    