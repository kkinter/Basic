## 2309 일곱 난쟁이

for i in range(9):
    n = int(input())
    li.append(n)

sum_val = sum(li) - 100
temp_li = []
is_end = False
for j in range(len(li)-1):
    for k in range(1,len(li)):
        if li[j] + li[k] == sum_val:
            temp_li.append(li[j])
            temp_li.append(li[k])
            is_end = True
        if is_end == True:
            break
    
                      
for s in temp_li:
    li.remove(s)
li.sort()
print(li)

        
    