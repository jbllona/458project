import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import matplotlib.pyplot as plt




def drawGraph(time_turns, rates, virusName, graphType):
    title = "Rate of Infection by a "+virusName +" in a "+graphType+" Network"
    fileName = virusName+"_"+graphType + ".png"
    plt.figure() # plot time turns vs percentage of infected network/system
    plt.ylabel("Infection rate per step")
    plt.xlabel("Network Cycles")
    plt.title(title)
    plt.plot(range(time_turns), rates)
    plt.savefig(fileName)
    
virus = viruses.Worm()

Type = "Worm"

theNetwork = n.Network(disp.graphType.LINE)
theNetwork.createnetwork("line.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Line")

theNetwork = n.Network(disp.graphType.RING)
theNetwork.createnetwork("ring.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Ring")

theNetwork = n.Network(disp.graphType.MESH)
theNetwork.createnetwork("mesh.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Mesh")

theNetwork = n.Network(disp.graphType.ALL_CONNECTED)
theNetwork.createnetwork("fullconnect.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Fully Connected")

theNetwork = n.Network(disp.graphType.STAR)
theNetwork.createnetwork("star.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Star")

theNetwork = n.Network(disp.graphType.TREE)
theNetwork.createnetwork("tree.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Tree")

virus = viruses.Trojan()
Type = "Trojan"

theNetwork = n.Network(disp.graphType.LINE)
theNetwork.createnetwork("line.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Line")

theNetwork = n.Network(disp.graphType.RING)
theNetwork.createnetwork("ring.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Ring")

theNetwork = n.Network(disp.graphType.MESH)
theNetwork.createnetwork("mesh.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Mesh")

theNetwork = n.Network(disp.graphType.ALL_CONNECTED)
theNetwork.createnetwork("fullconnect.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Fully Connected")

theNetwork = n.Network(disp.graphType.STAR)
theNetwork.createnetwork("star.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Star")

theNetwork = n.Network(disp.graphType.TREE)
theNetwork.createnetwork("tree.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Tree")

virus = viruses.LogicBomb()

Type = "Logic Bomb"

theNetwork = n.Network(disp.graphType.LINE)
theNetwork.createnetwork("line.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Line")

theNetwork = n.Network(disp.graphType.RING)
theNetwork.createnetwork("ring.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Ring")

theNetwork = n.Network(disp.graphType.MESH)
theNetwork.createnetwork("mesh.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Mesh")

theNetwork = n.Network(disp.graphType.ALL_CONNECTED)
theNetwork.createnetwork("fullconnect.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Fully Connected")

theNetwork = n.Network(disp.graphType.STAR)
theNetwork.createnetwork("star.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Star")

theNetwork = n.Network(disp.graphType.TREE)
theNetwork.createnetwork("tree.txt")
numberOfSteps, infectionRates = sim.runOnce(theNetwork, 1, virus, )
drawGraph(numberOfSteps, infectionRates, Type, "Tree")