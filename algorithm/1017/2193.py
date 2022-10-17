# https://www.acmicpc.net/problem/2193
# f(1) = 1
# f(2) = 1
# f(3) = 2
# f(4) = 3
# f(5) = 5 > f(n) = f(n - 1) + f(n - 2)
n = int(input())
dp = [0] * 91
dp[1] = 1
dp[2] = 1
for idx in range(3, 91):
    dp[idx] = dp[idx - 1] + dp[idx - 2]

print(dp[n])