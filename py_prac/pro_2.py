## while 

s = input()
cnt = 0
sum_val = 0
while True: 
    try:
        if s[cnt] != 0:
            sum_val +=1
            cnt += 1
    except:
        break
print(sum_val)

## for (문자열 그대로)

s = "happy"
cnt_2 = 0
for i in s:
    cnt_2 += 1
print(cnt_2)
