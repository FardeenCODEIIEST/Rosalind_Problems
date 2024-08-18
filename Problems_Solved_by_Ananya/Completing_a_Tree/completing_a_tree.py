def read_graph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n = int(lines[0].strip())
    edges = []
    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        edges.append((u, v))
    
    return n, edges

def find_connected_components(n, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    component_count = 0
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    for i in range(1, n + 1):
        if not visited[i]:
            component_count += 1
            bfs(i)
    
    return component_count

def minimum_edges_to_tree(n, component_count):
    return component_count - 1

file_path = 'rosalind_tree.txt'

n, edges = read_graph(file_path)
component_count = find_connected_components(n, edges)
result = minimum_edges_to_tree(n, component_count)

with open('output.txt', 'w') as file:
    file.write(f"{result}\n")
