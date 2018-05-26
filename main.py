# -*- coding: utf-8 -*-
import numpy as N
import Network
import viruses

filename = 'mesh.txt'
network = network.Network('mesh')
network.createnetwork(filename)
print(network.edges)

virus1 = viruses.SuperVirus()
virus2 = viruses.logicBomb()
virus3 = viruses.trojan()
virus4 = viruses.worm()

virusList = [virus1, virus2, virus3, virus4]

numIterations = 100    # represents 100 days

# Initialize virus spread by infecting the first node in the network
network.nodes[1].status = network.State.infected
network.infectedList.append(network.nodes[rand].nodeID)

# state = []
# state.append(network.infectedList)
#
# for i in range(numIter):
#     for infectedNode in network.infectedList:
#         adjNodes = network.nodes[infectedNode].adjacentNodes
