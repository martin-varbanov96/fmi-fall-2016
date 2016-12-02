import math
import queue

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         if len(self.data) > 1:
#             self.add_child(Node(self.data[:int((len(self.data)+1)/2)]))
#             self.add_child(Node(self.data[int(len(self.data)/2):]))

#     def add_child(self, obj):
#         self.children.append(obj)

#     def print_tree(self):
#         curr_level=[self]
#         while curr_level:
#             nextlevel=[]
#             for obj in curr_level:
#                 print("*{}".format(obj.data), end="")
#                 for chld in obj.children:
#                     nextlevel.append(chld)
#             print("*")
#             curr_level=nextlevel

# hable = Node(input_var)
# hable.print_tree()

def wave_traverse(input_graph):
    visited_list=dict()
    for node in input_graph:
        visited_list[node]=False
    que = queue.Queue()
    while(!que.empty())


g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }

