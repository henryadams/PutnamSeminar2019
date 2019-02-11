class Graph:
    """
    An abstract class for a graph.  This provides the necessary operations for
    finding a min core.

    Currently there is only 1 concrete subclass: a naive adjacency list that
    finds a dominated vertex via brute force.  In order to implement the nice
    triangle algorithm, one would make a different sublcass of this.
    """
    def getDominatedVertex(self):
        """
        If u dominates v, returns (u, v).  If no dominated vertex exists,
        returns None.
        """
        raise NotImplementedError

    def removeVertex(self, vertex):
        """Removes the given vertex"""
        raise NotImplementedError

    def getOrder(self):
        """Returns the number of vertices in the graph"""
        raise NotImplementedError


