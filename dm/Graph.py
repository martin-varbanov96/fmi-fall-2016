class Graph(object):
	def __init__(self):
		self.nodes=set()
		self.distance={}
		self.edges=dict()

	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self,node_1, node_2):
		self.edges[node_1].add(node_2)

a = Graph()
a.add_node("a")
print(a.nodes)