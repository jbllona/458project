# -*- coding: utf-8 -*-
import numpy as N
from Network import Network

filename = 'mesh.txt'
network = Network('mesh')
network.createnetwork(filename)
print(network.edges)
