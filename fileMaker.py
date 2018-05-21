import numpy as np
# -*- coding: utf-8 -*-
def line(maxNode):
    fileName = "line"+str(maxNode)+".txt"
    File = open(fileName,"w")
    
    for x in range(1,maxNode):
        writePairs(File, x, x+1)
    File.close()
    
    print("Line File made. File is named ", fileName)
    
def fullConnected(maxNode):
    record = np.zeros((maxNode+1,maxNode+1),dtype=bool)
    fileName = "fullyConnected"+str(maxNode)+".txt"
    File = open(fileName,"w")
    
    for x in range(1,maxNode):
    #create ring of values:
        writePairs(File, x, x+1)
        record[x, x+1] = True;
        record[x+1, x] = True;
        record[x, x] = True;
    record[maxNode, maxNode] = True;
    for y in range(1,maxNode+1):
        for x in range(1,maxNode+1):
            if(record[y, x] == False):
                writePairs(File, x, y)
                record[y, x] = True;
                record[x, y] = True;
                
    File.close()
    print("Fully connected File made. File is named ", fileName)
    
def mesh(maxNode):
    pass
    
def ring(maxNode):
    fileName = "ring"+str(maxNode)+".txt"
    File = open(fileName,"w")
    
    for x in range(1,maxNode):
        writePairs(File, x, x+1)
    writePairs(File, maxNode, 1)
    
    File.close()
    print("Ring File made. File is named ", fileName)
    
def star(maxNode):
    fileName = "star"+str(maxNode)+".txt"
    File = open(fileName,"w")
    
    for x in range(1,maxNode):
        writePairs(File, 1, x+1)
    File.close()
    
    print("Star File made. File is named ", fileName)
    
def tree(maxNode):
    fileName = "tree"+str(maxNode)+".txt"
    File = open(fileName,"w")

    currentNode = 1
    currentMaxNode = 2
    
    while(currentMaxNode <= maxNode):
        if currentNode*2 <= maxNode:
            writePairs(File, currentNode, currentMaxNode)
            currentMaxNode+=1
        if currentNode*2 +1 <= maxNode:
            writePairs(File, currentNode, currentMaxNode)
            currentMaxNode+=1
        currentNode+=1
    File.close()
    print("Tree File made. File is named ", fileName)

def writePairs(File, val1, val2):         
    File.write(str(val1))
    File.write("\t")
    File.write(str(val2))
    File.write("\n")

def main(maxNumber):
    line(maxNumber)
    ring(maxNumber)
    star(maxNumber)
    tree(maxNumber)
    fullConnected(maxNumber)