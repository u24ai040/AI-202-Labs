 # city index mapping
    # 0  Chicago
    # 1  Detroit
    # 2  Cleveland
    # 3  Indianapolis
    # 4  Columbus
    # 5  Buffalo
    # 6  Pittsburgh
    # 7  Syracuse
    # 8  Philadelphia
    # 9  Baltimore
    # 10 New York
    # 11 Providence
    # 12 Boston
    # 13 Portland

INT_MAX = 10000000

def addEdge(graph, u, v, d):
    graph[u][v] = d
    graph[v][u] = d

def go(res, graph, visited, u, v, curr, pcost, path):
    # If we reach the target node (v)
    if curr == v:
        # Store a snapshot of the path and the cost
        res.append((list(path), pcost))
        return

    for i in range(14):
        if graph[curr][i] != INT_MAX and visited[i] == 0:
            # 1. Mark and move forward
            visited[i] = 1
            path.append(i)
            
            go(res, graph, visited, u, v, i, pcost + graph[curr][i], path)

            # 2. Backtrack (undo)
            path.pop()
            visited[i] = 0

def main():
    n = 14
    adj = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(INT_MAX)
        adj.append(row)

    # Adding Edges
    addEdge(adj, 0, 1, 283)
    addEdge(adj, 0, 2, 345)
    addEdge(adj, 0, 3, 182)
    addEdge(adj, 3, 4, 176)
    addEdge(adj, 4, 2, 144)
    addEdge(adj, 4, 6, 185)
    addEdge(adj, 2, 1, 169)
    addEdge(adj, 2, 5, 189)
    addEdge(adj, 2, 6, 134)
    addEdge(adj, 1, 5, 256)
    addEdge(adj, 5, 7, 150)
    addEdge(adj, 5, 6, 215)
    addEdge(adj, 6, 8, 305)
    addEdge(adj, 6, 9, 247)
    addEdge(adj, 9, 8, 101)
    addEdge(adj, 8, 10, 97)
    addEdge(adj, 10, 11, 181)
    addEdge(adj, 10, 12, 215)
    addEdge(adj, 12, 11, 50)
    addEdge(adj, 12, 13, 107)
    addEdge(adj, 7, 12, 312)
    addEdge(adj, 7, 8, 253)
    addEdge(adj, 7, 10, 254)

    res = []
    visited = [0] * n
    visited[0] = 1 
    
    # Run DFS: start node 0, target node 7
    go(res, adj, visited, 0, 7, 0, 0, [0])

    # Display results
    for path, cost in res:
        print(f"Path: {path} | Cost: {cost}")
        
    print("\nTotal paths found:", len(res))

main()