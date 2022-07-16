while True:
    a = int(input())
    li = []
    for i in range(1,a):
        if a % i == 0:
            li.append(i)
    if a == -1:
        break

    elif a == sum(li):
        print(f'{a} ='," + ".join(map(str,li)))
    
    elif a != sum(li):
        print(f'{a} is NOT perfect.')
    
