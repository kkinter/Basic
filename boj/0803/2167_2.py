
import sys

# sys.stdin = open('./2167.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
k = int(input())
coor = [list(map(int ,input().split())) for _ in range(k)]

dp = [[0]*(m + 1) for x in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]


for row in coor:
    print(dp[row[2]][row[3]] - dp[row[2]][row[1] - 1] - dp[row[0] - 1][row[3]] + dp[row[0] - 1][row[1] - 1] )

    