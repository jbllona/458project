# -*- coding: utf-8 -*-
import numpy as N
import Network
import viruses

filename = 'mesh.txt'
network = Network.Network('mesh')
network.createnetwork(filename)
print(network.nodes)

virus1 = viruses.SuperVirus()
virus2 = viruses.LogicBomb()
virus3 = viruses.Trojan()
virus4 = viruses.Worm()

virusList = [virus1, virus2, virus3, virus4]

# numIterations = 100    # represents 100 days
#
# # Initialize virus spread by infecting the first node in the network
# network.nodes[1].status = network.State.infected
# network.infectedList.append(network.nodes[rand].nodeID)

# state = []
# state.append(network.infectedList)
#
# for i in range(numIter):
#     for infectedNode in network.infectedList:
#         adjNodes = network.nodes[infectedNode].adjacentNodes
