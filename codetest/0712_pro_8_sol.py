
numbers = [0, 20, 100, 40]
max_num = numbers[0] # float("-inf")
second_number = numbers[0] # float("-inf") 0번쨰 인덱스에 가장 큰 값이 나올 경우가 있기 떄문에 
# 1. 전체 숫자를 반복
for n in numbers:
    # 만약에, n이 최대보다 크다면
    if max_num < n:
        # 최대값이었던 것이 두번째로 큰 수
        second_number = max_num
        max_num = n
    # elif second_number < n < max_num:
    #     second_number = n
    elif second_number < n and n < max_num:
        second_number = n
print(second_number)