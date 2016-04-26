###     import of tsplib file format into dictionary
###
###     Author: Patrick Nisble
###     Python ver.: 2.7+ / 3.3+

import re

def readTspData(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        clean = [x.lstrip() for x in content if x != " "]
        tupel = []

        nnum = re.compile(r'[^\d]+')

        for elem in clean:
            if elem.startswith("DIMENSION"):
                dim = int(nnum.sub("",elem))

        for item in clean:
            for x in range(1,dim + 1):
                if item.startswith(str(x)):
                    c1,space,c2 = item.partition(' ')
                    b1,space,b2 = c2.partition(' ')
                    tupel.append((c1.strip(),(b1.strip(),b2.strip())))

    return tupel

def elem(elem,node):
    if elem == "x":
        return node[1][0]
    elif elem == "y":
        return node[1][1]

def distEucl(n1,n2):
    import numpy as np
    dx = (elem("x",n1)-elem("x",n2))
    dy = (elem("y",n1)-elem("y",n2))
    return np.sqrt(dx**2+dy**2)

def distGeo(n1,n2):
    return

tspDict = readTspData("data/berlin52.tsp")

print(tspDict)

print(elem("x",tspDict[1]))
