t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    res = a + b
    if res % 24 == 0 and res != 0:
        print(f"#{i+1} 0")
    elif res < 24:
        print(f"#{i+1} {a+b}")
    else:
        print(f"#{i+1} {(a+b)%24}")