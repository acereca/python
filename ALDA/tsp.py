###     Python implementation of TSP
###
###     Author: Patrick Nisble
###     Python ver.: 3.3+

def readTspData(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        clean = [x.lstrip() for x in content if x != ' ']
        tupel = {}
        decl = {}

        for item in clean:
            if item[:1].isdigit():
                c1,space,c2 = item.partition(' ')
                b1,space,b2 = c2.partition(' ')
                tupel.update({int(c1.strip()):{
                                    'x':float(b1.strip()),
                                    'y':float(b2.strip())}})
            elif len(item.split(':')) == 2:
                decl.update({item.split((':'))[0]:item.split(':')[1][1:]})

    tupel['PROPERTIES'] = decl
    return tupel

def distEuc(n1,n2):
    import math as m
    dx = n1['x']-n2['x']
    dy = n1['y']-n2['y']
    return int(m.sqrt(dx**2+dy**2)+.5)

def distGeo(n1,n2):
    import math as m

    latitude = []
    longitude = []

    for node in (n1,n2):
        global m
        deg = int(node['x'])
        minu = node['x'] - deg
        latitude.append(m.pi * (deg + 5.0 * minu / 3.0) / 180)

        deg = int(node['y'])
        minu = node['y'] - deg
        longitude.append(m.pi * (deg + 5.0 * minu / 3.0) / 180)

    rad = 6378.388
    q1 = m.cos(longitude[0] - longitude[1])
    q2 = m.cos(latitude[0] - latitude[1])
    q3 = m.cos(latitude[0] + latitude[1])
    d = int(rad * m.acos(.5*((1.0+q1)*q2 - (1.0+q1)*q3)) + .5)

    return d

def neighborDist(tspData,startNode):
    # sx = tspData[startNode]['x']
    # sy = tspData[startNode]['y']

    distances = {}
    distances['TO'] = []
    #calc distances between startNode and rest

    copyTspData = tspData.copy()
    copyTspData.pop('PROPERTIES')
    copyTspData.pop(startNode)

    for k,v in copyTspData.items():
        if tspData['PROPERTIES']['EDGE_WEIGHT_TYPE'] == 'GEO':
            dist = distGeo(tspData[startNode],tspData[k])
        elif tspData['PROPERTIES']['EDGE_WEIGHT_TYPE'] == 'EUCL_2D':
            dist = distEuc(tspData[startNode],tspData[k])

        distances['TO'].append((k,dist))
    distances['FROM'] = startNode

    return distances

#
def sort(tupellist):
    less = []
    equal = []
    greater = []

    if len(tupellist['TO']) > 1:
        pivot = tupellist['TO'][0][1]
        for x in tupellist['TO']:
            if int(x[1]) < pivot:
                less.append(x)
            if int(x[1]) == pivot:
                equal.append(x)
            if int(x[1]) > pivot:
                greater.append(x)

        return sort({'TO':less})+ \
                equal+ \
                sort({'TO':greater})
    else:
        return tupellist['TO']


## Main Block / example for distEucl

import sys

# if (len(sys.argv) >= 2 and sys.argv[1].startswith('data')):
#     tspDict = readTspData(sys.argv[1])
#     if len(sys.argv) == 4:
#         print('Distance({}<->{}): {}'.format(sys.argv[2],sys.argv[3],distEuc(tspDict[int(sys.argv[2])],tspDict[int(sys.argv[3])])))
# else:
#     print('you gave me something else than a tsplib formatted file, pls retry :|')

## example for eucl_2d data
tspData = readTspData(sys.argv[1])
manipulationData = tspData.copy()
startNode = int(sys.argv[2])
node = startNode
length = 1
print(len(tspData),tspData['PROPERTIES']['EDGE_WEIGHT_TYPE'])
for item in range(len(tspData)-2):
    neighborDict = neighborDist(manipulationData,node)
    sortedNeighborList = sort(neighborDict)
    #print(node,sortedNeighborList[0],item+1)
    manipulationData.pop(node)
    length += sortedNeighborList[0][1]
    node = sortedNeighborList[0][0]

#print(node,(startNode,distEuc(tspData[startNode],tspData[node])))

print(length)
