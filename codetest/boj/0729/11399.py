## 합계 구하기
## "https://www.acmicpc.net/problem/11399"
res = 0
sum = 0
for i in range(1, 5):
    res = res + i
    sum = sum + res
    print(f"{i}번쨰 {res} {sum}")

## 인덱스 구하기 
li = [3, 1, 4, 3, 2]
res = []
li_rev = sorted(li, reverse= True)
for i in li:
    res.append(li_rev.index(i) + 1)
print(res)

ans = 0
ans_sum = 0
for j in res:
    ans += li[j - 1]
    ans_sum += ans
    print(ans, ans_sum)

print(ans_sum)
