import sys
# sys.stdin = open("./2776.txt")
input = sys.stdin.readline


t = int(input()) ## 100만개이니, n^2 X
for i in range(t):
    cnt_1 = int(input())
    note_1 = list(map(int, input().split()))
    
    cnt_2 = int(input())
    note_2 = list(map(int, input().split()))
    
    dic = {}
    for j in note_1:
        if j not in dic:
            dic[j] = 1
    
    for k in note_2:
        if k in dic:
            print(dic[k], end=' ')
        else:
            print(0, end=' ')
    print()
