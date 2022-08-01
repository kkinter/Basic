n = int(input())
stk = list(map(int, input().split()))


for i in range(1, n + 1):
    for j in stk:
        if i != j:
            print(stk, i, j)
            stk.pop(0)
            