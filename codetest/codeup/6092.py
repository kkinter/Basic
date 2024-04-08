n = int(input())
li = list(map(int,input().split()))

li2 = [0]*23
for i in li:
    li2[i-1] += 1
    
for i in li2:
    print(i, end=' ')