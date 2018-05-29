import Network as n
import displayVirusSpread as disp


def nowhereToGo(network):
  count = 1
  for node in network.infectedList[1:]:
    if node == n.State.infected:
      for neighbor in network.nodes[count].adjacentNodes:
        if network.infectedList[neighbor] != n.State.infected and network.infectedList[neighbor] != n.State.immune:  
          return False
    count += 1
  return True

def runOnce(network, startingPoint, virus, displayAnimation = True):
  network.infectedList[startingPoint] = n.State.infected
  simulationNotOver = True

  displayData = disp.dataToDisplay()
  displayData.typeOfGraph = network.networkType

  while simulationNotOver == True:
    hasNewAnimationInfo = False
    currentTurnMoves = []
    # currentNodeID = 1
    for x in range(1, len(network.infectedList)):
      if network.infectedList[x] == n.State.infected:
        for neighbor in network.nodes[x].adjacentNodes:
          if network.infectedList[neighbor] != n.State.infected:  
            if virus.infectOrNot(network, neighbor, x):
              currentTurnMoves.append((x, neighbor))
              hasNewAnimationInfo = True

    for move in currentTurnMoves:
      network.infectedList[move[1]] = n.State.infected
    if hasNewAnimationInfo:
      displayData.animationSteps.append(currentTurnMoves)
    
    if nowhereToGo(network):
      simulationNotOver = False  
      if displayAnimation:
        disp.display(displayData)