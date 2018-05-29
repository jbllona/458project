import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import matplotlib.pyplot as plt

def drawGraph(infectionRates, percentages, graphType):
    title = "Rate of Infection by % Infected in "+graphType+" Network"
    fileName = "Rate of Infection by %_"+graphType + ".png"
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_ylabel("Percentage of Network Infected")
    ax1.set_xlabel("Average Infections per Cycle")
    plt.title(title)
    
    ax1.scatter(infectionRates[0], percentages[0], color=color, alpha=0.5, label="Worm")
    color = 'tab:blue'
    ax1.scatter(infectionRates[1], percentages[1], color=color, alpha=0.5, label="Trojan")
    color = 'tab:green'
    ax1.scatter(infectionRates[2], percentages[2], color=color, alpha=0.5, label="Logic Bomb")
    
    ax1.legend()
    ax1.grid(True)
    #plt.show()
    plt.savefig(fileName)
def getPercentage(theNetwork):
    infectedCount = 0
    for node in theNetwork.infectedList[1:]:
        if node == n.State.infected:
            infectedCount+= 1
    return (infectedCount / len(theNetwork.nodes)) * 100

Types = ["Worm", "Trojan", "Logic Bomb"]
dispatcher = {0:viruses.Worm, 1:viruses.Trojan, 2:viruses.LogicBomb}
averageInfectionRatesLine = [[],[],[]]
averagePercentagesLine = [[],[],[]]
averageInfectionRatesRing = [[],[],[]]
averagePercentagesRing = [[],[],[]]
averageInfectionRatesMesh = [[],[],[]]
averagePercentagesMesh = [[],[],[]]
averageInfectionRatesAllConnected = [[],[],[]]
averagePercentagesAllConnected = [[],[],[]]
averageInfectionRatesStar = [[],[],[]]
averagePercentagesStar = [[],[],[]]
averageInfectionRatesTree = [[],[],[]]
averagePercentagesTree = [[],[],[]]

for current in range(100):
    for x in range(3):
        theNetwork = n.Network(disp.graphType.LINE)
        theNetwork.createnetwork("line.txt")
        numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, dispatcher[x](), False)
        averageInfectionRate = sum(infectionRates)/len(infectionRates)
        averagePercentage = sum(percentatages)/len(percentatages)
        
        averageInfectionRatesLine[x].append(averageInfectionRate)
        averagePercentagesLine[x].append(getPercentage(theNetwork))
        
    
        theNetwork = n.Network(disp.graphType.RING)
        theNetwork.createnetwork("ring.txt")
        numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, dispatcher[x](), False)
        averageInfectionRatesRing[x].append(averageInfectionRate)
        averagePercentagesRing[x].append(getPercentage(theNetwork))
    
        theNetwork = n.Network(disp.graphType.MESH)
        theNetwork.createnetwork("mesh.txt")
        numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, dispatcher[x](), False)
        
        averageInfectionRatesMesh[x].append(averageInfectionRate)
        averagePercentagesMesh[x].append(getPercentage(theNetwork))
    
        theNetwork = n.Network(disp.graphType.ALL_CONNECTED)
        theNetwork.createnetwork("fullconnect.txt")
        numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, dispatcher[x](), False)

        averageInfectionRatesAllConnected[x].append(averageInfectionRate)
        averagePercentagesAllConnected[x].append(getPercentage(theNetwork))
    
        theNetwork = n.Network(disp.graphType.STAR)
        theNetwork.createnetwork("star.txt")
        numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, dispatcher[x](), False)

        averageInfectionRatesStar[x].append(averageInfectionRate)
        averagePercentagesStar[x].append(getPercentage(theNetwork))
        
        theNetwork = n.Network(disp.graphType.TREE)
        theNetwork.createnetwork("tree.txt")
        numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, dispatcher[x](), False)

        averageInfectionRatesTree[x].append(averageInfectionRate)
        averagePercentagesTree[x].append(getPercentage(theNetwork))

drawGraph(averageInfectionRatesLine, averagePercentagesLine, "Line")
drawGraph(averageInfectionRatesRing, averagePercentagesRing, "Ring")
drawGraph(averageInfectionRatesMesh, averagePercentagesMesh, "Mesh")
drawGraph(averageInfectionRatesAllConnected, averagePercentagesAllConnected, "Fully Connected")
drawGraph(averageInfectionRatesStar, averagePercentagesStar, "Star")
drawGraph(averageInfectionRatesTree, averagePercentagesTree, "Tree")