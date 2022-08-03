# 쥰내 구리게 푼거 같음


n = int(input())
li = []
cnt = 2
while n != 1:
    if n % cnt == 0:
        n = n/cnt
        li.append(cnt)

    else:
        cnt += 1
for i in li:
    print(i)