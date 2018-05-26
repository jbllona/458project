# -*- coding: utf-8 -*-
import numpy as N
from Network import Network
import viruses

filename = 'mesh.txt'
network = Network('mesh')
network.createnetwork(filename)
print(network.edges)

virus = viruses.SuperVirus()

numIter = 100    # represents 100 days

rand = int(N.random.uniform() * len(network.nodes.keys()))
while rand is 0:
    rand = int(N.random.uniform() * len(network.nodes.keys()))

network.nodes[rand].state = Network.State.infected
network.infectedList.append(network.nodes[rand].nodeID)

# state = []
# state.append(network.infectedList)
#
# for i in range(numIter):
#     for infectedNode in network.infectedList:
#         adjNodes = network.nodes[infectedNode].adjacentNodes
