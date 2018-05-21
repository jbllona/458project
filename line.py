
class Line:
       
    def __init__(self, txt):
        self.systems = []
        self.infected_systems = []
        self.add(txt)
        
    def add(textFile):
        fileobj = open("line.txt", "r")
        lines = fileobj.readlines()
        lines = [line.rstrip('\n') for line in lines]
        for i in range(len(lines)):
            # split from system and its neighboring system
            data = lines[i].split('\t')            
            # Create a system 
            # system1 = System(data[0])            
            # when we store neighbors, do we store them as int, string, or system            
            # neighbor system = System(data[1])
            # add_nighbor(system1, neighbor_system)            
            #systems.append(System1)
                
         
add("line.txt")

def add_neighbor(self, system1, system2):
    system1.neighbors.append(system2)
    system2.neighbors.append(system1)


def remove_system():
    return 0
    
