

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
        
    IMMUNE = 0
    SUSCEPTIBLE = 1
    INFECTED = 2
    RECOVERED = 3
    
        
    def __init__(self, state=rand()%2):
        self.state = state
        self.neighbors = []

    def getState(self):
        return self.state
        
    def infectSystem(self):
        self.state = 2
        
    def show_state(self, server):
        if server.state == 0:
            return "Immune System"
        elif server.state == 1:
            return "Susceptible System"
        elif server.state == -1:
            return "Infected System"
        elif server.state == 2:
            return "Recovered System"
        else:
            "Wrong state"
        
     
            
        