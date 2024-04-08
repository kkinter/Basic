from collections import deque
import sys
from pprint import pprint
sys.stdin = open('./13567.txt')
m, n = map(int, input().split())
x = 0
y = 0
angle = 0
flag = False
for i in range(n):
    com, n = map(str, input().split())
    n = int(n)
    
    direction = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}
    if com == 'TURN':
        if n == 0:
            angle += 90
        if n == 1:
            angle -= 90

    if com == 'MOVE':
        nx = x + n * direction[angle % 360][0]
        ny = y + n * direction[angle % 360][1]
        if 0 <= nx < m + 1 and 0 <= ny < m + 1:
            x = nx
            y = ny
        else:
            flag = True
            break

if flag:
    print(-1)
else:
    print(x, y)
