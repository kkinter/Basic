#최댓값 구하기
numbers = [0,20,100,40]
# max_num = 0 # -값 때문에 
max_num = numbers[0]
# float(".inf")

# 1. 반복
for n in numbers:
    # 2. 만약, max값이 n보다 작으면 바꾼다.
    if max_num < n:
        max_num =n
print(max_num)