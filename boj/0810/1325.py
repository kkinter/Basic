from collections import deque
import sys

sys.stdin = open('./1325.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]

arr = [0] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    adj_list[y].append(x)
    
def bfs(start):
    
    que = deque()
    que.append(start)
    visited[start] = True

    while que:
        v = que.popleft()
        
        for i in adj_list[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
    
    return visited.count(True)

dic = {}

for j in range(1, n + 1):
    visited = [False] * (n + 1)
    dic[j] = bfs(j)

max_val = max(dic.values())
for key, val in dic.items():
    if val == max_val:
        print(key, end=' ')
