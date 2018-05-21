import displayVirusSpread as disp

displayData = disp.dataToDisplay()
# # displayData.startNodes.append(1)
# displayData.animationSteps.append([(1,2),(1,4)])
# displayData.animationSteps.append([(1,3),(1,5),(1,6)])
# displayData.animationSteps.append([(1,7),(1,8)])
# displayData.typeOfGraph = disp.graphType.STAR

# displayData.animationSteps.append([(1,2), (1,8)])
# displayData.animationSteps.append([(2,3), (8,7)])
# displayData.typeOfGraph = disp.graphType.RING

displayData.animationSteps.append([(1,2), (1,8), (1,3)])
displayData.animationSteps.append([(3,4), (3,5)])
displayData.typeOfGraph = disp.graphType.MESH

disp.display(displayData)