n =int(input())
li = []

for i in range(1,n+1):
    if n % i == 0:
        li.append(i)

for j in li:
    if j != li[-1]:
        print(j, end=' ')
    else:
        print(j, end='')