n = input()
li = []

for i in n:
    li.append(int(i))
res = sorted(li, reverse=True)

print("".join(map(str, res)))