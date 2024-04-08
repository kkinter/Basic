# https://www.acmicpc.net/problem/11726
# 2*2  = 2
# 2*3  = 3
# 2*9  = 55
# f(n) = f(n - 1) + f(n - 2)
def func(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return func(n - 1) + func(n - 2)
print(func(9))
n = int(input())
def func_dp(n):
    cache = [0 for i in range(n + 1)]
    cache[0] = 0
    cache[1] = 1
    cache[2] = 2

    for idx in range(3, n + 1):
        cache[idx] = cache[idx - 1] + cache[idx - 2]
    return cache[n]
print(func_dp(n) % 10007)
n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for idx in range(3, 1001):
    dp[idx] = dp[idx-1] + dp[idx-2]
print(dp[n] % 10007)