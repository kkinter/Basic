li = [1, 2, 3]
arr = []
for i in li:
    for j in li:
        if i != j:
            arr.append(i + j)
print(arr)