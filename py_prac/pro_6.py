numbers = [0, 20, 100]
temp = numbers[0]
for i in numbers:
    if i > temp:
        temp = i
print(temp)