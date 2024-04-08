import sys
sys.stdin = open('./11467.txt')
n = int(input())
dic = {}
cnt = 0
for i in range(n):
    x, y = map(int, input().split())
    if x not in dic:
        dic[x] = y
    elif x in dic:
        if dic[x] != y:
            cnt += 1
            dic[x] = y

print(cnt)
