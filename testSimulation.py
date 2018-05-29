import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import fileMaker as fm



# virus = viruses.superVirus()
# theNetwork = n.Network(disp.graphType.MESH)
# theNetwork.createnetwork("mesh.txt")
# sim.runOnce(theNetwork, 1, virus)

# virus = viruses.logicBomb()
# theNetwork = n.Network(disp.graphType.MESH)
# theNetwork.createnetwork("mesh.txt")
# sim.runOnce(theNetwork, 1, virus)

# virus = viruses.trojan()
fm.main()
virus = viruses.Worm()
theNetwork = n.Network(disp.graphType.LINE)
theNetwork.createnetwork("line.txt")
count,infectionRates, percent_infected = sim.runOnce(theNetwork, 1, virus, True)
#sim.drawGraph(time_turns, percent_infected)