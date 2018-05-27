# -*- coding: utf-8 -*-
import numpy as N
import Network
import viruses

file_list = {'list': 'line.txt', 'mesh': 'mesh.txt', 'ring': 'ring.txt', 'star': 'star.txt', 'fullconnect': 'fullconnect.txt', 'tree': 'tree.txt'}

filename = file_list['list']
network_type = list(file_list.keys())[0]
network = Network.Network(network_type)
network.createnetwork(filename)

virus1 = viruses.SuperVirus()
virus2 = viruses.LogicBomb()
virus3 = viruses.Trojan()
# virus4 = viruses.Worm()
virusList = [virus1, virus2, virus3]

numIterations = 5    # represents 100 days
network_status_per_virus = []

# Do the simulation for each virus type
for active_virus in virusList:
    # Create Network
    network = Network.Network(network_type)
    network.createnetwork(filename)
    # Initialize virus spread by infecting the first node in the network
    network.nodes[1].status = Network.State.infected
    network.infectedList[1] = Network.State.infected

    # Append the initial network status to the network_status List, which will be sent to the
    # class that visualizes the network
    network_status_per_simulation = [network.infectedList]

    # For each iteration,
        # Take a node from the infectedList
            # If a node is already infected,
                # get its neighbors by Node.adjacentNodes
                # For each of the neighbors,
                    # retrieve True or False from the virus
                    # If the virus says True,
                        # Spread it to the neighbor
                        # Update infectedList & its own status

    for i in range(numIterations):
        for j in range(len(network.infectedList)):
            if network.infectedList[j] == Network.State.infected:
                neighbors = network.nodes[j].adjacentNodes
                for neighbor in neighbors:
                    if (active_virus.infectOrNot(network, neighbor)):
                        network.nodes[neighbor].status = Network.State.infected

        network_status_per_simulation.append(network.infectedList)

    network_status_per_virus.append(network_status_per_simulation)

