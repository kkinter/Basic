import sys

sys.stdin = open('./2644.txt')
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            arr[i] = arr[v] + 1
            dfs(graph, i, visited)


n = int(input()) # 정점
a, b = map(int, input().split())
m = int(input()) # 간선

adj_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
arr = [0] * (n + 1) # 인덱스가 1부터 시작하니까

for i in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

print(adj_list)
dfs(adj_list, a, visited)

if not arr[b]:
    print(-1)
else:
    print(arr[b])

