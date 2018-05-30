import Network as net
from time import sleep
import fileMaker

# NONE = 0
# RING = 1
# STAR = 2
# MESH = 3
# ALL_CONNECTED = 4
# BUS = 5
# HYBRID = 6
# LINE = 7
# TREE = 8
for networkShape in range(1,9):
    maker = None
    fileName = None
    network = net.Network(networkShape)
    if(networkShape == 1):
        maker = fileMaker.ring
        fileName = "ring.txt"
    elif(networkShape == 2):
        maker = fileMaker.star
        fileName = "star.txt"
    elif(networkShape == 3):
        maker = fileMaker.mesh
        fileName = "mesh.txt"
    elif(networkShape == 4):
        maker = fileMaker.fullConnected
        fileName = "fullconnect.txt"
    elif(networkShape == 5):
        continue
    elif (networkShape == 6):
        continue
    elif (networkShape == 7):
        maker = fileMaker.line
        fileName = "line.txt"
    elif (networkShape == 8):
        maker = fileMaker.tree
        fileName = "tree.txt"
    else:
        print("Tests Failed, Invalid shape")
        break

    for x in range(2, 101, 1):
        maker(x)
        network.createnetwork(fileName)
        if(len(network.nodes) == x):
            print("Test",str(x), "Passed")
        else:
            print("Test", str(x), "Failed")
            break
        print(len(network.nodes))
print("Network Tests Completed")