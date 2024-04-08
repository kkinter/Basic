# 시간초과

import sys
input = sys.stdin.readline

n = int(input())
li = [x for x in range(1, n + 1)]
while len(li) >= 2:
    li.pop(0)
    li.append(li[0])
    li.pop(0)
    
    
print(li[0])