import numpy as N
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
    infectedCount = 0;
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
        