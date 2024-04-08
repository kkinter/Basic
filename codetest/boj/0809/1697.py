from collections import deque
import sys
sys.stdin = open('./1697.txt')
n, m = map(int, input().split())
MAX = 10001
arr = [0] * MAX

def bfs():
    que = deque()
    que.append(n)
    while que:
        now_pos = que.popleft()
        if now_pos == m:
            return arr[now_pos]
        
        dx = [now_pos - 1, now_pos + 1, 2*now_pos]
        for next_pos in dx:
            if 0 <= next_pos <= m and not arr[next_pos]:
                que.append(d)
                arr[d] = arr[now_pos] + 1

print(bfs())

