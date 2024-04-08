t = int(input())
for i in range(t):
    s = int(input())
    n = int(input())
    res = s
    for j in range(n):
        q, p = map(int, input().split())
        res += q * p
    print(res)