from pprint import pprint
import sys
# sys.stdin = open('./9445.txt')


t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for j in range(n):
        for k in range(m):
            for l in range(k + 1, m):
                if matrix[k][j] == 1 and matrix[l][j] == 0:
                    cnt += 1

    print(cnt)