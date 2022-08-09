from collections import deque

MAX = 100001
n, m = map(int, input().split())
arr = [0] * MAX

def bfs():
    que = deque()
    que.append(n)
    while que:
        now = que.popleft()
        if now == m:
            return arr[now]
        
        dx = (now - 1, now + 1, 2*now)
        for d in dx:
            if 0 <= d < MAX and not arr[d]:
                arr[d] = arr[now] + 1
                que.append(d)
print(bfs())
