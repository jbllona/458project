from system import System
from enum import Enum
import numpy as N
import displayVirusSpread as disp


class state(Enum):
    """
        Description: state is an Enum type. none is for a non-node such as for the zeroth index/node
                     which is not used in the network. clean refers to a node that has not yet seen
                     any effect from a virus. All nodes at the initialization step are set to clean.
                     infected means a node is infected by a virus. susceptible means there is a higher
                     chance of getting infected by a virus but that has not happened yet. immune is when
                     a node has recovered from an infection and is now immune to all viruses.
     """
    none          = 0
    clean         = 1
    infected      = 2
    susceptible    = 3
    immune        = 4

class graphType(Enum):
    """
        Description: graphType is an Enum type. NONE is for a node that does not represent the network.
                     For example zeroth node and/or index is not considered a node in the network. All
                     other network types are given numbers from 1 to 8 that represents a particular type
                     of network.
     """
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
    """
        Description: Node class represents a computer in the network. nodeID is used to identify
                     the node, adjacentNodes is a list that stores a nodes directly connected neighbors.
                     susceptibility var tells us if a node becomes susceptible to getting infectede
                     from a virus.
    """
    nodeID = -1
    adjacentNodes = None
    susceptibility = None
    def __init__(self, nodeNum):
        self.nodeID = nodeNum
        self.susceptibility = N.random.uniform(.0, .7)
        self.adjacentNodes = []


class Network:
    """
        Description: Node class represents a computer in the network. nodeID is used to identify
                     the node, adjacentNodes is a list that stores a nodes directly connected neighbors.
                     susceptibility var tells us if a node becomes susceptible to getting infectede
                     from a virus.
    """
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
            
