i = [1,1,1,1,1,0,0,1,1,1]
ck_sq = 0
res = 0 
for j in range(len(i)-1):
    if ck_sq == 2: # k-1
        if i[-1] == 1:
            res += 1
    
    if i[j] == 1:
        ck_sq += 1
        if ck_sq == 3: # k
            print("ck 가 3이네요")
            if i[j+1] != 1:
                print("뒤에 1이 없네요 연속하네요")
                res+=1
            else:
                print("뒤에 1이 있어요")
                ck_sq = 0
         
        print(ck_sq,res)
    
    elif i[j] == 0:
        ck_sq = 0
    

print(res,'결과') 
