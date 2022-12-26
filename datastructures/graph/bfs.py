from print_graph import Graph

def bfs(my_graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    
    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a queue for BFS
    queue = []

    # Result string
    result = ""

    # Mark the source node as
    # visited and enqueue it
    queue.append(source)
    visited[source] = True
    

    while queue:

        # Dequeue a vertex from
        # queue and print it
        source = queue.pop(0)
        result += str(source)

        temp=my_graph.graph[source] # original graph will not be affected

        # Get all adjacent vertices of the
        # dequeued vertex source. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        while temp is not None:
            data = temp.vertex
            if not visited[data]:
                queue.append(data)
                visited[data] = True
            temp=temp.next

    return result


# Main to test the above program
if __name__ == "__main__":
    
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(bfs(g, 0))
