import sys

from sympy import randMatrix
sys.stdin = open('./2001.txt')
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    length = n - m + 1
    sum_li = []
    for idx in range(length):
        sum_val = 0
        for j in range(idx, idx + m):
            sum_val += matrix[idx][j]

        for j in range(idx, idx + m):
            sum_val += matrix[j][idx]
        sum_li.append(sum_val)
    print(sum_li)

            
            

    

