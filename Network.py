from system import System
from enum import Enum
import numpy as N
import displayVirusSpread as disp

class state(Enum):
    none          = 0
    clean         = 1
    infected      = 2
    susceptible    = 3
    immune        = 4

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

class Node:
    nodeID = -1
    adjacentNodes = None
    susceptibility = None
    p_infected = None # probability to get infected by worm
    infected = None
    def __init__(self, nodeNum):
        self.nodeID = nodeNum
        self.susceptibility = N.random.uniform(.0, .7)
        self.adjacentNodes = []
        self.p_infected = N.random.uniform(0, 0.5)
        infected


class Network:
    nodes = None
    infectedList = None
    networkType = graphType.NONE

    def __init__(self, type):
        self.nodes = {}
        self.networkType = type
        self.infectedList = [state.none]

    def createnetwork(self, filename):
        graphArray = disp.drawGraphFromFile(filename)
        for pair in graphArray:
            lhs = int(pair[0])
            rhs = int(pair[1])
            if lhs not in self.nodes:
                self.infectedList.append(state.clean)
                self.nodes[lhs] = Node(lhs)
                self.nodes[lhs].adjacentNodes.append(rhs)
            else:
                self.nodes[lhs].adjacentNodes.append(rhs)
            if rhs not in self.nodes:
                self.infectedList.append(state.clean)
                self.nodes[rhs] = Node(rhs)
                self.nodes[rhs].adjacentNodes.append(lhs)
            else:
                self.nodes[rhs].adjacentNodes.append(lhs)
            
