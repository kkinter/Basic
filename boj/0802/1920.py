n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    
for j in arr2:
    if j in dic:
        print(1)
    else:
        print(0)