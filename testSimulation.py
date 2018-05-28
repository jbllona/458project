import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n


# virus = viruses.superVirus()
# theNetwork = n.Network(disp.graphType.MESH)
# theNetwork.createnetwork("mesh.txt")
# sim.runOnce(theNetwork, 1, virus)

# virus = viruses.logicBomb()
# theNetwork = n.Network(disp.graphType.MESH)
# theNetwork.createnetwork("mesh.txt")
# sim.runOnce(theNetwork, 1, virus)

# virus = viruses.trojan()
virus = viruses.Worm()
theNetwork = n.Network(disp.graphType.MESH)
theNetwork.createnetwork("mesh.txt")
percent_infected, time_turns = sim.runOnce(theNetwork, 1, virus)
sim.drawGraph(time_turns, percent_infected)