li = set()
res = {x for x in range(1, 10001)}
for i in range(1, 10001):
    digit = 0
    for j in str(i):
        digit += int(j)
    self_num = i + digit
    li.add(self_num)
arr =sorted(list(res - li))
for q in arr:
    print(q)