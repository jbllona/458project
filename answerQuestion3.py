import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import fileMaker
import numpy as N
import matplotlib.pyplot as plt

networkSize = 50
n_runs = 100
nodeStrengthRange = (0,.6)

def runSimulation(theNetwork, startingPoint, virus):

  if virus == "LB":
    virus = viruses.LogicBomb()
  if virus == "W":
    virus = viruses.Worm((0,.1))
  else:
    virus = viruses.Trojan()

  sim.runOnce(theNetwork, startingPoint, virus, False)

  infectedCount = 0
  for node in theNetwork.infectedList[1:]:
    if node == n.State.infected:
      infectedCount+= 1

  infectedPercent = (infectedCount / networkSize) * 100

  return infectedPercent

fileMaker.tree(networkSize)

infectedPercentRootTreeWorm   = []
infectedPercentMiddleTreeWorm = []
infectedPercentLeafTreeWorm = []

infectedPercentRootTreeLogicBomb   = []
infectedPercentMiddleTreeLogicBomb = []
infectedPercentLeafTreeLogicBomb = []

infectedPercentRootTreeTrojan   = []
infectedPercentMiddleTreeTrojan = []
infectedPercentLeafTreeTrojan = []

for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentRootTreeWorm.append(runSimulation(theNetwork, 1, "W"))

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentMiddleTreeWorm.append(runSimulation(theNetwork, int(networkSize/2), "W"))

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentLeafTreeWorm.append(runSimulation(theNetwork, networkSize, "W"))
  
virus = viruses.LogicBomb()  
for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentRootTreeLogicBomb.append(runSimulation(theNetwork, 1, "LB"))

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentMiddleTreeLogicBomb.append(runSimulation(theNetwork, int(networkSize/2), "LB"))

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentLeafTreeLogicBomb.append(runSimulation(theNetwork, networkSize, "LB"))

virus = viruses.Trojan()  
for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentRootTreeTrojan.append(runSimulation(theNetwork, 1, "T"))

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentMiddleTreeTrojan.append(runSimulation(theNetwork, int(networkSize/2), "T"))

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentLeafTreeTrojan.append(runSimulation(theNetwork, networkSize, "T"))

infectedPercentRootTreeWorm = N.array(infectedPercentRootTreeWorm)
infectedPercentMiddleTreeWorm = N.array(infectedPercentMiddleTreeWorm)
infectedPercentLeafTreeWorm = N.array(infectedPercentLeafTreeWorm)

infectedPercentRootTreeLogicBomb = N.array(infectedPercentRootTreeLogicBomb)
infectedPercentMiddleTreeLogicBomb = N.array(infectedPercentMiddleTreeLogicBomb)
infectedPercentLeafTreeLogicBomb = N.array(infectedPercentLeafTreeLogicBomb)

infectedPercentRootTreeTrojan = N.array(infectedPercentRootTreeTrojan)
infectedPercentMiddleTreeTrojan = N.array(infectedPercentMiddleTreeTrojan)
infectedPercentLeafTreeTrojan = N.array(infectedPercentLeafTreeTrojan)

meansWorm = [N.mean(infectedPercentRootTreeWorm),N.mean(infectedPercentMiddleTreeWorm), N.mean(infectedPercentLeafTreeWorm)]
meansLB   = [N.mean(infectedPercentRootTreeLogicBomb),N.mean(infectedPercentMiddleTreeLogicBomb), N.mean(infectedPercentLeafTreeLogicBomb)]
meansTrojan = [N.mean(infectedPercentRootTreeTrojan),N.mean(infectedPercentMiddleTreeTrojan), N.mean(infectedPercentLeafTreeTrojan)]

print(meansWorm)

bar_width = 0.125
bar_locations = N.array([1,1.5,2])
fig, ax = plt.subplots()
plt.bar(bar_locations, 
        meansWorm, bar_width, 
        alpha=.4, 
        color='r', 
        label='Worm')

plt.bar(bar_locations + bar_width, 
        meansLB, 
        bar_width, 
        alpha=.4,
        color='g',
        label='Logic Bomb')

plt.bar(bar_locations + (bar_width*2), 
        meansTrojan, 
        bar_width, 
        alpha=.4, 
        color='b', 
        label='Trojan')

plt.xticks(bar_locations+bar_width, ('Root', 'Middle','Leaf'))
plt.ylabel('percentage infected')
plt.xlabel('Infection location')
plt.title('Tree infection rate vs. initial infection location')
plt.legend()

plt.show()
fig.savefig('tree-start-locations.png')