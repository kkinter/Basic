n, m = map(int, (input().split()))
res = []
for i in range(n):
    arr = input()
    res.append(arr[::-1])

for j in res:
    print(j)