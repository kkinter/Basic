# https://www.acmicpc.net/problem/1629

# 10 ^ 11 dp로 풀면 메모리 초과
a, b, c = map(int, input().split())
dp = [0] * (b + 1)
dp[1] = a
for idx in range(2, b + 1):
    dp[idx] = (dp[idx-1] * a) % c

# 분할 정복 (DAC)
a, b, c = map(int, input().split())
def dac(a, b, c):
    # 지수가 1이라면, a를 c로 나눈 값으로 리턴
    if b == 1:
        return a % c
    # 지수가 2로 나누어 진다면, 
    elif b % 2 == 0:
        return (dac(a, b // 2, c)**2) % c
    # 지수가 2로 나누어 지지 않는다면, 
    else:
        return ((dac(a, b // 2, c) ** 2) * a) % c
print(dac(a, b, c)) 
