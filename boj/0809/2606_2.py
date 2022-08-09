import sys
from pprint import pprint
sys.stdin = open('./2606.txt')

vertex = int(input())
edge = int(input())
adj_list = [[] * (vertex + 1) for _ in range(vertex + 1)] # 0 정점이 없으니까
for i in range(edge):                                     # 연결의 수만큼 for문
    x, y = map(int, input().split())
    adj_list[x].append(y)                                 # 무방향 그래프 key : [arr] > index : [arr]
    adj_list[y].append(x)

# for _ in adj_list:
#     print(_)
# [[],
# [2, 5],     < 1
# [1, 3, 5],  < 2
# [2],        < 3
# [7],        < 4
# [1, 2, 6],  < 5
# [5],        < 6
# [4]]        < 7

                                                          # 모두 연결이 되어 있지 않음.
visited =[False] * (vertex + 1)                           # dfs 기본 양식

def dfs(graph, v, visited):                               # v 는 key 값              
    visited[v] = True
    print(v, *visited, end=' ')
    for j in graph[v]:                                    # graph[v] > adj_list[6]
        print(j)
        if not visited[j]:
            dfs(graph, j, visited)

dfs(adj_list, 6, visited)

