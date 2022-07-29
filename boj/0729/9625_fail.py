# A > B > BA > BAB > BABBA 
import sys
input = sys.stdin.readline

n = int(input())
word = ['A']
cnt = 0
while n > 0:
    for i in range(len(word)):
        if word[i] == 'A':
            word[i] = 'B'
        elif word[i] == 'B':
            word.append('A')
    n -= 1

print(word.count('A'), word.count('B'))

## a, b = b, a + b