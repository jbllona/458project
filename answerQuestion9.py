"""
Answer to Question 9

Description: 
            This file is for answering question 9 in the analysis document.
            The code below simulates the virus spread and creates a graph
            of time verses the node strength.
"""


import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import fileMaker as fm
import numpy as N
import matplotlib.pyplot as plt

# Store time for each run
time_taken_Trojan = []  
time_taken_Worm = []

# Node strength range is divided into 3 categories
node_strengths = [(0, 0.2), (0.2, 0.4), (0.4, 0.6)]
strength_scale = ['High', 'Medium', 'Low']

# Simulation for the Trojan
virus = viruses.Trojan()
for i in range(len(node_strengths)):
    """
    Description:
        For the length of the node_strenths array, each time a network for each
        type of network is created consisting of 50 nodes. Then runOnce() method of
        simulateVirusSpread module is called which returns the time it took to
        run the simulation, infection rates, and percent of infected nodes in the
        network. The times taken are appended to the time_taken_Trojan array each
        iteration.
    Pre:
        time_taken_Trojan and time_taken_Worm do not contain any data
    Post:
        time_taken_Trojan and time_taken_Worm will be populated with data about
        how much time it took for each simulation run for each type of network.
    """
    fm.main(50)
    line_Network = n.Network(disp.graphType.LINE)
    line_Network.createnetwork("line.txt", node_strengths[i])
    ring_Network = n.Network(disp.graphType.RING)
    ring_Network.createnetwork("ring.txt", node_strengths[i])
    star_Network = n.Network(disp.graphType.STAR)
    star_Network.createnetwork("star.txt", node_strengths[i])
    tree_Network = n.Network(disp.graphType.TREE)
    tree_Network.createnetwork("tree.txt", node_strengths[i])
    all_connected_Network = n.Network(disp.graphType.ALL_CONNECTED)
    all_connected_Network.createnetwork("fullconnect.txt", node_strengths[i])
    mesh_Network = n.Network(disp.graphType.MESH)
    mesh_Network.createnetwork("mesh.txt", node_strengths[i])

    # Call runOnce in the simulateVirusSpread module for each network type
    time_turns1,infectionRates1, percent_infected_line = sim.runOnce(line_Network, 1, virus, False)
    time_turns2,infectionRates2, percent_infected_ring = sim.runOnce(ring_Network, 1, virus, False)
    time_turns3,infectionRates3, percent_infected_star = sim.runOnce(star_Network, 1, virus, False)
    time_turns4,infectionRates4, percent_infected_tree = sim.runOnce(tree_Network, 1, virus, False)
    time_turns5,infectionRates5, percent_infected_connected = sim.runOnce(all_connected_Network, 1, virus, False)
    time_turns6,infectionRates6, percent_infected_mesh = sim.runOnce(mesh_Network, 1, virus, False)

    time_taken_Trojan.append(time_turns1)
    time_taken_Trojan.append(time_turns2)
    time_taken_Trojan.append(time_turns3)
    time_taken_Trojan.append(time_turns4)
    time_taken_Trojan.append(time_turns5)
    time_taken_Trojan.append(time_turns6)

# rows = size of network
# columns = shape of network
time_taken_Trojan = N.reshape(time_taken_Trojan, [3, 6])  # Reshape to the correct width/rows
print(time_taken_Trojan)
#
# network data depending on the size of network 10 - 100 for each shape of network
# Get the corresponding portion of the time_taken_Trojan for each type of network.
line_data_Trojan = N.array(time_taken_Trojan[:, 0])
ring_data_Trojan = N.array(time_taken_Trojan[:, 1])
star_data_Trojan = N.array(time_taken_Trojan[:, 2])
tree_data_Trojan = N.array(time_taken_Trojan[:, 3])
fullconnect_data_Trojan = N.array(time_taken_Trojan[:, 4])
mesh_data_Trojan = N.array(time_taken_Trojan[:, 5])

