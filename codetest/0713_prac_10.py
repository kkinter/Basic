def foo(numbers,number):
    cnt = 0
    for i in numbers:
        if i == number:
            cnt +=1
    return cnt

print(foo([7, 17, 10, 5, 4, 3, 17, 5, 2, 5],5))