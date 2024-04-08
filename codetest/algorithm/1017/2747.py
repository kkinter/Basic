# https://www.acmicpc.net/problem/2747
# 인덱스 에러 체크
n = int(input())
dp = [0] * (46)
dp[1] = 1
dp[2] = 1

if n > 2:
    for idx in range(3, 46):
        dp[idx] = dp[idx - 1] + dp[idx - 2]
print(dp[n])
