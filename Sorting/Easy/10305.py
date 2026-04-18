import sys
sys.setrecursionlimit(10000)

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    stack.append(u)

while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    visited = [False]*(n+1)
    stack = []
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    
    stack.reverse()
    print(*stack)