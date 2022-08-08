n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] <= m:
                res = max(res, arr[i] + arr[j] + arr[k])
print(res)