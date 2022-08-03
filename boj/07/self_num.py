li = set()
temp_num = 0
for i in range(1,10001):
    for j in str(i):
        temp_num += int(j)
    i += temp_num
    li.add(i)
    temp_num =0

li_2 = [x for x in range(1,10001)]

for i in sorted(list(set(li_2)-li)):
    print(i)    

