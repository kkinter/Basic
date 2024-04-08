import sys
from pprint import pprint
sys.stdin = open('./21.txt')

n, m = map(int, (input().split()))
adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]
adj_list = [[] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)
    adj_matrix[x][y] = 1
    adj_matrix[y][x] = 1

pprint(adj_matrix)
print(adj_list)
