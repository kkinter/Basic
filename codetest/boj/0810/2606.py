import sys
sys.stdin = open('./2606.txt')

n = int(input())
m = int(input())
adj_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

def dfs(v):
    visited[v] = True

    for i in adj_list[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True) - 1)
