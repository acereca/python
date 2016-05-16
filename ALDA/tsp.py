###     Python implementation of TSP
###
###     Author: Patrick Nisble
###     Python ver.: 3.3+

def readTspData(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        clean = [x.lstrip() for x in content if x != " "]
        tupel = []
        decl = {}

        for item in clean:
            if item[:1].isdigit():
                c1,space,c2 = item.partition(' ')
                b1,space,b2 = c2.partition(' ')
                tupel.append((c1.strip(),(b1.strip(),b2.strip())))
            elif len(item.split(":")) == 2:
                decl.update({item.split((":"))[0]:item.split(":")[1][1:]})

    tupel.insert(0,(0,decl))
    return tupel

def elem(elem,node):
    if elem == "x":
        return float(node[1][0])
    elif elem == "y":
        return float(node[1][1])

def distEuc(n1,n2):
    import math as m
    dx = (elem("x",n1)-elem("x",n2))
    dy = (elem("y",n1)-elem("y",n2))
    return int(m.sqrt(dx**2+dy**2)+.5)

def distGeo(n1,n2):
    import math as m
    ## node 1
    deg = int(elem("x", n1))
    minu = elem("x", n1) - deg
    latitude1 = m.PI * (deg + 5.0 * min / 3.0) / 180
    deg = int(elem("y", n1))
    minu = elem("y", n1) - deg
    longitude1 = m.PI * (deg + 5.0 * min / 3.0) / 180
    ## node 2
    deg = int(elem("x", n2))
    minu = elem("x", n2) - deg
    latitude2 = m.PI * (deg + 5.0 * min / 3.0) / 180
    deg = int(elem("y", n2))
    minu = elem("y", n2) - deg
    longitude2 = m.PI * (deg + 5.0 * min / 3.0) / 180

    rad = 6378.388
    q1 = m.cos(longitude1 - longitude2 )
    q2 = m.cos(latitude1 - latitude2 )
    q3 = m.cos(latitude1 + latitude2 )
    dij = int(rad * m.acos(.5*((1.0+q1)*q2 - (1.0+q1)*q3)) + .5)

    return dij

def nearestNeighborSort(tspData,startNode):
    sx = elem("x",tspData[startNode])
    sy = elem("y",tspData[startNode])

    distances = []

    #calc distances between startNode and rest
    for i in range(len(tspData)-2):
        if i+1 >= startNode:
            dist = (startNode,i+2,distEuc(tspData[startNode],tspData[i+2]))
        else:
            dist = (startNode,i+1,distEuc(tspData[startNode],tspData[i+1]))
        distances.append(dist)



    return distances


#
def sort(tupellist):
    less = []
    equal = []
    greater = []

    if len(tupellist) > 1:
        pivot = tupellist[0][2]
        for x in tupellist:
            if x[2] < pivot:
                less.append(x)
            if x[2] == pivot:
                equal.append(x)
            if x[2] > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return tupellist


## Main Block / example for distEucl

import sys

# if (len(sys.argv) >= 2 and sys.argv[1].startswith("data")):
#     tspDict = readTspData(sys.argv[1])
#     if len(sys.argv) == 4:
#         print("Distance({}<->{}): {}".format(sys.argv[2],sys.argv[3],distEuc(tspDict[int(sys.argv[2])],tspDict[int(sys.argv[3])])))
# else:
#     print("you gave me something else than a tsplib formatted file, pls retry :|")

tspData = readTspData("data/berlin52.tsp")
neighborList = nearestNeighborSort(tspData,10)
print(neighborList[2][2])
sortedneighborlist = sort(neighborList)
print(sortedneighborlist)
