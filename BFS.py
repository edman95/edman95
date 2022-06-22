import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def dibujar_grafo(m):

    G = nx.Graph()

    for i in range(len(m)):
        G.add_node(i+1)
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 0:
                G.add_edge(i+1, j+1)
    
    nx.draw_networkx(G)
    plt.show()
    return 0

graph = [
    [0,1,0,0,0,0,0,1],
    [0,0,1,1,0,0,0,0],
    [0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,0],
]
print(graph)

def BFS(graph, root):

    path = []
    q = []
    visited = [False] * len(graph)
    visited[root] = True
    q.append(root)

    while q:
        root = q.pop(0)
        path.append(root+1)
        for i in range(len(graph[root])):
            if graph[root][i] != 0:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
    
    return path

def DFS(graph, root):
    
    path = []
    s = []
    visited = [False] * len(graph)
    visited[root] = True
    s.append(root)
    
    while s:
        root = s.pop()
        path.append(root+1)
        for i in range(len(graph[root])):
            if graph[root][i] != 0:
                if visited[i] == False:
                    s.append(i)
                    visited[i] = True
    
    return path

print("BFS:", BFS(graph,[0,0,0]))
print("DFS:", DFS(graph,0))
dibujar_grafo(graph)






