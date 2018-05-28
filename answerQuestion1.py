import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import fileMaker
import numpy as N

networkSize = 100


nodeStrengthRange = (0,1)
def runWorm():
  startingPoint = N.random.randint(1,networkSize+1)

  fileMaker.mesh(networkSize)

  virus = viruses.Worm()
  theNetwork = n.Network(disp.graphType.MESH)
  theNetwork.createnetwork("mesh.txt", nodeStrengthRange)
  sim.runOnce(theNetwork, startingPoint, virus, False)

  infectedCount = 0
  for node in theNetwork.infectedList[1:]:
    if node == n.State.infected:
      infectedCount+= 1

  infectedPercent = (infectedCount / networkSize) * 100

  return infectedPercent

def runLB():
  startingPoint = N.random.randint(1,networkSize+1)

  fileMaker.mesh(networkSize)

  virus = viruses.LogicBomb()
  theNetwork = n.Network(disp.graphType.MESH)
  theNetwork.createnetwork("mesh.txt", nodeStrengthRange)
  sim.runOnce(theNetwork, startingPoint, virus, False)

  infectedCount = 0
  for node in theNetwork.infectedList[1:]:
    if node == n.State.infected:
      infectedCount+= 1

  infectedPercent = (infectedCount / networkSize) * 100

  return infectedPercent

def runTrojan():
  startingPoint = N.random.randint(1,networkSize+1)

  fileMaker.mesh(networkSize)

  virus = viruses.Trojan()
  theNetwork = n.Network(disp.graphType.MESH)
  theNetwork.createnetwork("mesh.txt", nodeStrengthRange)
  sim.runOnce(theNetwork, startingPoint, virus, False)

  infectedCount = 0
  for node in theNetwork.infectedList[1:]:
    if node == n.State.infected:
      infectedCount+= 1

  infectedPercent = (infectedCount / networkSize) * 100

  return infectedPercent

infectedPercentWorm = []
infectedPercentLogicBomb = []
infectedPercentTrojan = []

for x in range(100):
  print(x)
  infectedPercentWorm.append(runWorm())
  infectedPercentLogicBomb.append(runLB())
  infectedPercentTrojan.append(runTrojan())
  
infectedPercentWorm = N.array(infectedPercentWorm)
infectedPercentLogicBomb = N.array(infectedPercentLogicBomb)
infectedPercentTrojan = N.array(infectedPercentTrojan)
print(N.mean(infectedPercentWorm),N.mean(infectedPercentLogicBomb),N.mean(infectedPercentTrojan))