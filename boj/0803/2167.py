
import sys

# sys.stdin = open('./2167.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
k = int(input())
coor = [list(map(int ,input().split())) for _ in range(k)]

for i in coor:
    sum_val = 0
    for j in range(i[0] - 1, i[2]):
        for k in range(i[1] - 1, i[3]):
            sum_val += arr[j][k]
    print(sum_val)
