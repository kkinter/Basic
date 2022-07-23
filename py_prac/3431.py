t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    if c > b:
        print(f"#{i+1} -1")
    elif c < a:
        print(f"#{i+1} {a-c}")
    else:
        print(f"#{i+1} 0")