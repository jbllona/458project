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

def runWorm(theNetwork):
  startingPoint = N.random.randint(1,networkSize+1)

  virus = viruses.Worm((0, .3))
  sim.runOnce(theNetwork, startingPoint, virus, False)

  infectedCount = 0
  for node in theNetwork.infectedList[1:]:
    if node == n.State.infected:
      infectedCount+= 1

  infectedPercent = (infectedCount / networkSize) * 100

  return infectedPercent

def runLB(theNetwork):
  startingPoint = N.random.randint(1,networkSize+1)
  
  virus = viruses.LogicBomb()
  sim.runOnce(theNetwork, startingPoint, virus, False)

  infectedCount = 0
  for node in theNetwork.infectedList[1:]:
    if node == n.State.infected:
      infectedCount+= 1

  infectedPercent = (infectedCount / networkSize) * 100

  return infectedPercent

def runTrojan(theNetwork):
  startingPoint = N.random.randint(1,networkSize+1)
  
  virus = viruses.Trojan()
  sim.runOnce(theNetwork, startingPoint, virus, False)

  infectedCount = 0
  for node in theNetwork.infectedList[1:]:
    if node == n.State.infected:
      infectedCount+= 1

  infectedPercent = (infectedCount / networkSize) * 100

  return infectedPercent

# run for mesh network
infectedPercentWormMesh = []
infectedPercentLogicBombMesh = []
infectedPercentTrojanMesh = []

for x in range(n_runs):
  print(x)

  fileMaker.mesh(networkSize)
  theNetwork = n.Network(disp.graphType.MESH)
  theNetwork.createnetwork("mesh.txt", nodeStrengthRange)

  infectedPercentWormMesh.append(runWorm(theNetwork))
  infectedPercentLogicBombMesh.append(runLB(theNetwork))
  infectedPercentTrojanMesh.append(runTrojan(theNetwork))
  
infectedPercentWormMesh = N.array(infectedPercentWormMesh)
infectedPercentLogicBombMesh = N.array(infectedPercentLogicBombMesh)
infectedPercentTrojanMesh = N.array(infectedPercentTrojanMesh)


#run for all connected network
infectedPercentWormAllConnected = []
infectedPercentLogicBombAllConnected = []
infectedPercentTrojanAllConnected = []

fileMaker.fullConnected(networkSize)
for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.ALL_CONNECTED)
  theNetwork.createnetwork("fullconnect.txt", nodeStrengthRange)

  infectedPercentWormAllConnected.append(runWorm(theNetwork))
  infectedPercentLogicBombAllConnected.append(runLB(theNetwork))
  infectedPercentTrojanAllConnected.append(runTrojan(theNetwork))
  
infectedPercentWormAllConnected = N.array(infectedPercentWormAllConnected)
infectedPercentLogicBombAllConnected = N.array(infectedPercentLogicBombAllConnected)
infectedPercentTrojanAllConnected = N.array(infectedPercentTrojanAllConnected)

#run for line network
infectedPercentWormLine = []
infectedPercentLogicBombLine = []
infectedPercentTrojanLine = []

fileMaker.line(networkSize)


for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.LINE)
  theNetwork.createnetwork("line.txt", nodeStrengthRange)

  infectedPercentWormLine.append(runWorm(theNetwork))
  infectedPercentLogicBombLine.append(runLB(theNetwork))
  infectedPercentTrojanLine.append(runTrojan(theNetwork))
  
infectedPercentWormLine = N.array(infectedPercentWormLine)
infectedPercentLogicBombLine = N.array(infectedPercentLogicBombLine)
infectedPercentTrojanLine = N.array(infectedPercentTrojanLine)

#run for ring network
infectedPercentWormRing = []
infectedPercentLogicBombRing = []
infectedPercentTrojanRing = []

fileMaker.ring(networkSize)


for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.RING)
  theNetwork.createnetwork("ring.txt", nodeStrengthRange)

  infectedPercentWormRing.append(runWorm(theNetwork))
  infectedPercentLogicBombRing.append(runLB(theNetwork))
  infectedPercentTrojanRing.append(runTrojan(theNetwork))
  
infectedPercentWormRing = N.array(infectedPercentWormRing)
infectedPercentLogicBombRing = N.array(infectedPercentLogicBombRing)
infectedPercentTrojanRing = N.array(infectedPercentTrojanRing)

