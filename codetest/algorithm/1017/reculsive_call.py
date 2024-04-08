def multiple(data):
    if data <= 1:
        return data
    else:
        return data*multiple(data-1)

print(multiple(10))

import random

def sum_list(data):
    if len(data) == 1:
        return data[0]
    
    else:
        return data[0] + sum_list(data[1:])
data = random.sample(range(10), 5)

print(sum_list(data), data)

def palindrome(string):
    if len(string) == 1:
        return True
    elif string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

print(palindrome('level'))

def foo(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:
        return foo(3*n + 1)     
    else:
        return foo(n / 2)
        
print(foo(3))

def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    else:
        return(func(data-1) + func(data-2) + func(data-3))

print(func(4))