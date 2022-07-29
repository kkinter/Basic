
import sys
input = sys.stdin.readline
dic = {}
n = int(input())
arr = list(map(int, input().split()))
for j in arr:
    dic[j] = 0
res = sorted(dic.keys())
print(" ".join(map(str, res)))