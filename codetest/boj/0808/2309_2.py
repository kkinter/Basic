arr = []
for i in range(9):
    n = int(input())
    arr.append(n)

interval = sum(arr) - 100

find = False

for j in range(8):
    for k in range(j + 1, 9):
        if arr[j] + arr[k] == interval:
            del arr[j]
            del arr[k - 1]
            find = True
            break
    if find:
        break
    

arr = sorted(arr)
for q in arr:
    print(q)