# drawing graph to compare
fig = plt.figure()
plt.plot(strength_scale, line_data_Trojan)
plt.plot(strength_scale, ring_data_Trojan)
plt.plot(strength_scale, star_data_Trojan)
plt.plot(strength_scale, tree_data_Trojan)
plt.plot(strength_scale, fullconnect_data_Trojan)
plt.plot(strength_scale, mesh_data_Trojan)
plt.xlabel("Node Strengths")
plt.ylabel("Time")
plt.legend(['line', 'ring', 'star', 'tree', 'full_connect' , 'mesh'] , loc='upper right')
plt.title("Trojan Infection")
plt.show()

virus = viruses.Worm()
for i in range(len(node_strengths)):
    """
        For the length of the node_strenths array, each time a network for each
        type of network is created consisting of 50 nodes. Then runOnce() method of
        simulateVirusSpread module is called which returns the time it took to
        run the simulation, infection rates, and percent of infected nodes in the
        network. The times taken are appended to the time_taken_Worm array each
        iteration.
    """
    fm.main(50)
    line_Network = n.Network(disp.graphType.LINE)
    line_Network.createnetwork("line.txt", node_strengths[i])
    ring_Network = n.Network(disp.graphType.RING)
    ring_Network.createnetwork("ring.txt", node_strengths[i])
    star_Network = n.Network(disp.graphType.STAR)
    star_Network.createnetwork("star.txt", node_strengths[i])
    tree_Network = n.Network(disp.graphType.TREE)
    tree_Network.createnetwork("tree.txt", node_strengths[i])
    all_connected_Network = n.Network(disp.graphType.ALL_CONNECTED)
    all_connected_Network.createnetwork("fullconnect.txt", node_strengths[i])
    mesh_Network = n.Network(disp.graphType.MESH)
    mesh_Network.createnetwork("mesh.txt", node_strengths[i])

    # Call runOnce in the simulateVirusSpread module for each network type
    time_turns1,infectionRates, percent_infected = sim.runOnce(line_Network, 1, virus, False)
    time_turns2,infectionRates, percent_infected = sim.runOnce(ring_Network, 1, virus, False)
    time_turns3,infectionRates, percent_infected = sim.runOnce(star_Network, 1, virus, False)
    time_turns4,infectionRates, percent_infected = sim.runOnce(tree_Network, 1, virus, False)
    time_turns5,infectionRates, percent_infected = sim.runOnce(all_connected_Network, 1, virus, False)
    time_turns6,infectionRates, percent_infected = sim.runOnce(mesh_Network, 1, virus, False)

    time_taken_Worm.append(time_turns1)
    time_taken_Worm.append(time_turns2)
    time_taken_Worm.append(time_turns3)
    time_taken_Worm.append(time_turns4)
    time_taken_Worm.append(time_turns5)
    time_taken_Worm.append(time_turns6)

# # rows = size of network
# # columns = shape of network
time_taken_Worm = N.reshape(time_taken_Worm, [3, 6])
print(time_taken_Worm)

network data depending on the size of network 10 - 100 for each shape of network
Get the corresponding portion of the time_taken_Trojan for each type of network.
line_data_Worm = N.array(time_taken_Worm[:, 0])
ring_data_Worm = N.array(time_taken_Worm[:, 1])
star_data_Worm = N.array(time_taken_Worm[:, 2])
tree_data_Worm = N.array(time_taken_Worm[:, 3])
fullconnect_data_Worm = N.array(time_taken_Worm[:, 4])
mesh_data_Worm = N.array(time_taken_Worm[:, 5])
#
# drawing graph to compare
# fig = plt.figure()
# plt.plot(strength_scale, line_data_Worm)
# plt.plot(strength_scale, ring_data_Worm)
# plt.plot(strength_scale, star_data_Worm)
# plt.plot(strength_scale, tree_data_Worm)
# plt.plot(strength_scale, fullconnect_data_Worm)
# plt.plot(strength_scale, mesh_data_Worm)
# plt.xlabel("Node Strengths")
# plt.ylabel("Time")
# plt.legend(['line', 'ring', 'star', 'tree', 'full_connect' , 'mesh'] , loc='upper right')
# plt.title("Worm Infection")
# plt.show()
