from graph import Graph
from stack import MyStack
# We only need Graph and Stack for this question!

def find_mother_vertex(g):
    # Traverse the Graph Array and perform DFS operation on each vertex
    # The vertex whose DFS Traversal results is equal to the total number
    # of vertices in graph is a mother vertex
    num_of_vertices_reached = 0
    for i in range(g.vertices):
        num_of_vertices_reached = perform_DFS(g, i)
        if (num_of_vertices_reached is g.vertices):
            return i
    return - 1

    # Performs DFS Traversal on graph starting from source
    # Returns total number of vertices which can be reached from source


def perform_DFS(g, source):
    num_of_vertices = g.vertices
    vertices_reached = 0  # To store how many vertices reached from source
    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you push it into stack
    visited = [False] * num_of_vertices
    # Create Stack (Implemented in previous section) for Depth First Traversal
    # and Push source in it
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while not stack.is_empty():
        # Pop a vertex/node from stack
        current_node = stack.pop()
        # Get adjacent vertices to the current_node from the list,
        # and if only push unvisited adjacent vertices into stack
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                visited[temp.data] = True
                vertices_reached += 1
            temp = temp.next_element
        # end of while
    return vertices_reached + 1  # +1 is to include the source itself

if __name__ == "__main__" :
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    print(find_mother_vertex(g))
