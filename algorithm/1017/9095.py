# https://www.acmicpc.net/problem/9095
# f(1) = 1 f(2) = 2 f(3) = 4 

# f(4) = 7



t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for idx in range(4, 11):
        dp[idx] = dp[idx - 1] + dp[idx - 2] + dp[idx - 3]
    print(dp[n])