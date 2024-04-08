word = input() # ABCD
n = int(input()) # 반지의 개수

arr = []
cnt = 0
for i in range(n):
    target = input() # 각 반지의 문자열
    if word in target*2:
        cnt += 1

print(cnt)