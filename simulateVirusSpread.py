import Network as n
import displayVirusSpread as disp


def nowhereToGo(network):
  count = 1
  for node in network.infectedList[1:]:
    if node == n.state.infected:
      for neighbor in network.edges[count].adjacentNodes:
        if network.infectedList[neighbor] != n.state.infected and network.infectedList[neighbor] != n.state.immune:  
          return False
    count += 1
  return True

def runOnce(network, startingPoint, virus):
  network.infectedList[startingPoint] = n.state.infected
  simulationNotOver = True

  displayData = disp.dataToDisplay()
  displayData.typeOfGraph = network.networkType

  while simulationNotOver == True:
    hasNewAnimationInfo = False
    currentTurnMoves = []
    count = 1
    for node in network.infectedList[1:]:
      if node == n.state.infected:
        for neighbor in network.edges[count].adjacentNodes:
          if network.infectedList[neighbor] != n.state.infected:  
            if virus.infectOrNot(network, neighbor):
              currentTurnMoves.append((count, neighbor))
              network.infectedList[neighbor] = n.state.infected
              hasNewAnimationInfo = True
      count += 1
    
    for move in currentTurnMoves:
      network.infectedList[move[1]] = n.state.infected
    if hasNewAnimationInfo:
      displayData.animationSteps.append(currentTurnMoves)
    
    if nowhereToGo(network):
      simulationNotOver = False  
  disp.display(displayData)