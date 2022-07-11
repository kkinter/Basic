a, b, c= map(int,input().split())

li = [a,b,c]
temp = li[0]
for i in li:
    if i <= temp:
        temp = i
print(temp)