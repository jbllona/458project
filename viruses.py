import numpy as N
import Network
import time

""" this is an example virus, it has a 50% chance of infecting any neighboring viruses.
    Model all future viruses after this one, and make sure they have a function called 
    infectOrNot, with that same interface 
"""
class SuperVirus:
  chance = .5
  def infectOrNot(self, network, nodeID):
    retVal = N.random.uniform() 
    return retVal < self.chance

class logicBomb:
    infectedCount = 0
    def infectOrNot(self, network, nodeID):
        #get current time in milliseconds
        ms = int(round(time.time() * 1000))
        #Always infect if the network is 75% infected by this virus
        if(self.infectedCount>int(len(network.edges)*.75)):
            return True
        #of infect if the current time modulus 5 is 0
        elif(ms % 5 == 0):
            self.infectedCount+=1
            return True
        return False

class trojan:
  strength = N.random.uniform(0, .6)
 
  def infectOrNot(self, network, nodeID):
    """ every turn, an infected node sends the virus
        to all neighbor nodes. This makes those nodes suceptable.
        On the next turn, a scceptable node is infected if its strength
        is less than that of the virus. If it does not become infected,
        it becomes immune, and cannot become suceptable or spread the virus."""
 
    retVal = None
 
    if network.infectedList[nodeID] == Network.state.immune:
      retVal = False
    else:
      if network.infectedList[nodeID] == Network.state.clean:
        network.infectedList[nodeID] = Network.state.suceptable
        retVal = False
      elif network.infectedList[nodeID] == Network.state.suceptable:
        if network.edges[nodeID].suceptibility < self.strength:
          retVal = True
        else:
          network.infectedList[nodeID] = Network.state.immune
 
    return retVal

class worm:
  infecteCount = 0
  # probability to successfully infect the system
  self.p_success = N.random.uniform(0, 1)

  def chooseTarget(self, network, count):
    # node that has the most number of neighbors
    maxNode = None
    max_neighbor = 0
    for node in network.edges[count].adjacentNodes:
      n_neighbor = len(node.adjacentNodes)
      if (n_neighbor > max_neighbor):
        max_neighbor = n_neighbor
        maxNode = node
    return maxNode

  def infectOrNot(self, network, nodeID):
    target = self.chooseTarget(network, count)
    # probability to get infected of the neighboring node that has the most
    # number of neighbors.
    probability = network.edges[nodeID].adjacentNodes[target].p_infected 
    return probability < self.p_success
