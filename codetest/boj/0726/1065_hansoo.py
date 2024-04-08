n = input()
cnt = 0

for i in range(1,int(n)+1):
    if len(str(i)) == 1:
        cnt += 1
    li = set()
    for j in range(len(str(i))-1):
        li.add(int(str(i)[j]) - int(str(i)[j + 1]))
    if len(li) == 1:
        cnt += 1
print(cnt)
        
    


         