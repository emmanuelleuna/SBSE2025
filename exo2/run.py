from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(graph[node] - visited)
    
    return traversal_order

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    traversal_order = [start]
    
    for neighbor in graph[start] - visited:
        traversal_order.extend(dfs(graph, neighbor, visited))
    
    return traversal_order

def is_connected(graph, node1, node2):
    if node1 not in graph or node2 not in graph:
        return False  # Si un des nœuds n'existe pas
    
    return node2 in bfs(graph, node1)

def shortest_path_bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node] - visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path found

# Example Graph Representation
city_map = {
    '0': {'1', '2', '3'},
    '1': {'0', '4', '5'},
    '2': {'0', '6'},
    '3': {'0', '7'},
    '4': {'1'},
    '5': {'1'},
    '6': {'2'},
    '7': {'3'}
}

# Testing BFS and DFS
print("BFS Traversal:", bfs(city_map, '0'))
print("DFS Traversal:", dfs(city_map, '0'))

# Checking connectivity and shortest path
print("Is 0 connected to 5?:", is_connected(city_map, '0', '5'))
print("Shortest path from 0 to 5:", shortest_path_bfs(city_map, '0', '5'))
print("Is 3 connected to 0?:", is_connected(city_map, '3', '0'))
