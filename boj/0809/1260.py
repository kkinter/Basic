from collections import deque
import sys
sys.stdin = open('./1260.txt')

n, m, v = map(int, input().split())
adj_list = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)
visited = [False] * (n + 1)

for _ in adj_list:
    _.sort()


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(adj_list, v, visited)
print()
visited = [False] * (n + 1)
bfs(adj_list, v, visited)
print()