###     Python implementation of TSP
###
###     Author: Patrick Nisble
###     Python ver.: 3.3+

def readTspData(filename):
    # read file and clean of empty lines
    with open(filename) as f:
        content = f.read().splitlines()
        clean = [x.lstrip() for x in content if x != ' ']
        tupel = {}
        decl = {}

        # process every line in cleaned file
        for item in clean:

            # if line is node (begins with digit)
            # write as key:value pair into dictionary
            if item[:1].isdigit():
                c1,space,c2 = item.partition(' ')
                b1,space,b2 = c2.partition(' ')
                tupel.update({int(c1.strip()):{
                                    'x':float(b1.strip()),
                                    'y':float(b2.strip())}})
            # if line consists of "string:string"
            # write into "PRPERTIES" entry
            elif len(item.split(':')) == 2:
                key = item.split((':'))[0].strip()
                val = item.split((':'))[1].strip()
                decl.update({key : val})

    tupel['PROPERTIES'] = decl
    return tupel

# calculate euclidian distance between given nodes
def distEuc(n1,n2):
    import math as m
    dx = n1['x']-n2['x']
    dy = n1['y']-n2['y']
    return int(m.sqrt(dx**2+dy**2)+.5)

# calculate geometric distance in km of given nodes
def distGeo(n1,n2):
    import math as m

    latitude = []
    longitude = []

    # calculate longitude and latidude
    for node in (n1,n2):
        global m
        deg = int(node['x'])
        minu = node['x'] - deg
        latitude.append(m.pi * (deg + 5.0 * minu / 3.0) / 180)

        deg = int(node['y'])
        minu = node['y'] - deg
        longitude.append(m.pi * (deg + 5.0 * minu / 3.0) / 180)

    # calculate distance on sphere surface
    rad = 6378.388
    q1 = m.cos(longitude[0] - longitude[1])
    q2 = m.cos(latitude[0] - latitude[1])
    q3 = m.cos(latitude[0] + latitude[1])
    d = int(rad * m.acos(.5*((1.0+q1)*q2 - (1.0+q1)*q3)) + .5)

    return d

# gives list of distance to each neighbor
def neighborDist(tspData,startNode):

    distances = {}
    distances['TO'] = []

    # we dont need the "PROPERTIES" entry in tspData
    copyTspData = tspData.copy()
    copyTspData.pop('PROPERTIES')
    copyTspData.pop(startNode)


    # decide if distGeo or distEuc is needed
    if tspData['PROPERTIES']['EDGE_WEIGHT_TYPE'] == 'GEO':
        for k,v in copyTspData.items():
            dist = distGeo(tspData[startNode],tspData[k])
            distances['TO'].append((k,dist))

    elif tspData['PROPERTIES']['EDGE_WEIGHT_TYPE'] == 'EUC_2D':
        for k,v in copyTspData.items():
            dist = distEuc(tspData[startNode],tspData[k])
            distances['TO'].append((k,dist))

    distances['FROM'] = startNode

    return distances

# quicksort the given list of nodes via quicksort
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

# nearestNeighbor
def nearestNeighborHeuristic(dataDict,startNode):
    manipulationData = dataDict.copy()
    startNode = int(startNode)
    node = startNode
    length = 0

    for item in range(len(dataDict)-2):
        neighborDict = neighborDist(manipulationData,node)
        sortedNeighborList = sort(neighborDict)

        manipulationData.pop(node)
        length += sortedNeighborList[0][1]
        node = sortedNeighborList[0][0]

    return length


## Main Block /nearestNeighbor for given node

# nearestNeighborHeuristic(sys.argv[1],sys.argv[2])

import sys
tspData = readTspData(sys.argv[1])
startNode = sys.argv[2]

fl=0

for i in range(len(tspData)-1):
    length = nearestNeighborHeuristic(tspData,i+1)
    if -length > fl or fl == 0:
        fl = length
    print(i)
    sys.stdout.write("\033[F")


print('Nodes:',len(tspData)-1)
print('Type: ',tspData['PROPERTIES']['EDGE_WEIGHT_TYPE'])
print('NNRT: ',length)
