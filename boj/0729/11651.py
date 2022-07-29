import sys 
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    coor = list(map(int, input().split()))
    arr.append(coor[::-1])

arr = sorted(arr) # 2차원 배열 sort 
for j in arr:
    print(j[-1], j[0])


