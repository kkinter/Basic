import sys
from pprint import pprint

sys.stdin = open('./2897.txt')
r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
res = 0
res2 = 0
res3 = 0
res4 = 0
res5 = 0
for i in range(r - 1):
    for j in range(c - 1):
        arr = []
        for k in range(2):
            for l in range(2):
                arr.append(matrix[i + k][j + l])
                # if matrix[i + k][j + l] == '.':
                #     cnt += 1
        cnt = arr.count('.')
        if cnt == 4:
            res += 1
        if cnt == 3 and '#' not in arr:
            res2 += 1
        if cnt == 2 and '#' not in arr:
            res3 += 1
        if cnt == 1 and '#' not in arr:
            res4 += 1
        if cnt == 0 and '#' not in arr:
            res5 += 1
            

print(res)
print(res2)
print(res3)
print(res4)
print(res5)



        