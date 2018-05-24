import displayVirusSpread as disp
import fileMaker as make
from time import sleep

displayData = disp.dataToDisplay()

# for current in range(5,15):
#     make.line(current)
#     sleep(1) # Time in seconds.
#     displayData.animationSteps.append([(1,2)])
#     disp.LINE_GRAPH = disp.drawGraphFromFile('line.txt')
#     displayData.typeOfGraph = disp.graphType.LINE
#     disp.display(displayData)
# 
# for current in range(5,15):
#     make.ring(current)
#     sleep(1) # Time in seconds.
#     displayData.animationSteps.append([(1,2)])
#     disp.RING_GRAPH = disp.drawGraphFromFile('ring.txt')
#     displayData.typeOfGraph = disp.graphType.RING
#     disp.display(displayData)
    
# for current in range(5,15):
#     make.star(current)
#     displayData.animationSteps.append([(1,2)])
#     disp.STAR_GRAPH = disp.drawGraphFromFile('star.txt')
#     displayData.typeOfGraph = disp.graphType.STAR
#     disp.display(displayData)

#cannot make files larger than 11
#Also always does 11 computer no matter what
# for current in range(5,11):
#     make.fullConnected(current)
#     sleep(1) # Time in seconds.
#     displayData.animationSteps.append([(1,2)])
#     disp.ALL_CONNECTED_GRAPH = disp.drawGraphFromFile('fullconnect.txt')
#     displayData.typeOfGraph = disp.graphType.ALL_CONNECTED
#     disp.display(displayData)

# for current in range(5,15):
    # make.tree(current)
    # sleep(1) # Time in seconds.
    # displayData.animationSteps.append([(1,2)])
    # disp.TREE_GRAPH = disp.drawGraphFromFile('tree.txt')
    # displayData.typeOfGraph = disp.graphType.TREE
    # disp.display(displayData)
#Always does 11 computer no matter what   
for current in range(5,15):
    make.mesh(current)
    sleep(1) # Time in seconds.
    displayData.animationSteps.append([(1,2)])
    disp.MESH_GRAPH = disp.drawGraphFromFile('mesh.txt')
    displayData.typeOfGraph = disp.graphType.MESH
    disp.display(displayData)