from system import System


class Network(object):

    def __init__(self, type):
        self.nodes = []
        self.edges = {}
        self.networktype = type

    def createnetwork(self, filename):
        fileobj = open(filename, 'r')
        lines = fileobj.readlines()
        
        for i in range(len(lines)):
            split_line = lines[i].split('\t')
            split_line[1] = split_line[1].split('\n')[0]

            found = False
            for node in self.nodes:
                if node.nodeNumber == split_line[0]:
                    self.edges[split_line[0]].append(split_line[1])
                    found = True

            if found is False:
                newNode = System(split_line[0])
                self.nodes.append(newNode)
                edgeList = []
                edgeList.append(split_line[1])
                self.edges[split_line[0]] = edgeList
            
        fileobj.close()

