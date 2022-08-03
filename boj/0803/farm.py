n, m = map(int, input().split())
matritx = [list(map(int, input().split())) for x in range(n)]

for _ in range(n):
    line = list(map(int, input().split()))
    matritx.append(line)

