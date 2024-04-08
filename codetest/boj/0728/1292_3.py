a, b = map(int,input().split())
s = []

for i in range(1,b+1):
    for j in range(i) :
        s.append(i)
        
print(s)
print(sum(s[a-1:b]))