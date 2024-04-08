t = int(input())
for i in range(t):
    n = int(input())
    li = [x for x in range(8)]
    while n > 0:
        if n >= 50000:
            li[0] = n // 50000
            n %= 50000
            print(n)
        if n >= 10000:
            li[1] = n // 10000
            n %= 10000
            print(n)
        if n >= 5000:
            li[2] = n // 5000
            n %= 5000
            print(n)
        if n >= 1000:
            li[3] = n // 1000
            n %= 1000
            print(n)
        if n >= 500:
            li[4] = n // 500
            n %= 500
            print(n)
        if n >= 100:
            li[5] = n // 100
            n %= 100
            print(n)
        if n >= 50:
            li[6] = n // 50
            n %= 50
            print(n)
        if n >= 10:
            li[7] = n // 10
            n %= 10
            print(n)
        
    print(f"#{i+1} {li}")