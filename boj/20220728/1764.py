# import sys
# sys.stdin = open("1764.txt")


n, m = map(int, input().split())
d = {}
for _ in range(n):
    d_person = input()
    if d_person not in d:
        d[d_person] = 0
    if d_person in d:
        d[d_person] += 1

b = {}
for _ in range(m):
    b_person = input()
    if b_person not in b:
        b[b_person] = 0
    if b_person in b:
        b[b_person] += 1

res = []
for i in d:
    if i in b:
        res.append(i)
res = sorted(res)
print(len(res))
for name in res:
    print(name)