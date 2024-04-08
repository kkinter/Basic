n =int(input())

for i in range(1,n+1):
    a, b =map(int,input().split())
    li = []
    for j in range(a):
        m, l, p = map(int,input().split())
        li.append(round(m*0.35 + l*0.45 + p*0.2))
        
    li.sort()
    check_rank = li.index(li[b])+1
    print(li)

    if check_rank <= a//10:
        print(f"#{i} A+")
    elif check_rank <= a//10*2:
        print(f"#{i} A0")
    elif check_rank <= a//10*3:
        print(f"#{i} A-")
    elif check_rank <= a//10*4:
        print(f"#{i} B+")
    elif check_rank <= a//10*5:
        print(f"#{i} B0")
    elif check_rank <= a//10*6:
        print(f"#{i} B-")
    elif check_rank <= a//10*7:
        print(f"#{i} C+")
    elif check_rank <= a//10*8:
        print(f"#{i} C0")
    elif check_rank <= a//10*9:
        print(f"#{i} C-")
    elif check_rank <= a//10*10:
        print(f"#{i} D0")

 
