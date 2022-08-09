from collections import deque
import sys
sys.stdin = open('./2644.txt')

n = int(input()) # vertex
x, y = map(int, input().split())
m = int(input()) # edge
adj_list = [[] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


arr = [0] * (n + 1)

def bfs():
    q = deque()
    q.append(x)

    while q:
        v = q.popleft()
        if v == y:
            return arr[v]
        
        for i in adj_list[v]:
            if not arr[i]:
                arr[i] = arr[v] + 1
                q.append(i)
    return -1
    
 
print(bfs())