"""
answerQuestion13

Description: This file is meant to answer question 13 of our analysis questions.
            Is the rate that a malware propagates consistent throughout the entire simulation?
            
            This program will create 6 line graphs for each network to show the 
            infection rate over time. It should be noted that this program run 
            the simulation only once because each simulation has a dynamic length.
            This makes it hard to run it multiple times and average them

Notes: By default, the program will use any files that already exist. If you would 
        like this progam to generate the files, uncomment the fileMaker.main 
        command
        
        If a file is blank, this is because the network was immune and there
        was nothing to plot
"""
import simulateVirusSpread as sim
import displayVirusSpread as disp
import viruses
import Network as n
import matplotlib.pyplot as plt




def drawGraph(time_turns, rates, virusName, graphType):
    """
    This method will generate the scatter plot for a given network.
    
    Input: infectionRates: a list of Infection rates for the 100 simulations
            percentages: a list of precentages of total network infected 
                        for the 100 simulations
            virusName: A string of the virus name
            graphType: A string of the name of the network
            
    After Running: A image file will be create called Rate of Infection 
                    by %_NetowrkShape
    
    """
    title = "Rate of Infection by a "+virusName +" in a "+graphType+" Network"
    fileName = virusName+"_"+graphType + ".png"
    plt.figure() # plot time turns vs percentage of infected network/system
    plt.ylabel("Infection rate per step")
    plt.xlabel("Network Cycles")
    plt.title(title)
    plt.plot(range(time_turns), rates)
    plt.savefig(fileName)
    
#fileMaker.main(50)

Types = ["Worm", "Trojan", "Logic Bomb"]
virus = [viruses.Worm(), viruses.Trojan(), viruses.LogicBomb()]

#create 6 line graphs of the rate of infection over time.
for x in range(3):
    theNetwork = n.Network(disp.graphType.LINE)
    theNetwork.createnetwork("line.txt")
    numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, virus[x], False)
    drawGraph(numberOfSteps, infectionRates, Types[x], "Line")

    theNetwork = n.Network(disp.graphType.RING)
    theNetwork.createnetwork("ring.txt")
    numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, virus[x], False)
    drawGraph(numberOfSteps, infectionRates, Types[x], "Ring")

    theNetwork = n.Network(disp.graphType.MESH)
    theNetwork.createnetwork("mesh.txt")
    numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, virus[x], False)
    drawGraph(numberOfSteps, infectionRates, Types[x], "Mesh")

    theNetwork = n.Network(disp.graphType.ALL_CONNECTED)
    theNetwork.createnetwork("fullconnect.txt")
    numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, virus[x], False)
    drawGraph(numberOfSteps, infectionRates, Types[x], "Fully Connected")

    theNetwork = n.Network(disp.graphType.STAR)
    theNetwork.createnetwork("star.txt")
    numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, virus[x], False)
    drawGraph(numberOfSteps, infectionRates, Types[x], "Star")
    
    theNetwork = n.Network(disp.graphType.TREE)
    theNetwork.createnetwork("tree.txt")
    numberOfSteps, infectionRates, percentatages = sim.runOnce(theNetwork, 1, virus[x], False)
    drawGraph(numberOfSteps, infectionRates, Types[x], "Tree")

