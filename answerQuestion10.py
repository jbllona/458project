import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import fileMaker
import numpy as N
import matplotlib.pyplot as plt

networkSize = 10
n_runs = 100

files = ['tree.txt', 'mesh.txt', 'line.txt', 'star.txt', 'ring.txt', 'fullconnect.txt']

def runSimulation(theNetwork, startingPoint, virus):
    if virus == "W":
        virus = viruses.Worm()
    else:
        virus = viruses.Trojan()

    sim.runOnce(theNetwork, startingPoint, virus, False)

    infectedCount = 0
    for node in theNetwork.infectedList[1:]:
        if node == n.State.infected:
            infectedCount += 1

    infectedPercent = (infectedCount / networkSize) * 100

    return infectedPercent


fileMaker.fullConnected(networkSize)

infectedPercentLowStrengthTreeWorm = []
infectedPercentMedStrengthTreeWorm = []
infectedPercentHighStrengthTreeWorm = []

infectedPercentLowStrengthTreeTrojan = []
infectedPercentMedStrengthTreeTrojan = []
infectedPercentHighStrengthTreeTrojan = []

virus = viruses.Worm()
for x in range(n_runs):

    nodeStrengthRange = (0, .2)
    theNetwork = n.Network(disp.graphType.TREE)
    theNetwork.createnetwork("fullconnect.txt", nodeStrengthRange)

    infectedPercentLowStrengthTreeWorm.append(runSimulation(theNetwork, 1, "W"))

    nodeStrengthRange = (.2, .4)
    theNetwork = n.Network(disp.graphType.TREE)
    theNetwork.createnetwork("fullconnect.txt", nodeStrengthRange)

    infectedPercentMedStrengthTreeWorm.append(runSimulation(theNetwork, 1, "W"))

    nodeStrengthRange = (.4, .6)
    theNetwork = n.Network(disp.graphType.TREE)
    theNetwork.createnetwork("fullconnect.txt", nodeStrengthRange)

    infectedPercentHighStrengthTreeWorm.append(runSimulation(theNetwork, 1, "W"))



virus = viruses.Trojan()
for x in range(n_runs):

    nodeStrengthRange = (0.4, .6)
    theNetwork = n.Network(disp.graphType.TREE)
    theNetwork.createnetwork("fullconnect.txt", nodeStrengthRange)

    infectedPercentLowStrengthTreeTrojan.append(runSimulation(theNetwork, 1, "T"))

    nodeStrengthRange = (.2, .4)
    theNetwork = n.Network(disp.graphType.TREE)
    theNetwork.createnetwork("fullconnect.txt", nodeStrengthRange)

    infectedPercentMedStrengthTreeTrojan.append(runSimulation(theNetwork, int(networkSize / 2), "T"))

    nodeStrengthRange = (0, .2)
    theNetwork = n.Network(disp.graphType.TREE)
    theNetwork.createnetwork("fullconnect.txt", nodeStrengthRange)

    infectedPercentHighStrengthTreeTrojan.append(runSimulation(theNetwork, networkSize, "T"))


infectedPercentLowStrengthTreeWorm = N.array(infectedPercentLowStrengthTreeWorm)
infectedPercentMedStrengthTreeWorm = N.array(infectedPercentMedStrengthTreeWorm)
infectedPercentHighStrengthTreeWorm = N.array(infectedPercentHighStrengthTreeWorm)

infectedPercentLowStrengthTreeTrojan = N.array(infectedPercentLowStrengthTreeTrojan)
infectedPercentMedStrengthTreeTrojan = N.array(infectedPercentMedStrengthTreeTrojan)
infectedPercentHighStrengthTreeTrojan = N.array(infectedPercentHighStrengthTreeTrojan)

meansWorm = [N.mean(infectedPercentLowStrengthTreeWorm), N.mean(infectedPercentMedStrengthTreeWorm),
             N.mean(infectedPercentHighStrengthTreeWorm)]
meansTrojan = [N.mean(infectedPercentLowStrengthTreeTrojan), N.mean(infectedPercentMedStrengthTreeTrojan),
               N.mean(infectedPercentHighStrengthTreeTrojan)]


bar_width = 0.125
bar_locations = N.array([1, 1.5, 2])
fig, ax = plt.subplots()
plt.bar(bar_locations,
        meansWorm, bar_width,
        alpha=.4,
        color='r',
        label='Worm')

plt.bar(bar_locations + (bar_width * 2),
        meansTrojan,
        bar_width,
        alpha=.4,
        color='b',
        label='Trojan')

plt.xticks(bar_locations + bar_width, ('High Strength', 'Medium Strength', 'Low Strength'))
plt.ylabel('percentage infected')
plt.xlabel('Node Strength')
plt.title('Fully Connected')
plt.legend()

plt.show()
fig.savefig('fullconnect-infection-vs-node-strength.png')