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

virus = viruses.Trojan()
#virus = viruses.worm()
theNetwork = n.Network(disp.graphType.MESH)
theNetwork.createnetwork("mesh.txt")
time_steps, percent_infected = sim.runOnce(theNetwork, 1, virus)
sim.drawGraph(time_steps, percent_infected)