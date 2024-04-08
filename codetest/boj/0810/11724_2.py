import sys
from pprint import pprint

sys.stdin = open('./11724.txt')


n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

print(adj_list)
arr = [[0] * (n + 1)]
print(arr)