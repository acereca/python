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
            elif elem.startswith("EDGE"):
                coord = (elem.split())[1]

        tupel.append((0,coord))

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

def distEuc(n1,n2):
    import numpy as np
    dx = (elem("x",n1)-elem("x",n2))
    dy = (elem("y",n1)-elem("y",n2))
    return np.sqrt(dx**2+dy**2)

def distGeo(n1,n2):
    import numpy as np
    ## node 1
    deg = int(elem("x", n1))
    minu = elem("x", n1)
    latitude1 = np.PI * (deg + 5.0 * min / 3.0) / 180
    deg = int(elem("y", n1))
    minu = elem("y", n1)
    longitude1 = np.PI * (deg + 5.0 * min / 3.0) / 180
    ## node 2
    deg = int(elem("x", n2))
    minu = elem("x", n2)
    latitude2 = np.PI * (deg + 5.0 * min / 3.0) / 180
    deg = int(elem("y", n2))
    minu = elem("y", n2)
    longitude2 = np.PI * (deg + 5.0 * min / 3.0) / 180

    rad = 6378.388
    q1 = np.cos(longitude1 - longitude2 )
    q2 = np.cos(latitude1 - latitude2 )
    q3 = np.cos(latitude1 + latitude2 )
    dij = int(rad * np.arccos(.5*((1.0+q1)*q2 - (1.0+q1)*q3)) + 1.0)

    return dij


## Main Block

import sys

if (len(sys.argv) == 2 and sys.argv[1].startswith("data")):
    tspDict = readTspData(sys.argv[1])
    print(tspDict)
else:
    print("you gave me something else than a tsplib formatted file, pls retry :|")
