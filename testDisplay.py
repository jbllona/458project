import displayVirusSpread as disp

displayData = disp.dataToDisplay()
displayData.startNodes.append(1)
displayData.animationSteps.append([(1,2),(1,4)])
displayData.animationSteps.append([(1,3),(1,5),(1,6)])
displayData.animationSteps.append([(1,7),(1,8)])
displayData.typeOfGraph = disp.graphType.STAR
disp.display(displayData)