from graph import Graph
from collections import deque 
# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty() 
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex

def bfs_traversal_rec(g, source, visited):
    result = ""
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        current_node = queue.popleft()
        result += str(current_node)
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.append(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited

def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    
    visited = [False] * num_of_vertices
    result, visited = bfs_traversal_rec(g, source, visited)

    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal(g, source, visited)
            result += result_new
    return result


if __name__ == "__main__" :
    g = Graph(4)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        print(bfs_traversal(g, 0))