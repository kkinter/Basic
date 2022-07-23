n = int(input())
for p in range(n):
    k = int(input())
    s = list(map(int, input().split(" ")))
    maxx = s[-1]
    ans = 0
    for i in range(len(s)-2,-1,-1):
        if s[i] < maxx:
            ans += (maxx-s[i])
        if s[i] > maxx:
            maxx = s[i]
    print("#%d %d" %(p+1 , ans))