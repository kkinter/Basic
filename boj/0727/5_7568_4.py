n = int(input())
li = []
res = []

for i in range(n):
    w, h = map(int, input().split())
    li.append([w, h])

for j in range(n):
    cnt = 0
    for k in range(n):
        if li[j][0] < li[k][0] and li[j][1] < li[k][1]:
            cnt += 1
    res.append(cnt + 1)

print(" ".join(res))