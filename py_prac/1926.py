n = int(input())

for i in range(1,n+1):
    res = str(i)  # res str
    for j in range(len(res)): # j int
        if j == len(res-1) and i == n:
            if int(res[j]) % 3 == 0 and int(res[j]) != 0:
                
                print("-",end="")
            else:
                print(res[j],end="")

        if j < len(res)-1:
            if int(res[j]) % 3 == 0 and int(res[j]) != 0:
                
                print("-",end="")
            else:
                print(res[j],end="")
        else:
            if int(res[j]) % 3 == 0 and int(res[j]) != 0:
                print("-",end=" ")
            else:
                print(res[j],end=" ")

        
        