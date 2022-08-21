for i in range(3):
    s = input()
    res = []
    cnt = 0
    for i in range(7):
        if s[i] == s[i + 1]:
            cnt += 1
        if s[i] != s[i + 1] or i + 1 == 7:
            res.append(cnt)
            cnt = 0
    print(max(res) + 1)
