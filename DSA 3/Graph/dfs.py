def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {
'A': ['B','C'],
'B': ['A','D','E'],
'C': ['A'],
'D': ['B'],
'E': ['B']
}

# dfs(graph, "A")



# dfs without recursion
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if not in visited:
                    stack.append(neighbor)