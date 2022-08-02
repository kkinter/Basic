import sys

sys.stdin = open("./25192.txt")

n = int(input())
arr = set()
cnt = 0
for i in range(n):
    chat = input()
    if chat == 'ENTER':
        cnt += len(arr)
        arr = set()
    else:
        arr.add(chat)

cnt += len(arr)

print(cnt)