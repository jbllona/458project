import Network as n
import displayVirusSpread as disp
import numpy as N
import matplotlib.pyplot as plt

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

  steps = []
  count = 0
  steps.append(count)
  percent_infected = []
  percent_infected.append(percentage(network))
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
    print(percentage(network))
    for move in currentTurnMoves:
      network.infectedList[move[1]] = n.State.infected

    if hasNewAnimationInfo:
      displayData.animationSteps.append(currentTurnMoves)
      count += 1
      steps.append(count)
    if nowhereToGo(network):
      simulationNotOver = False  
  
  print(steps)
  print(percent_infected)
  if displayAnimation:
    disp.display(displayData)
  return percent_infected, steps
  

def percentage(network):
  newList = N.array(network.infectedList)
  infected_nodes = N.where(newList == n.State.infected)
  print(infected_nodes)
  return 100.0 * len(infected_nodes) / len(network.nodes)


  # draw a xy plot that shows the percentage of infected system in network per step 
def drawGraph(time_turns, percentage):
    fig1 = plt.figure() # plot time turns vs percentage of infected network/system
    plt.title("Infected rate per steps")
    plt.xlabel("Time steps")
    plt.ylabel("percentage of infection")
    plt.plot(time_turns, percentage)
    plt.show()