import sys
sys.stdin = open('./2587.txt')

hash = {}
for i in range(1, 6):
    s = input()
    if 'FBI' in s:
        hash[s] = i

if not hash:
    print('HE GOT AWAY!')
else:
    print(" ".join(map(str, sorted(hash.values()))))
