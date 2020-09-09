"""
We have algorithms for traversing these:
----------------------------------------
Every search tree is a graph
Linked list is a graph

The general code that we will write today will work on any graph
Including linked lists :D 

Graphs
------

Nodes connected by edges
Vertexes - Vertices - Verts

Directed vs Undirected
    Directed has one-way edges

Cyclic vs Acyclic:
    Cyclic has a way to 
    Binary Search Trees = Acyclic
    Linked Lists = Cyclic

Weighted edges:
    "Cost" with traversing an edge

LL:

cur = head
while cur is not None:
    print(cur)
    cur = cur.next

Binary Tree:

traverse(node):
    if node is None:

    traverse(node.left)
    print(node)
    traverse(node.right)

General graph:

???

"""