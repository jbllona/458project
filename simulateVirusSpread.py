import Network as n
import displayVirusSpread as disp


def allInfected(network):
  for node in network.infectedList:
    if node == n.state.clean:
      return False
  return True

def runOnce(network, startingPoint, virus):
  network.infectedList[startingPoint] = n.state.infected
  simulationNotOver = True

  displayData = disp.dataToDisplay()
  displayData.typeOfGraph = network.networkType

  while simulationNotOver == True:
    currentTurnMoves = []
    count = 1
    for node in network.infectedList[1:]:
      if node == n.state.infected:
        # when virus is not a worm:
        if type(virus) != Worm:
          for neighbor in network.edges[count].adjacentNodes:
            if network.infectedList[neighbor] != n.state.infected: 
              if virus.infectOrNot(network, neighbor):
                currentTurnMoves.append((count, neighbor))
                network.infectedList[neighbor] = n.state.infected
        # when a type of the virus is a worm    
        else:
          # choose the target to infect
          neighbor = virus.chooseTarget(network, count)
            if network.infectedList[neighbor] != n.state.infected: 
              if virus.infectOrNot(network, neighbor)):
                currentTurnMoves.append((count, neighbor))
                network.infectedList[neighbor] = n.state.infected
      count += 1

    for move in currentTurnMoves:
      network.infectedList[move[1]] = n.state.infected
    displayData.animationSteps.append(currentTurnMoves)
    
    if allInfected(network):
      simulationNotOver = False  
  disp.display(displayData)