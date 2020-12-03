# BFS using queue
def bfs(graph,node):
    """
    bsf
    :param graph: graph
    :param node: start node
    """
    visited=[]
    queue=[]
    visited.append(node)
    queue.append(node)

    while queue:
        temp = queue.pop(0)
        print(temp, end=' ')

        for node in graph[temp]:
            if node not in visited:
                visited.append(node)
                queue.append(node)

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

bfs(graph,'A') # A B D C E F G H 