#run for star network
infectedPercentWormStar = []
infectedPercentLogicBombStar = []
infectedPercentTrojanStar = []

fileMaker.star(networkSize)


for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.STAR)
  theNetwork.createnetwork("star.txt", nodeStrengthRange)

  infectedPercentWormStar.append(runWorm(theNetwork))
  infectedPercentLogicBombStar.append(runLB(theNetwork))
  infectedPercentTrojanStar.append(runTrojan(theNetwork))
  
infectedPercentWormStar = N.array(infectedPercentWormStar)
infectedPercentLogicBombStar = N.array(infectedPercentLogicBombStar)
infectedPercentTrojanStar = N.array(infectedPercentTrojanStar)

#run for tree network
infectedPercentWormTree = []
infectedPercentLogicBombTree = []
infectedPercentTrojanTree = []

fileMaker.tree(networkSize)


for x in range(n_runs):
  print(x)

  theNetwork = n.Network(disp.graphType.TREE)
  theNetwork.createnetwork("tree.txt", nodeStrengthRange)

  infectedPercentWormTree.append(runWorm(theNetwork))
  infectedPercentLogicBombTree.append(runLB(theNetwork))
  infectedPercentTrojanTree.append(runTrojan(theNetwork))
  
infectedPercentWormTree = N.array(infectedPercentWormTree)
infectedPercentLogicBombTree = N.array(infectedPercentLogicBombTree)
infectedPercentTrojanTree = N.array(infectedPercentTrojanTree)

print("Mesh:\t\t",N.mean(infectedPercentWormMesh), N.mean(infectedPercentLogicBombMesh), N.mean(infectedPercentTrojanMesh))
print("All connected:\t",N.mean(infectedPercentWormAllConnected), N.mean(infectedPercentLogicBombAllConnected), N.mean(infectedPercentTrojanAllConnected))
print("Line:\t\t",N.mean(infectedPercentWormLine), N.mean(infectedPercentLogicBombLine), N.mean(infectedPercentTrojanLine))
print("Ring:\t\t",N.mean(infectedPercentWormRing), N.mean(infectedPercentLogicBombRing), N.mean(infectedPercentTrojanRing))
print("Star:\t\t",N.mean(infectedPercentWormStar), N.mean(infectedPercentLogicBombStar), N.mean(infectedPercentTrojanStar))
print("Tree:\t\t",N.mean(infectedPercentWormTree), N.mean(infectedPercentLogicBombTree), N.mean(infectedPercentTrojanTree))

means_worm = N.array([N.mean(infectedPercentWormMesh), N.mean(infectedPercentWormAllConnected), N.mean(infectedPercentWormLine), N.mean(infectedPercentWormRing), N.mean(infectedPercentWormStar), N.mean(infectedPercentWormTree)])

means_logicBomb = N.array([N.mean(infectedPercentLogicBombMesh), N.mean(infectedPercentLogicBombAllConnected), N.mean(infectedPercentLogicBombLine), N.mean(infectedPercentLogicBombRing), N.mean(infectedPercentLogicBombStar), N.mean(infectedPercentLogicBombTree)])

means_trojan = N.array([N.mean(infectedPercentTrojanMesh), N.mean(infectedPercentTrojanAllConnected), N.mean(infectedPercentTrojanLine), N.mean(infectedPercentTrojanRing), N.mean(infectedPercentTrojanStar), N.mean(infectedPercentTrojanTree)])

fig, ax = plt.subplots()
bar_width = 0.25

opacity = 0.4

index = N.arange(6)

rects1 = ax.bar(index, means_worm, bar_width,
                alpha=opacity, color='r',
                label='Worm')

rects2 = ax.bar(index + bar_width, means_logicBomb, bar_width,
                alpha=opacity, color='g',
                label='Logic Bomb')

rects3 = ax.bar(index + (bar_width * 2), means_trojan, bar_width,
                alpha=opacity, color='b',
                label='Trojan')

ax.set_xlabel('Malware Type')
ax.set_ylabel('Percentage of network infected')
ax.set_title('Percentage of network infected by network type')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(('Mesh', 'Connected', 'Line', 'Ring', 'Star', 'Tree'))
ax.legend()

fig.tight_layout()
plt.show()
fig.savefig('virus-success-with-every-network.png')