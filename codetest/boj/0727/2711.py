n = int(input())
for i in range(n):
    idx, n = input().split()
    li = [i for i in n]
    li.pop(int(idx) - 1)
    print("".join(li))
