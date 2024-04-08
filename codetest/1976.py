t = int(input())

for i in range(t):
    h1, m1, h2, m2 = map(int,input().split())
    val1 = h1*60 + m1
    val2 = h2*60 + m2
    if val1 + val2 < 720:
        res = val1 + val2
        print(f"#{i+1} {(res)//60} {(res)%60}")

    else:
        res = val1 + val2 - 720
        print(f"#{i+1} {(res)//60} {(res)%60}")