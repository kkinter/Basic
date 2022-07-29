t = int(input())
for i in range(t):
    n = int(input())
    print(f"#{i+1}")
    if n >= 50000:
        print(n // 50000, end=' ')
        n = n % 50000
    else:
        print(0, end=' ')
    if n >= 10000:
        print(n // 10000, end=' ')
        n = n % 10000
    else:
        print(0, end=' ')
    if n >= 5000:
        print(n // 5000, end=' ')
        n = n % 5000
    else:
        print(0, end=' ')
    
    if n >= 1000:
        print(n // 1000, end=' ')
        n = n % 1000
    else:
        print(0, end=' ')

    if n >= 500:
        print(n // 500, end=' ')
        n = n % 500
    else:
        print(0, end=' ')

    if n >= 100:
        print(n // 100, end=' ')
        n = n % 100
    else:
        print(0, end=' ')

    if n >= 50:
        print(n // 50, end=' ')
        n = n % 50
    else:
        print(0, end=' ')
    
    if n >= 10:
        print(n // 10, end='')
        n = n % 10
    else:
        print(0, end='')
    print()