li = set()
for i in range(34):
    for j in range(21):
        if 3*i + 5*j < 100:
            li.add(3*i+5*j)

print(li)
for i in li:
    