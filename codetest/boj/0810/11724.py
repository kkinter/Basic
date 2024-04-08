import sys
from pprint import pprint

sys.stdin = open('./11724.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

adj_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

print(adj_list)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, visited,end= ' ')
    for k in graph[v]:
        if not visited[k]:
            dfs(graph, k, visited)
    
cnt = 0
for j in range(1, n + 1):
    if not visited[j]:
    
        cnt += 1
        
        dfs(adj_list, j, visited)
        print()


print(cnt)



    
    


    
    
