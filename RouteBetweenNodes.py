
# Find if there is a path between two vertices in a directed graph
def is_route(graph,start,end):
    """
    Find if there is a path between two vertices in a directed graph using bfs
    :param graph: graph
    :param start: start point
    :param end: end point
    :return: if there is a route between two points then return true else return false
    """
    visited=[]
    queue=[]
    if start == end:
        return True
    visited.append(start)
    queue.append(start)

    while queue:
        temp = queue.pop(0)
        if temp == end:
            return True

        for node in graph[temp]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    return False

graph={
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}
print(is_route(graph, 'A','F')) # True
print(is_route(graph,'A','G')) # True
print(is_graph(graph,'A','Z')) # False
