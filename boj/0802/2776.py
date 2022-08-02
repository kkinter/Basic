import sys
input = sys.stdin.readline
# sys.stdin = open("./2776.txt")

t = int(input()) ## 100만개이니, n^2 X
for i in range(t):
    cnt_1 = int(input())
    note_1 = sorted(list(map(int, input().split())))
    
    cnt_2 = int(input())
    note_2 = list(map(int, input().split()))
    
    arr = [0 for x in range(cnt_2)]
    for j in range(cnt_2):
        if note_2[j] in note_1:
            arr[j] += 1


for k in arr:
    print(k)
