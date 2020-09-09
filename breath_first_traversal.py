"""
A treversal is when you visit all of the nodes of a graph and you start where ever
Traversals may be different depending on where you start

Like witha linked list: A -> B -> C -> D

If we start at A we go through all of the nodes
However, if we start at C we can only go to D


Breadth-first Traversal - Ripples in a pond - Queue

While there is still something in the queue, dequeue it
Make sure it's not visited and if it isn't, mark it is a visited - add it to the visted set
Add it's neighbors to the queue 
Repeat

Like ripples in a pond because of the QUEUE
    We check the closest neighbors to process first and then reach out to the next nearest etc

"""



def bft(self, node):
    # Create a queue to hold nodes to visit
    to_visit = Queue()
    
    # Create a set to hold visited nodes
    visited = set()

    # Initialize: add the starting node to the queue
    to_visit.enqueue(node)

    # While queue not empty:
    while to_visit.size() > 0:
        print(to_visit.queue)

        # dequeue first entry
        v = to_visit.dqueue()

        # if not visited:
        if v not in visted:
            
            # Visit the node - whatever we wanna do when we get there (print it out)
            print(v)

            # Add it to the visited set
            visted.add(v)

            # enqueue all of its neighbors
            for n in v.neighbors:
                to_visit.enqueue(n)


