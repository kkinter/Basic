t = int(input())

for i in range(1,t+1):
    li = set()
    s =input()
    for j in s:
        if j not in li:
            li.add(j)
    print(li)
