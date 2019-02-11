import sys
from adjacency import AdjacencyList

"""
This program reads a graph from either stdin, or a filename from the command
line.  It then determines the minimum core of the input graph, and outputs
whether the graph is a cop-win graph, or a robber-win graph, and ouputs the
min core.

The current runtime is kinda not great: O(n m log n).
"""

def main():
    if len(sys.argv) == 2:
        inputStream = open(sys.argv[1])
    else:
        imputStream = sys.stdin

    G = AdjacencyList(inputStream)

    if debug:
        print("read graph:")
        print(G)

    while True:
        v = G.getDominatedVertex()
        if debug: print("got dominated vertex: ", v)
        if v == None:
            break
        G.removeVertex(v[0])

        if debug:
            print("graph is now:")
            print(G)

    if G.getOrder() == 1:
        print("the graph is a cop-win graph")
    else:
        print("the graph is a robber-win graph")

    print("the min core is:")
    print(G)
    

if __name__ == '__main__':
    debug = False
    main()
