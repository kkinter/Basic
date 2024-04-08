a = 19
li = []
cnt = 1
while cnt < 9:
    if a != 1:
        s = a % 2
        li.append(s)
        a //= 2
    else:
        li.append(0)
    cnt += 1
    print(a)
print(li)