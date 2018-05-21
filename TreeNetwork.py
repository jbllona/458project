# -*- coding: utf-8 -*-
import numpy as N

class TreeNetwork(object):
    def __init__(self):
        self.root = None
        self.verteces = []
        
    def add(self, filename):
        
        fileobj = open('tree.txt', 'r')
        data_str = fileobj.readlines()
        
        for i in range(len(data_str)):
            split_istr = data_str[i].split('\t')
            if (split_istr.size() == 1):
                self.root = system(int(split_istr[0]))
            else:
                source = int(split_istr[0])
                dest = int(split_istr[1])
                self.addHelper(self.root, source, dest)
        
        fileobj.close()
                
                
    def addHelper(self, root, source, dest):
        if (root.nodeNumber == source):
            root.neighbors.append(dest)
        else:
            for i in range(root.neighbors.size()):
                self.addHelper(root.neighbors[i])       
        return root
        
    
    
        
        
        