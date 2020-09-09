class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class GraphNode:
    def __init__(self, value):
        self.value = value
        #self.next = None
        self.neightbors = []

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = [] # Adjecency List representation of a graph

    def __repr__(self):
        return f"Node({repr(self.value)})"

# this graph is Cyclic b/c c and b are connected and b visits itself :D
# if there's any play anywhere on the graph that you can return to a place you've already seen
    # then the entire graph is Cyclic :D

a = Node("A")
b = Node("B")
c = Node("C")

a.neighbors.append(b)
a.neighbors.append(c)

print(a.neighbors)

b.neighbors.append(b)
b.neighbors.append(c)
c.neighbors.append(b) # We've made a bi-directional edge, we manually need to put connections in both
                        #directions





