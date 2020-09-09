"""
This uses a stack - another place you can use a stack to get effective traversals with recursion!!

A recursive version of depth first traversal might be somemthing like that

def dft_recursive(node):
    # Broken pseudocode - broken base case? 

    for n in node.neighbors:
        dft_recursive(n)

"""

class Stack:
    pass

def dft(node):
        # Create a queue to hold nodes to visit
    to_visit = Stack()
    
    # Create a set to hold visited nodes
    visited = set()

    # Initialize: add the starting node to the queue
    to_visit.push(node)

    # While queue not empty:
    while to_visit.size() > 0:
        # dequeue first entry
        v = to_visit.pop()

        # if not visited:
        if v not in visted:
            
            # Visit the node - whatever we wanna do when we get there (print it out)
            print(v)

            # Add it to the visited set
            visted.add(v)

            # enqueue all of its neighbors
            for n in v.neighbors:
                to_visit.add(n)

