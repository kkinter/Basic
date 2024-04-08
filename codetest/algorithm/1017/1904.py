# https://www.acmicpc.net/problem/1904
# f(1) = 1 , f(2) = 2 f(3) = 5
# f(n) = f(n - 1) + f(n - 2)
# 메모이제이션에 저장할 때, 수가 작으면 메모리 용량도 적어짐,
# dp_list 를 n+1로 할 경우, n 일 때, 인덱스 에러 발생
n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for idx in range(3, n + 1):
    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 15746
print(dp[n]) 
    