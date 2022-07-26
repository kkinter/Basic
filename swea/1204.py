t = int(input())
for i in range(1, t + 1):
    a = int(input())
    res = {}
    achive = list(map(int, input().split()))
    for j in achive:
        if j not in res:
            res[j] = 1
        if j in res:
            res[j] += 1
    max_val = max(res, key = res.get)
    print(f"#{a} {max_val}")