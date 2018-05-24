
class System(object):
    """ Create and manage a system, which is going to be a node for our graph.
    
    Attributes 
    ==========
    state: int 
        current state of servers: Immune(0), susceptible(1), infected(2)
                                    , or Recovered(3)
    
    neighbors: 
        a list of neighbor systems. 
    """
        
    # IMMUNE = 0
    # SUSCEPTIBLE = 1
    # INFECTED = 2
    # RECOVERED = 3

    def __init__(self, number):
        self.state = 1
        self.nodeNumber = number
        self.edges = []

    def get_state(self):
        return self.state
        
    def infect_system(self):
        self.state = 2
    
    def recover_system(self):
        self.state = 3
        
    def immune_system(self):
        self.state = 0
        
    def print_state(self):
        if self.state == 0:
            return "System is Immune"
        elif self.state == 1:
            return "System is Susceptible"
        elif self.state == 2:
            return "System is Infected"
        elif self.state == 3:
            return "System is Recovered"
        else:
            return "Wrong state"