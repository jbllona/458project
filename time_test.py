import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import fileMaker as fm
import numpy as N

virus = viruses.SuperVirus()
#virus = viruses.LogicBomb()
#virus = viruses.Trojan()
#virus = viruses.Worm()

time_taken = []

size_of_network = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(size_of_network)):
    fm.main(size_of_network[i])
    line_Network = n.Network(disp.graphType.LINE)
    line_Network.createnetwork("mesh.txt")
    ring_Network = n.Network(disp.graphType.RING)
    ring_Network.createnetwork("mesh.txt")
    star_Network = n.Network(disp.graphType.STAR)
    star_Network.createnetwork("mesh.txt")
    tree_Network = n.Network(disp.graphType.TREE)
    tree_Network.createnetwork("mesh.txt")
    all_connected_Network = n.Network(disp.graphType.ALL_CONNECTED)
    all_connected_Network.createnetwork("mesh.txt")
    mesh_Network = n.Network(disp.graphType.MESH)
    mesh_Network.createnetwork("mesh.txt")

    percent_infected1, time_turns1 = sim.runOnce(line_Network, 1, virus, False)
    percent_infected2, time_turns2 = sim.runOnce(ring_Network, 1, virus, False)
    percent_infected3, time_turns3 = sim.runOnce(star_Network, 1, virus, False)
    percent_infected4, time_turns4 = sim.runOnce(tree_Network, 1, virus, False)
    percent_infected5, time_turns5 = sim.runOnce(all_connected_Network, 1, virus, False)
    percent_infected6, time_turns6 = sim.runOnce(mesh_Network, 1, virus, False)
    time_taken.append(len(time_turns1) - 1)
    time_taken.append(len(time_turns2) - 1)
    time_taken.append(len(time_turns3) - 1)
    time_taken.append(len(time_turns4) - 1)
    time_taken.append(len(time_turns5) - 1)
    time_taken.append(len(time_turns6) - 1)

# rows = size of network
# columns = shape of network
time_taken = N.reshape(time_taken, [10, 6])
print(time_taken)

# def draw_graph:


