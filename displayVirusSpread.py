import numpy as N
import pygame
from enum import Enum
import sys

# def drawGraphFromFile(fileName):
#     retVal = []
#     with open(fileName, 'r') as file:
#         for line in file:
#             if line[0] != '#':
#                 if line.find('\n') != -1:
#                     retVal.append(line[:line.find('\n')].split(" "))
#                 else:
#                     retVal.append(line.split(" "))
#     return retVal

# # RING_GRAPH          = drawGraphFromFile('ringGraph.txt')
# # STAR_GRAPH          = drawGraphFromFile('starGraph.txt')
# # MESH_GRAPH          = drawGraphFromFile('meshGraph.txt')
# # ALL_CONNECTED_GRAPH = drawGraphFromFile('allConnectedGraph.txt')
# # BUS_GRAPH           = drawGraphFromFile('busGraph.txt')
# # HYBRID_GRAPH        = drawGraphFromFile('hybridGraph.txt')
# # LINE_GRAPH          = drawGraphFromFile('lineGraph.txt')
# # TREE_GRAPH          = drawGraphFromFile('treeGraph.txt')

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

def roundTuple(tuple):
    return (round(tuple[0]),round(tuple[1]))

def distanceBetweenTwoPoints(pointA, pointB):
    return ((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)**.5

def startAnimation():
    clock = pygame.time.Clock()
    displayImage = None
    done = False
    screen = None
    width = 640
    height = 480
    displayImage = N.zeros((width,height,3), dtype = N.uint8) + 255
    pygame.init()
    screen = pygame.display.set_mode((width,height))

    while not done:
        iterationDone = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((255,255,255))

        for line in linesToDraw:
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
            # addNextDataToLinesToDraw
            linesToDraw.append([pointC, pointB, 0])
        
        clock.tick(60)