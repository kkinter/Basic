numbers = [-10, -100, -30]

max = numbers[0]
for i in numbers:
    if i > max:
        max = i

print(max)

numbers.remove(max)
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)