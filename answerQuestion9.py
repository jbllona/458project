import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import fileMaker as fm
import numpy as N
import matplotlib.pyplot as plt


time_taken_Trojan = []
time_taken_Worm = []

node_strengths = [(0, 0.2), (0.2, 0.4), (0.4, 0.6)]
strength_scale = ['High', 'Medium', 'Low']

virus = viruses.Trojan()
for i in range(len(node_strengths)):
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
time_taken_Trojan = N.reshape(time_taken_Trojan, [3, 6])
print(time_taken_Trojan)
#
# network data depending on the size of network 10 - 100 for each shape of network
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

# network data depending on the size of network 10 - 100 for each shape of network
# line_data_Worm = N.array(time_taken_Worm[:, 0])
# ring_data_Worm = N.array(time_taken_Worm[:, 1])
# star_data_Worm = N.array(time_taken_Worm[:, 2])
# tree_data_Worm = N.array(time_taken_Worm[:, 3])
# fullconnect_data_Worm = N.array(time_taken_Worm[:, 4])
# mesh_data_Worm = N.array(time_taken_Worm[:, 5])
#
# # drawing graph to compare
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