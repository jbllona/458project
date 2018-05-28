import numpy as N
import Network
import time

""" this is an example virus, it has a 50% chance of infecting any neighboring viruses.
    Model all future viruses after this one, and make sure they have a function called 
    infectOrNot, with that same interface 
"""
class SuperVirus(object):
  chance = .5
  def infectOrNot(self, network, targetID):
    retVal = N.random.uniform()
    if retVal < self.chance:
      network.infectedList[targetID] = Network.State.infected
      return True
    else:
      return False

class LogicBomb(object):
    infectedCount = 0
    def infectOrNot(self, network, targetID):
        #get current time in milliseconds
        ms = int(round(time.time() * 1000))
        #Always infect if the network is 75% infected by this virus
        if(self.infectedCount>int(len(network.nodes)*.75)):
            network.infectedList[targetID] = Network.State.infected
            return True
        #of infect if the current time modulus 5 is 0
        elif(ms % 5 == 0):
            self.infectedCount+=1
            network.infectedList[targetID] = Network.State.infected
            return True
        return False

class Trojan(object):
  strength = N.random.uniform(0, .6)
 
  def infectOrNot(self, network, targetID):
    """ every turn, an infected node sends the virus
        to all neighbor nodes. This makes those nodes susceptible.
        On the next turn, a scceptable node is infected if its strength
        is less than that of the virus. If it does not become infected,
        it becomes immune, and cannot become susceptible or spread the virus."""
 
    retVal = None
 
    if network.infectedList[targetID] == Network.State.immune:
      retVal = False
    else:
      if network.infectedList[targetID] == Network.State.clean:
        network.infectedList[targetID] = Network.State.susceptible
        retVal = False
      elif network.infectedList[targetID] == Network.State.susceptible:
        if network.nodes[targetID].susceptibility < self.strength:
          network.infectedList[targetID] = Network.State.infected
          retVal = True
        else:
          network.infectedList[targetID] = Network.state.immune
          retVal = False
    return retVal

class Worm(object):
  infecteCount = 0
  # probability to successfully infect the system
  p_success = N.random.uniform(0, .8)

  def chooseTarget(self, network, source):
    # node that has the most number of neighbors that is not immune
    maxNode = None
    max_neighbor = 0
    for node in network.nodes[source].adjacentNodes:
      n_neighbor = len(network.nodes[node].adjacentNodes)
      if network.infectedList[node] != Network.State.immune and network.infectedList[node] != Network.State.infected:
        if (n_neighbor > max_neighbor):
          max_neighbor = n_neighbor
          maxNode = node
    return maxNode

  def infectOrNot(self, network, targetID, sourceID):
    target = self.chooseTarget(network, sourceID)
    # probability to get infected of the neighboring node that has the most
    # number of neighbors.
    if targetID == target:
      probability = network.nodes[target].susceptibility
      if probability > self.p_success:
        network.infectedList[target] = Network.State.immune
        return False
      else:
        # network.infectedList[targetID] = Network.state.infected
        return True
    else:
        return False