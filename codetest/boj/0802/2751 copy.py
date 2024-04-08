import heapq
import sys

input = sys.stdin.readline

heap = []
arr = []
n = int(input())
for i in range(n):
    num = int(input())
    arr.append(num)

arr = sorted(arr)
for j in arr:
    print(j)