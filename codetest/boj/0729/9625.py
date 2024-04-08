# A > B > BA > BAB > BABBA 
import sys
input = sys.stdin.readline

n = int(input())
a = 1
b = 0

while n > 0:
    a, b = b, a + b
    n -= 1

print(a, b)
## a, b = b, a + b