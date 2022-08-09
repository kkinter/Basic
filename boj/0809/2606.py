import sys
sys.stdin = open('./2606.txt')

vertex = int(input())
edge = int(input())
adj_list = [[] * (vertex + 1) for _ in range(vertex + 1)]
visited = [False] * (vertex + 1)

for i in range(edge):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

cnt = 0
def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    cnt += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

    return cnt

print(dfs(adj_list, 1, visited) - 1)

