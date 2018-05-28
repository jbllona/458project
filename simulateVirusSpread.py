import Network as n
import displayVirusSpread as disp
import numpy as N

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
  network.infectedList[startingPoint] = n.State.infected
  simulationNotOver = True

  displayData = disp.dataToDisplay()
  displayData.typeOfGraph = network.networkType

  # list of percentage of infected systems in network
  percent_infected = []
  percent_infected.append(percentage(network)) # initial percentage before simulation
  steps = []
  count = 0
  steps.append(count)


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
      percent_infected.append(percentage(network))

    for move in currentTurnMoves:
      network.infectedList[move[1]] = n.state.infected
    if hasNewAnimationInfo:
      displayData.animationSteps.append(currentTurnMoves)
      count += 1
      steps.append[count]
    
    if nowhereToGo(network):
      simulationNotOver = False  
  if (displayAnimation):
    disp.display(displayData)
  return displayData.animationSteps, percent_infected


# function to calculate the infection percentage of network. 
def percentage(network):
  newList = N.array(network.infectedList)
  print(newList)
  infected_nodes = N.where(network.infectedList == n.State.infected)
  return 100.0 * len(network.infectedList) / len(network.nodes)


# draw a xy plot that shows the percentage of infected system in network per step 
def drawGraph(time_turns, percentage):
    fig1 = plt.figure() # plot time turns vs percentage of infected network/system
    plt.title("Infected rate per steps")
    plt.xlabel("Time steps")
    plt.ylabel("percentage of infection")
    plt.plot(time_turns, percentage)
    plt.show()

