from graph import Graph

class AdjacencyList(Graph):
    """
    An adjacency list undirected graph implementation.

    self.vertices is a dictionary with keys being vertices, and values being
    sets of adjacent vertices.

    NOTE: in this implementation, a vertex is explicitly marked as adjacent to
    itself.
    """

    def __init__(self, inputStream):
        """
        Deserialize a graph from an input stream.  For example, a 3-cycle could
        be encoded as:
        2
        a b c
        b c

        The first line is the number of lines to follow.  For each subsequent
        line, the first entry is a vertex, and every subsequent entry is a
        neighbor of this vertex.  If the input isn't an undirected graph, this
        will add the missing edges.

        Runtime is O(n + m).
        """
        numVertices = int(inputStream.readline())
        self.vertices = {}
        for _ in range(numVertices):
            line = inputStream.readline().split()
            self.vertices[line[0]] = set(line)
        for v, adj in list(self.vertices.items()):
            for u in adj:
                if u in self.vertices:
                    self.vertices[u].add(v)
                else:
                    self.vertices[u] = set([v, u])

    def getDominatedVertex(self):
        """
        If u dominates v, returns (u, v).  If no dominated vertex exists,

        Runtime is O(m log n), because we visit each edge at most twice, and
        log comes from set operations.
        """
        for vertex, adj in self.vertices.items():
            # a dominated vertex must be dominated by one of its neighbors
            for neighbor in adj:
                if neighbor is not vertex and adj <= self.vertices[neighbor]:
                    # vertex is dominated by neighbor
                    return (vertex, neighbor)
        return None

    def removeVertex(self, vertex):
        """Removes the given vertex"""
        # remove vertex from any lists that contain it
        for neighbor in self.vertices[vertex]:
            if neighbor is not vertex:
                self.vertices[neighbor].discard(vertex)
        del self.vertices[vertex]

    def getOrder(self):
        """Returns the number of vertices in the graph"""
        return len(self.vertices)

    def __repr__(self):
        order = str(self.getOrder())
        vertices = [v + " " + " ".join(adj) for v, adj in self.vertices.items()]
        return order + "\n" + "\n".join(vertices)
