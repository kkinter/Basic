n = int(input())
cnt = 0
if (n % 5) % 3 == 0 :
    cnt += (n //5) + (n % 5)//3  
    print(cnt)  
# n % 3의 나머지가 3보다 큰 경우가 있음
elif (n % 3) % 5 == 0:
    cnt += (n //3) + (n % 3)//5
    print(cnt)
elif (n % 3) % 5 == 1 :
    cnt += ((n-10) // 3) + 2 
    print(cnt)
elif (n % 3) % 5 == 2 :
    cnt += ((n-5) // 3) + 1 
    print(cnt)
else:
    print('-1')