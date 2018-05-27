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

def runOnce(network, startingPoint, virus, displayAnimation = True):
  network.infectedList[startingPoint] = n.state.infected
  simulationNotOver = True

  displayData = disp.dataToDisplay()
  displayData.typeOfGraph = network.networkType

  # list of percentage of infected systems in network
  percent_infected = []
  percent_infected.append(percentage(network)) # initial percentage before simulation

  while simulationNotOver == True:
    hasNewAnimationInfo = False
    currentTurnMoves = []
    # currentNodeID = 1
    for x in range(1, len(network.infectedList)):
      if network.infectedList[x] == n.state.infected:
        for neighbor in network.edges[x].adjacentNodes:
          if network.infectedList[neighbor] != n.state.infected:  
            if virus.infectOrNot(network, neighbor, x):
              currentTurnMoves.append((x, neighbor))
              hasNewAnimationInfo = True

    for move in currentTurnMoves:
      network.infectedList[move[1]] = n.state.infected
    if hasNewAnimationInfo:
      displayData.animationSteps.append(currentTurnMoves)
      
      percent_infected.append(percentage(network))
    
    if nowhereToGo(network):
      simulationNotOver = False  
  disp.display(displayData)
  drawGraph(displayData.animationSteps, percent_infected)
  #return displayData.animationSteps


# function to calculate the infection percentage of network. 
def percentage(network):
  return len(network.infectedList) / len(network.node) * 100


# draw a xy plot that shows the percentage of infected system in network per step 
def drawGraph(time_turns, percentage):
    fig1 = plt.figure() # plot time turns vs percentage of infected network/system
    fig1.plot(time_turns, percentage)