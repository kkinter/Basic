import sys
sys.stdin = open('./1371.txt')
s = sys.stdin.read().replace('\n', '').replace(' ', '')
dic = {}
for i in s:
    if i not in dic:
        dic[i] = 0
    if i in dic:
        dic[i] += 1
max_val = max(dic.values())
arr = []
for key, val in dic.items():
    if val == max_val:
        arr.append(key)
arr = sorted(arr)
for i in arr:
    print(i, end='')
print()