while True:
    s= input()
    cnt = 0
    if s == '#':
        break
    for i in s:
        if i in 'aeiou' or i in 'AEIOU':
            cnt += 1
    print(cnt)

