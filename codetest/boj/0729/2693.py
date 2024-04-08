# import sys
# sys.stdin = open("2693.txt")

n = int(input())
for i in range(n):
    arr = sorted(list(map(int, input().split())))
    print(arr[-3])