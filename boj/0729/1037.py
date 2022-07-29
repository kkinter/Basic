# import sys
# sys.stdin = open("1037.txt")

n = int(input())
common = list(map(int, input().split()))
common = sorted(common)
print(common[0] * common[-1])