import queue

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def traverse_width(self):
        visited=dict()
        vertucles = self.vertices()
        seed_elmnt = vertucles[0]
        for v in vertucles:
            visited[v]=False
        b=list()
        que = queue.Queue()
        que.put(seed_elmnt)
        visited[seed_elmnt] = True
        while(que.empty() is False):
            a=que.get()
            b.append(a)
            for v in self.__graph_dict[a]:
                if(visited[v] is False):
                    que.put(v)
                    visited[v] = True
        return b

    def edges_of_vertex(self, curr_vertex):
        return self.__graph_dict[curr_vertex]

    def dfs(self, curr_vertex, discovered_vertxes=[]):
        vertexes = self.vertices()
        discovered_vertxes.append(curr_vertex)
        related_edges = self.edges_of_vertex(curr_vertex)
        for i in related_edges:
            if i not in discovered_vertxes:
                self.dfs(i, discovered_vertxes)
        return discovered_vertxes
        # v as discovered
        # for all edges from v to w in G.adjacentEdges(v) do
        #     if vertex w is not labeled as discovered then
        #       recursively call DFS(G,w)
        

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)
    print("Final answer is:", graph.dfs("e"))

