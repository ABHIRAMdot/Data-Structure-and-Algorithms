def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            dfs(graph, i, visited)


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



#-------------------------------------------
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end '->')

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)



                