numbers = set(range(1, 10001)) ## 
gen_numbers = set() ## 중복된 생성자들이 존재하기 때문에, 집합을 사용

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    gen_numbers.add(i)

self_num = sorted(numbers-gen_numbers)
for i in self_num:
    print(i)

