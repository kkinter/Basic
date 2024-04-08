s = input()
l_cnt = 0
r_cnt = 0
is_left = True
for i in s:
    if i == '(':
        is_left = False
    if is_left:
        if i == '@':
            l_cnt += 1
    if not is_left:
        if i == "@":
            r_cnt += 1

print(l_cnt, r_cnt)
