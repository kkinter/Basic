n = int(input())
li = []
for i in range(n):
    n = int(input())
    if n != 0:
        li.append(n)
    if n == 0:
        li.pop(-1)

if len(li) == 0:
    print(0)
else:
    print(sum(li))