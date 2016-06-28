import numpy as np
import sys

import heapq
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

def dijkstra(aGraph, start):
    print("Dijkstra's shortest path")
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

## MAIN BLOCK
if True:
    tspData = readTspData(sys.argv[1])
    nodes = np.array(tspData)[:,1:]
    # nearest neighbor search in numpy
    diff = nodes.reshape(nodes.shape[0],1,2) - nodes
    D = (diff ** 2).sum(2)
    i = np.arange(nodes.shape[0])
    D[i,i] = np.inf
    i = np.argmin(D,1)
    # output nearest neighbor by node nr

    from scipy.spatial import Delaunay
    tri = Delaunay(nodes)
    print(tri.simplices)


    import matplotlib
    import matplotlib.pyplot as plt
    plt.plot(nodes[:,0],nodes[:,1],linestyle='none',marker=".")
    plt.triplot(nodes[:,0],nodes[:,1],tri.simplices.copy())
    plt.show()

    g = Graph()

    for elem in tspData:
        #print(elem)
        g.add_vertex(elem[0])

    for elem in tri.simplices.copy():
        dist = lambda l,a,b: np.sqrt((nodes[l[a],0]-nodes[l[b],0])**2+(nodes[l[a],1]-nodes[l[b],1])**2)
        g.add_edge(elem[0],elem[1],dist(elem,0,1))
        print(elem[:2],dist(elem,0,1))
        g.add_edge(elem[1],elem[2],dist(elem,1,2))
        print(elem[1:],dist(elem,1,2))
        g.add_edge(elem[0],elem[2],dist(elem,0,2))
        print(elem[[0,2]],dist(elem,0,2))


    dijkstra(g, g.get_vertex(1))
    shortest_edges = []
    for n in range(len(nodes[:,0])):
        target = g.get_vertex(n)
        path = [n]
        shortest(target,path)
        shortest_edges.append(np.array(path[::-1]))
        print('The shortest path for {}: {}'.format(n,path[::-1]))

    print(type(tri.simplices.copy()))
    print(type(shortest_edges.copy()))


    plt.plot(nodes[:,0],nodes[:,1],linestyle='none',marker='.')
    for l in shortest_edges:
        plt.plot(nodes[l,0],nodes[l,1],'g-')
    plt.show()
