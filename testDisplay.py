import displayVirusSpread as disp

displayData = disp.dataToDisplay()
displayData.startNodes.append(1)
displayData.typeOfGraph = disp.graphType.STAR

disp.display(displayData)