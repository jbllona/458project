import numpy as N

""" this is an example virus, it has a 50% chance of infecting any neighboring viruses.
    Model all future viruses after this one, and make sure they have a function called 
    infectOrNot, with that same interface 
"""
class SuperVirus:
  chance = .5
  def infectOrNot(self, network, nodeID):
    retVal = N.random.uniform() 
    return retVal < self.chance