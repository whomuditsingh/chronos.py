from collections import deque

def find_shortest_path(graph, start, goal):
    # Queue stores tuples of (current_node, path_to_this_node)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (current_node, path) = queue.popleft()
        if current_node == goal:
            return path

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Create a new path list by appending the neighbor
                new_path = list(path)
                new_path.append(neighbor)
                queue.append((neighbor, new_path))

    return None

# Testing
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

path = find_shortest_path(graph, 'A', 'F')
print(f"Shortest path from A to F: {path}")