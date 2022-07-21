n = int(input())
arr = list(map(int,input().split()))
print(sorted(arr)[(n//2)])
# print(list(arr)[n//2+1])