import System
            
        
class Network:
    
    """
        Create and manage a graph representing network.
        
    """ 

    NETWORK_TYPE = {1 : "linear", 2 : "mesh", 3 : "ring", 4 : "star", 5 : "tree"}
    
    def __init__(self, txt, directed=False):
        self.systems = []  
        self.infected_systems = []		
        self.directed = directed


    def create_network(shape, txt):
        if shape == 1:
            line_network(txt)
        elif shape == 2:
            mesh_network(txt)
        elif shape == 3:
            ring_network(txt)
        elif shape == 4:
            star_network(txt)
        elif shape == 5:
            tree_network(txt)
            
    def mesh_network(txt):
        
    def ring_network(txt):
        
    def star_network(txt):

    def tree_network(txt):
