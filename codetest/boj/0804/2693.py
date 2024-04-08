import sys
sys.stdin = open('./2693.txt')

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print(arr[-3])