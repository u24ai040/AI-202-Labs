INT_MAX = 10000000

class Queue:
    def __init__(self):
        self.q = []

    def append(self, item):
        self.q.append(item)

    def popleft(self):
        return self.q.pop(0)

    def __bool__(self):
        return len(self.q) != 0

def bfs_all_paths_costs(graph, start, goal):
    queue = Queue()
    queue.append((start, [start], 0))
    results = []
    price = 0

    while queue:
        current, path, cost = queue.popleft()

        if current == goal:
            results.append((path, cost))

        for i in range(14):
            if graph[current][i] != INT_MAX:
                if i not in path:
                    price = price + graph[current][i]
                    queue.append((i, path + [i], price))

    return results

def addEdge(graph, u, v, d):
    graph[u][v] = d
    graph[v][u] = d


def main():
    n = 14
    graph = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(INT_MAX)
        graph.append(row)

    addEdge(graph, 0, 1, 283)
    addEdge(graph, 0, 2, 345)
    addEdge(graph, 0, 3, 182)
    addEdge(graph, 3, 4, 176)
    addEdge(graph, 4, 2, 144)
    addEdge(graph, 4, 6, 185)
    addEdge(graph, 2, 1, 169)
    addEdge(graph, 2, 5, 189)
    addEdge(graph, 2, 6, 134)
    addEdge(graph, 1, 5, 256)
    addEdge(graph, 5, 7, 150)
    addEdge(graph, 5, 6, 215)
    addEdge(graph, 6, 8, 305)
    addEdge(graph, 6, 9, 247)
    addEdge(graph, 9, 8, 101)
    addEdge(graph, 8, 10, 97)
    addEdge(graph, 10, 11, 181)
    addEdge(graph, 10, 12, 215)
    addEdge(graph, 12, 11, 50)
    addEdge(graph, 12, 13, 107)
    addEdge(graph, 7, 12, 312)
    addEdge(graph, 7, 8, 253)
    addEdge(graph, 7, 10, 254)

    bfs_results = bfs_all_paths_costs(graph, 7, 0)

    count = 0
    print("\nBFS Paths & Costs:")
    for path, cost in bfs_results:
        print("Path:", path, "| Cost:", cost)
        count = count + 1

    print("\nTotal paths found:", count)


main()
