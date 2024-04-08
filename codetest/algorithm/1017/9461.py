# https://www.acmicpc.net/problem/9461
# p(1) = 1 
# f(n) = f(n-2) + f(n-3)
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for idx in range(6, 101):
    dp[idx] = dp[idx - 2] + dp[idx - 3]
t= int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])


