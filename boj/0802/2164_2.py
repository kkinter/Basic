
from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
stk = deque(range(1, n + 1))

while len(stk) > 1:
    stk.popleft()
    stk.append(stk.popleft())
    
print(stk[0])