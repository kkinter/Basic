
li = ['.','.','X','.','.','X','X','.','.','.']
temp = ''
for i in li:
    temp += i

temp = temp.split('X')
for j in temp:
    if len(j) > 1:
        print(j)  