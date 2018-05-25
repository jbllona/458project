from system import System
from enum import Enum
import numpy as N
import displayVirusSpread as disp

class state(Enum):
    none          = 0
    clean         = 1
    infected      = 2
    suceptable    = 3
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
    nodeID = 0
    adjacentNodes = None
    suceptibility = None
    def __init__(self, nodeNum):
        self.nodeID = nodeNum
        self.suceptibility = N.random.uniform(.3, 1)
        self.adjacentNodes = []


class Network:
    nodes = None
    edges = None
    infectedList = None
    networkType = graphType.NONE

    def __init__(self, type):
        self.edges = {}
        self.networkType = type
        self.infectedList = [state.none]

    def createnetwork(self, filename):
        graphArray = disp.drawGraphFromFile(filename)
        for edge in graphArray:
            lhs = int(edge[0])
            rhs = int(edge[1])
            if lhs not in self.edges:
                self.infectedList.append(state.clean)
                self.edges[lhs] = Node(lhs)
                self.edges[lhs].adjacentNodes.append(rhs)
            else:
                self.edges[lhs].adjacentNodes.append(rhs)
            if rhs not in self.edges:
                self.infectedList.append(state.clean)
                self.edges[rhs] = Node(rhs)
                self.edges[rhs].adjacentNodes.append(lhs)
            else:
                self.edges[rhs].adjacentNodes.append(lhs)
            
