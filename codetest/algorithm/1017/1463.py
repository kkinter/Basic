# https://www.acmicpc.net/problem/1463
# f(i) = min( f(1을 빼는 것), f(2를 나누는 것), f(3을 나누는 것)) + 1
x = int(input())
dp = [0] * (1000001)
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[x])