t = int(input())
for i in range(t):
    s = list(map(int,input().split()))
    print(f"#{i+1} {max(s)}")