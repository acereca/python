###     import of tsplib file format into dictionary
###
###     Author: Patrick Nisble
###     Python ver.: 2.7+ / 3.3+

def readTspData(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        clean = [x.lstrip() for x in content if x != " "]
    return clean

def elem(elem,node):
    return node[elem]

def distGeo(n1,n2):
