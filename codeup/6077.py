a = int(input())
results = 0
for i in range(a+1):
    if i % 2 == 0:
        results += i
print(results)