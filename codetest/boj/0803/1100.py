import sys

sys.stdin = open('1100.txt')

arr = [list(input()) for _ in range(8)]

cnt = 0

for j in range(8):
    for k in range(8):
        if (j + k) % 2 == 0 and arr[j][k] == 'F':
            cnt += 1

print(cnt)