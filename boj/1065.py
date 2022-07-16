X = int(input())
cnt = 0

for i in range(1, X +1):
    if len(str(i)) == 1:
        cnt += 1
    # 중복되는 항을 제거 하기위해 집합으로 생성
    li = set()
    for j in range(len(str(i))-1):
        ## 각 자리수의 차를 계산하여 집합에 추가
        n = int(str(i)[j])-int(str(i)[j+1])
        li.add(n)
    ## 자릿수의 차가 1개 이면 cnt를 더함
    if len(li) == 1:
        cnt += 1
print(cnt)

