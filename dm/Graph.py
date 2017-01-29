import random
class Graph(object):
	def __init__(self):
		self.nodes=list()
		self.distance={}
		self.edges=dict()

	def add_node(self, value):
		self.nodes.append(value)

	def add_edge(self,node_1, node_2, distance):
		self.edges.update({node_1: node_2})
		self.edges.update({node_2: node_1})
		self.distance[node_1, node_2]=distance
		self.distance[node_2, node_1]=distance

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


a = Graph()
a.add_node("a")
a.add_node("b")
a.add_node("c")
a.add_node("d")
a.add_node("e")
a.add_node("f")
a.add_node("g")
a.add_node("h")
a.add_node("j")
a.add_node("w")
for i in range(0, len(a.nodes)-1):
	a.add_edge(a.nodes[i], a.nodes[i+1], random.uniform(0, 100))
print("nodes", a.nodes)
print("EDGES", a.edges)
print("DISTANCE", a.distance)
print("PATH",dijsktra(a,"a"))