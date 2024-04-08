import sys
from pprint import pprint
sys.stdin = open("_어디에단어가들어갈수있을까.txt")

for test_case in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    maps = [list(map(str, input().split())) for _ in range(n)]
    # maps 의 열을 행으로 전환
    maps2 = list(map(list, zip(*maps)))
    pprint(maps)
    pprint(maps2)