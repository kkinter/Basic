t = int(input())

for i in range(1,t+1):
    num = int(input())
    li = set()
    cnt = 0
    while len(li) < 10:
        for j in str(num*(cnt+1)):
            li.add(j)
        
        cnt +=1
    
    print(f"#{i} {num*(cnt)}")
