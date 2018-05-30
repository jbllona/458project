import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import fileMaker as fm



#virus = viruses.SuperVirus()
# theNetwork = n.Network(disp.graphType.MESH)
# theNetwork.createnetwork("mesh.txt")
# sim.runOnce(theNetwork, 1, virus)

#virus = viruses.LogicBomb()
# theNetwork = n.Network(disp.graphType.MESH)
# theNetwork.createnetwork("mesh.txt")
# sim.runOnce(theNetwork, 1, virus)

virus = viruses.Trojan()
#fm.main()
#virus = viruses.Worm()
theNetwork = n.Network(disp.graphType.STAR)
theNetwork.createnetwork("star.txt")
count,infectionRates, percent_infected = sim.runOnce(theNetwork, 1, virus, True)
#sim.drawGraph(time_turns, percent_infected)