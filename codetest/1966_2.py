t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    l = len(arr)
    for j in range(l-1):
        for k in range(l-j-1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    
    print(f"#{i+1} {' '.join(map(str,arr))}")