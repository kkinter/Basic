import sys



n =int(input())

for i in range(n,-1, -1):
    if i != 0:
        print(i, end=" ")
    else:
        print(i, end="")