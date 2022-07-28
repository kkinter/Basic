
n = int(input())
dict = {}
for _ in range(n):
    name, status = input().split()
    dict[name] = status

res = []
for key, value in dict.items():
    if value == 'enter':
        res.append(key)

res = sorted(res, reverse= True)
for i in res:
    print(i)
