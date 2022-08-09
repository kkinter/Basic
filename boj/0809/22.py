import sys
from pprint import pprint
sys.stdin = open('./21.txt')


vertex, edge = map(int, input().split())
adj_matrix = [[0] * (vertex + 1) for _ in range(vertex + 1)]
adj_listt = [[] * (vertex + 1) for _ in range(vertex + 1)]

for i in range(edge):
    x, y = map(int, input().split())
    adj_listt[x].append(y)
    adj_matrix[x][y] = 1

print(adj_listt)
pprint(adj_matrix)