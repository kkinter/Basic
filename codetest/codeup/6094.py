a = int(input())
li = list(map(int,input().split()))
temp = li[0]
for i in li:
    if temp >= i:
        temp = i
print(temp)
