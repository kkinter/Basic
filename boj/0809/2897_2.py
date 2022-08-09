import sys

sys.stdin = open('./2897.txt')
r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]

res = [0, 0, 0, 0, 0] # re
for i in range(r - 1): #  r - c + 1
    for j in range(c - 1):  #  c - 2 + 1
        arr = [] #
        for k in range(2):
            for l in range(2):
                arr.append(matrix[i + k][j + l])
          
        cnt = arr.count('.')
        for q in range(4, -1, -1): 
            if cnt == q and '#' not in arr:
                res[4-q] += 1

for p in res:
    print(p)



        