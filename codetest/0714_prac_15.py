s = input()
li = []
cnt = 0
while cnt <= len(s)-1:
    if s[cnt] == 'a':
        li.append(cnt)
        cnt += 1
    else:
        cnt += 1
for i in li:
    print(i, end=" ")