# 1. Define the graph as a dictionary (Adjacency List)
# Neha1 = Center, Neha2 = Right, Arjun1 = Right, Arjun2 = Bottom
graph = {
    "Priya": ["Raj", "Aarav", "Akash"],
    "Raj": ["Sunil", "Neha1"],
    "Aarav": ["Neha1", "Arjun1"],
    "Akash": ["Sunil"],
    "Sunil": ["Sneha", "Maya"],
    "Neha1": ["Akash", "Rahul"],
    "Neha2": ["Aarav", "Rahul", "Arjun1"],
    "Sneha": ["Rahul"],
    "Rahul": ["Neha1", "Neha2", "Arjun1", "Pooja"],
    "Arjun1": ["Rahul"],
    "Maya": ["Arjun2"],
    "Arjun2": ["Maya"],
    "Pooja": ["Arjun2"]
}

def bfs_tree(graph, start_node):
    visited = [start_node]
    queue = [start_node]
    bfs_tree = []

    while queue:
        current = queue.pop(0) 
        
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
                    bfs_tree.append((current, neighbor))
    return bfs_tree

def dfs_tree(graph, start_node):
    visited = []
    dfs_tree = []

    def walk(node, parent=None):
        if node not in visited:
            visited.append(node)
            if parent is not None:
                dfs_tree.append((parent, node))
            
            if node in graph:
                for neighbor in graph[node]:
                    walk(neighbor, node)

    walk(start_node)
    return dfs_tree


print(" BFS Tree Edges :")
bfs_edges = bfs_tree(graph, "Priya")
for parent, child in bfs_edges:
    print(f"{parent} -> {child}")

print("\nDFS Tree Edges:")
dfs_edges = dfs_tree(graph, "Priya")
for parent, child in dfs_edges:
    print(f"{parent} -> {child}")