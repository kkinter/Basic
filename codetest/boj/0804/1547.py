import sys
sys.stdin = open('./1547.txt')

arr = [1, 2, 3]
n = int(input())
ball = 1
for _ in range(n):
    x, y = map(int, input().split())
    if ball == x:
        arr[x - 1], arr[y - 1], ball = y, x , y
    elif ball == y:
        arr[x - 1], arr[y - 1], ball = y, x , x

print(ball)