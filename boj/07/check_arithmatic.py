numbers = [1]
li = set()
cnt = 0
if len(numbers) == 1:
    cnt += 1
for i in range(len(numbers)-1):
    li.add(numbers[i]-numbers[i+1])
if len(li) == 1:
    cnt +=1
print(cnt)
        
