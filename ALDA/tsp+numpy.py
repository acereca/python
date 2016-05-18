import numpy as np
import sys

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
print(i+1)
import matplotlib
import matplotlib.pyplot as plt
#plt.plot(nodes[:,0],nodes[:,1],linestyle='none',marker=".")
#plt.show()
