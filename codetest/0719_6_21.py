number = int(input())
li = []

while number >= 1:
    li.append(number % 10)
    number = number//10

for i in li:
    print(i, end='')
    