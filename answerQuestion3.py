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

def runWorm(theNetwork, startingPoint):

  virus = viruses.LogicBomb()
  sim.runOnce(theNetwork, startingPoint, virus, False)

  infectedCount = 0
  for node in theNetwork.infectedList[1:]:
    if node == n.State.infected:
      infectedCount+= 1

  infectedPercent = (infectedCount / networkSize) * 100

  return infectedPercent

fileMaker.tree(networkSize)

infectedPercentRootTree   = []
infectedPercentMiddleTree = []
infectedPercentLeafTree = []

for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentRootTree.append(runWorm(theNetwork, 1))

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentMiddleTree.append(runWorm(theNetwork, int(networkSize/2)))

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentLeafTree.append(runWorm(theNetwork, networkSize))
  
infectedPercentRootTree = N.array(infectedPercentRootTree)
infectedPercentMiddleTree = N.array(infectedPercentMiddleTree)
infectedPercentLeafTree = N.array(infectedPercentLeafTree)

means = [N.mean(infectedPercentRootTree),N.mean(infectedPercentMiddleTree), N.mean(infectedPercentLeafTree)]

print(means)

bar_width = 0.4
bar_locations = N.array([1,1.5,2])
fig, ax = plt.subplots()
plt.bar(bar_locations, means, bar_width, alpha=.4, color='g')
plt.xticks(bar_locations, ('Root', 'Middle','Leaf'))
plt.ylabel('percentage infected')
plt.xlabel('Infection location')
plt.title('Tree infection rate vs. initial infection location')
plt.text(bar_locations[0],means[0], str(round(means[0],2)), ha='center', color='b')
plt.text(bar_locations[1],means[1], str(round(means[1],2)), ha='center', color='b')
plt.text(bar_locations[2],means[2], str(round(means[2],2)), ha='center', color='b')
plt.show()
fig.savefig('tree-start-locations.png')