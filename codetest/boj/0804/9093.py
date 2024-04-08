t = int(input())
for i in range(t):
    arr = input().split()
    for j in arr:
        print(j[::-1], end=' ')
    print()