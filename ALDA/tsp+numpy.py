import numpy as np
import sys

from classes import *

def readTspData(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        clean = [x.lstrip() for x in content if x != ' ']
        tupel = []

        for item in clean:
            if item[:1].isdigit():
                c1,space,c2 = item.partition(' ')
                b1,space,b2 = c2.partition(' ')
                tupel.append((int(c1.strip()),float(b1.strip()),float(b2.strip())))
    return tupel

tspData = readTspData(sys.argv[1])
nodes = np.array(tspData)[:,1:]
# nearest neighbor search in numpy
diff = nodes.reshape(nodes.shape[0],1,2) - nodes
D = (diff ** 2).sum(2)
i = np.arange(nodes.shape[0])
D[i,i] = np.inf
i = np.argmin(D,1)
# output nearest neighbor by node nr

#import matplotlib
#import matplotlib.pyplot as plt
#plt.plot(nodes[:,0],nodes[:,1],linestyle='none',marker=".")
#plt.show()

g = Graph()

for elem in tspData:
    #print(elem)
    g.add_vertex(elem[0])
    
for elem in range(len(diff)):
    for inner in range(len(diff[elem])):
        dist = numpy.sqrt(diff[elem,inner,0]**2+diff[elem,inner,1]**2)
        g.add_edge(elem,inner,dist)
        print(elem,inner,dist)
        
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print('( %s , %s, %d)'  % ( vid, wid, v.get_weight(w)))
