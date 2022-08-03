import sys
n =int(sys.stdin.readline())
cnt = 0
while cnt < n:
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
    cnt += 1